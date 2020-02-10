from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from auction.models import Auction, Bet
from auction.serializers import AuctionSerializer, BetSerializer, AuctionDetailedSerializer


class AuctionView(ListCreateAPIView):
    """
    Create and auction or get list of all auctions.
    """
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_active',)


class AuctionDetailedView(RetrieveAPIView):
    """Auction details"""
    queryset = Auction.objects.all()
    serializer_class = AuctionDetailedSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class BetView(ListCreateAPIView):
    """
    Make a bet or get list of all bets.
    """
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = (IsAuthenticated,)
