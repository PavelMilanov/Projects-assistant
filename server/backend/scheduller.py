from apscheduler.schedulers.background import BackgroundScheduler
from .logging import logger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


scheduler = BackgroundScheduler()

def job_listener(event):
    try:
        logger.info(f'{event} выполнен')
    except Exception as e:
        logger.error(f'{event} не выполнен')

scheduler.start()
scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)