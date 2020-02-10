from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import AuctionView, AuctionDetailedView, BetView

urlpatterns = [
    path('auctions/', csrf_exempt(AuctionView.as_view()), name='auctions-list'),
    path('auctions/<int:id>/', AuctionDetailedView.as_view(), name='auction-details'),
    path('bets/', BetView.as_view(), name='bets-list'),
]
