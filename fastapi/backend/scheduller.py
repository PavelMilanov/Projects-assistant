from apscheduler.schedulers.background import BackgroundScheduler
from .services import generate_doc, archive_cards, download_doc


scheduler = BackgroundScheduler()
scheduler.start()

def scheduler_init():
    
    scheduler.add_job(
        archive_cards,
        'cron',
        day_of_week='tue',
        hour='14', id='1',
        replace_existing=True)

    scheduler.add_job(
        generate_doc,
        'cron',
        day_of_week='mon',
        hour='20',id='2',
        replace_existing=True)
    
    scheduler.add_job(
        download_doc,
        'cron',
        day_of_week='tue',
        hour='13', minute='58', id='3',
        replace_existing=True)
