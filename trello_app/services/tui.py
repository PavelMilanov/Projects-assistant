from api.trello_request import TrelloManager
from api.google_docs import GoogleDocsManager


trello = TrelloManager()
google_doc = GoogleDocsManager()


class TUI:
    """TUI for cosole."""

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
        """Start Application."""
        try:
            while True:
                self._print_screen()
                menu_value = input(': ')
                if menu_value == '1':
                    trello.archive_done_cards()
                elif menu_value == '2':
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
                    google_doc.write(request)
                    google_doc.write(lists)
                    google_doc.write(style)
                elif menu_value == '3':
                    google_doc.clear()

        except KeyboardInterrupt:
            pass
