import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Newspaper.settings")

app = Celery("Newspaper")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'weekly_digest': {
        'task': 'news.tasks.weekly_digest',
        'schedule': crontab(day_of_week='fri', hour='08', minute='00')
    }
}

