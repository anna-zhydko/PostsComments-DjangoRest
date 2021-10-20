import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "posts_cmnts.settings")
app = Celery("posts_cmnts")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.timezone = "Europe/Kiev"


# The task "work_ua_insert" will be started at 11:40 every day
app.conf.beat_schedule = {
    "clear_db": {
        "task": "main.tasks.reset_upvotes",
        "schedule": crontab(hour=23, minute=23),
    }
}
