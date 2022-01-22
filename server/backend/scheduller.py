from apscheduler.schedulers.background import BackgroundScheduler
from .logging import logger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


scheduler = BackgroundScheduler()

def job_listener(event):
    if event.exception:
        logger.error(f'{event.exception}')
    else:
        logger.info(f'задача выполнена')

scheduler.start()
scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)