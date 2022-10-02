
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api

def start():
    print("jobs.updater.jobs")
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_api, 'cron', second=10)
    scheduler.start()