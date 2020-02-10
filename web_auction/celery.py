"""
run redis in docker:
sudo docker run --rm --name=redis-devel --publish=6379:6379 --hostname=redis redis:latest

celery -A web_auction worker -l info
"""
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_auction.settings')

app = Celery('sml')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'actualize-auction-status': {
        'task': 'auction.tasks.actualize_auction_status',
        'schedule': crontab(minute='*/1')
    }
}
