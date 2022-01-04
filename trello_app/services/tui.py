from api.trello_request import TrelloManager
from api.google_docs import GoogleDocsManager


trello = TrelloManager()
google_doc = GoogleDocsManager()


class TUI:
    
    def _print_screen(self):
        screen = """
    Docs Manager v0.1
    
        Меню:

1. Заархивировать карточки;
2. Составить отчет;
3. Очистить документ;

"""
        print(screen)
    
    def run(self):
        try:
            while True:
                self._print_screen()
                menu_value = input(": ")
                if menu_value == '1':
                    trello.archive_done_cards()
                elif menu_value == '2':
                    paragraph1 = google_doc._generate_header()
                    paragraph2 = google_doc._generate_tasks_for_document(trello.get_done_cards())
                    paragraph3 = google_doc._generate_paragraph3()
                    paragraph4 = google_doc._generate_tasks_for_document(trello.get_testing_prod_cards())
                    style = google_doc._generate_styles()
                    request = paragraph1 + paragraph2 + paragraph3 + paragraph4 + style
                    google_doc.write(request)
                elif menu_value == '3':
                    google_doc.clear()
                    
        except KeyboardInterrupt:
            pass
            