import sys
import os

PATH = os.getcwd()

sys.path.append(PATH)

from trello_app.api import google_docs, trello_request 
from .scheduller import scheduler
from .database import Database

trello = trello_request.TrelloManager()
google_doc = google_docs.GoogleDocsManager()

@scheduler.scheduled_job('cron', day_of_week='mon',
                          hour='18',id='2')
def generate_doc():
    text1 = google_doc._generate_tasks_for_document(
        trello.get_done_cards())
    text2 = google_doc._generate_tasks_for_document(
        trello.get_testing_prod_cards())
    text3 = google_doc._generate_tasks_for_document(
        trello.get_deploing_prod_cards())
    text4 = google_doc._generate_tasks_for_document(
        trello.get_testing_dev_cards())
    request = google_doc.generate_text(
        text1, text2, text3, text4)
    lists = google_doc.generate_paragraph_bullets()
    style = google_doc.generate_styles()
    google_doc.write(request, lists, style)
 
@scheduler.scheduled_job('cron', day_of_week='mon',
                        hour='9', id='3')
def clear_doc():
    google_doc.clear()

@scheduler.scheduled_job('cron', day_of_week='tue',
                         hour='15', id='4')
def download_doc():
    filename = google_doc.download_document()
    Database.insert_files({'name': filename})
    

@scheduler.scheduled_job('cron', day_of_week='tue',
                          hour='14', id='1')
def archive_cards():
    trello.archive_done_cards()

@scheduler.scheduled_job('cron', day_of_week='tue',
                         hour='15', minute='2', id='5')
def upload_document_to_folder():
    filename = Database.find_all_files()
    google_doc.upload_document_to_google_drive_folder(filename[0]['name'])
    Database.delete_file(filename[0]['name'])
