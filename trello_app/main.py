from api.trello_request import TrelloManager
from api.google_docs import GoogleDocsManager
from services.tui import TUI
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger


trello = TrelloManager()
scheduler = BackgroundScheduler()
google_doc = GoogleDocsManager()

logger.add('debug/logs.log', format='{time} {level} {message}', level='DEBUG', rotation="100 KB", compression="zip")
scheduler.start()


if __name__ == '__main__':
    
    app = TUI().run()
    # scheduler.add_job(trello.archive_done_cards, 'cron', day_of_week='tue', hour='14')
    # item1 = google_doc._generate_header()
    # item2 = google_doc._generate_tasks_for_document(trello.get_done_cards())
    # item3 = google_doc._generate_paragraph3()
    # item4 = google_doc._generate_tasks_for_document(trello.get_testing_prod_cards())
    # style = google_doc._generate_styles()
    # request = item1 + item2 + item3 + item4 + style
    # google_doc.write(request)
    # google_doc.clear()
    
