from typing import List

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .models import Auction


@shared_task(ignore_result=True, bind=True)
def async_send_email(self, email_list: List[str], subject: str, message: str):
    """Send email to specified recipients list"""
    send_mail(
        subject,
        message,
        from_email=settings.EMAIL_NO_REPLY,
        recipient_list=email_list,
        fail_silently=False
    )


@shared_task(ignore_result=True, bind=True)
def actualize_auction_status(self):
    """Close outdated auctions"""
    for auction in Auction.objects.filter(is_active=True):
        if auction.end_time <= timezone.now():
            last_bet = auction.bets.last()
            if last_bet:
                auction.winner = last_bet.created_by

            auction.is_active = False
            auction.save()

            if auction.winner:
                send_mail('Congratulations!', f'You won the auction #{auction.id}',
                          from_email=settings.EMAIL_NO_REPLY,
                          recipient_list=[auction.winner.email, ],
                          fail_silently=False)
