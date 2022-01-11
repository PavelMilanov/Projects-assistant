import sys
import os

PATH = os.getcwd()

sys.path.append(PATH)

from trello_app.api import google_docs, trello_request 


trello = trello_request.TrelloManager()
google_doc = google_docs.GoogleDocsManager()

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
 
def clear_doc():
    google_doc.clear()

def download_doc():
    google_doc.download_document()

def archive_cards():
    trello.archive_done_cards()
