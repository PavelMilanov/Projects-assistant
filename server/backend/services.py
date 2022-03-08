import sys
import os

PATH = os.getcwd()
sys.path.append(PATH)

from trello_app.api import google_docs, trello_request 
from .scheduller import scheduler
from .database import Database


trello = trello_request.TrelloManager()
google_doc = google_docs.GoogleDocsManager()

@scheduler.scheduled_job('cron', day_of_week='mon', hour='20',id='2')  # noqa E501
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
        text1, text2)
    lists = google_doc.generate_paragraph_bullets()
    header = google_doc.generate_header()
    style = google_doc.generate_styles()
    google_doc.write(header, request, lists, style)
 
@scheduler.scheduled_job('cron', day_of_week='mon', hour='9', id='3')  # noqa E501
def clear_doc():
    google_doc.clear()

@scheduler.scheduled_job('cron', day_of_week='tue', hour='15', id='4')  # noqa E501
def download_doc():
    Database.delete_file()
    file = google_doc.download_document()
    # file = 'отчет 2022-01-13.docx'
    name = file.split(' ')[0]
    Database.insert_files(
        {'name': file,
         'marker': name})
    
@scheduler.scheduled_job('cron', day_of_week='tue', hour='14', id='1')  # noqa E501
def archive_cards():
    trello.archive_done_cards()

@scheduler.scheduled_job('cron', day_of_week='tue', hour='15', minute='2', id='5')  # noqa E501
def upload_document_to_folder():
    filename = Database.find_file({
        'marker': 'отчет'
    })
    google_doc.upload_document_to_google_drive_folder(filename['name'])
    Database.delete_file()
