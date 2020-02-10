from datetime import datetime
import pytz

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Auction, Bet
from .tasks import async_send_email

User = get_user_model()


class AuctionSerializer(serializers.ModelSerializer):
    winner = serializers.SlugRelatedField(slug_field='username', many=False, read_only=True)

    class Meta:
        model = Auction
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at' 'is_active', 'winner')

    def validate(self, data: dict) -> dict:
        """
        Check that the price is correct.
        """
        request = self.context['request']

        end_time = data['end_time'].replace(tzinfo=pytz.UTC)

        if end_time <= datetime.now(end_time.tzinfo):
            raise serializers.ValidationError("Auction end time should be more than current time")

        data.update({'created_by': request.user})
        return data

    def create(self, validated_data):
        """
        Create an auction and notify all other users
        """
        auction: Auction = super().create(validated_data)

        users_to_notify = [u.email for u in User.objects.all() if u != auction.created_by]
        async_send_email.apply_async(
            args=[
                users_to_notify,
                f"Auction #{auction.id}",
                "New auction is available."
            ])

        return auction


class BetSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', many=False, read_only=True)

    class Meta:
        model = Bet
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

    def validate(self, data):
        """
        Check that the price is correct.
        """
        request = self.context['request']

        auction = data['auction']

        if auction.created_by == request.user:
            return serializers.ValidationError('As an auction owner you cannot make a bet')

        if not auction.is_active:
            raise serializers.ValidationError("Auction already closed.")

        if auction.actual_price + auction.price_step > data['price']:
            raise serializers.ValidationError("Bet price should be higher than actual price + step")

        data.update({'created_by': request.user})
        return data

    def create(self, validated_data):
        bet: Bet = super().create(validated_data)
        auction: Auction = bet.auction

        participants_to_notify = [p for p in auction.participants if p != bet.created_by]
        async_send_email.apply_async(
            args=[
                participants_to_notify,
                f"Auction #{auction.id}",
                f"Actual price: {bet.price}"
            ])

        return bet


class BetBriefSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.id', read_only=True)

    class Meta:
        model = Bet
        fields = ('price', 'created_by')


class AuctionDetailedSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=True)
    bets = BetBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Auction
        fields = '__all__'
