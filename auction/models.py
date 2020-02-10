from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.mixins import TimestampMixin

User = get_user_model()


class Auction(TimestampMixin, models.Model):
    """Auction model"""

    product_description = models.CharField(max_length=256)
    starting_price = models.FloatField(validators=[MinValueValidator(0.1)])
    price_step = models.FloatField(validators=[MinValueValidator(0.1)])
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='winner')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auction'
        verbose_name = _('auction')
        verbose_name_plural = _('auctions')

    @property
    def actual_price(self) -> Decimal:
        try:
            price = self.bets.latest('created_at').price
        except Bet.DoesNotExist:
            price = self.starting_price
        return price

    @property
    def participants(self):
        return [b.created_by for b in self.bets.all()]


class Bet(TimestampMixin, models.Model):
    """All bets for particular auction"""

    auction = models.ForeignKey(Auction, related_name='bets', on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.1)])

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bet'
        verbose_name = _('bet')
        verbose_name_plural = _('bets')
