from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger


scheduler = BackgroundScheduler()

logger.add('debug/logs.log', format='{time} {level} {message}',
    level='DEBUG', rotation='100 KB',
    compression='zip')
scheduler.start()
# scheduler.add_job(trello.archive_done_cards, 'cron', day_of_week='tue', hour='14')


if __name__ == '__main__':

    pass
