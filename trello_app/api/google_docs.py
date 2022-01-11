import io
import os
import httplib2
from datetime import datetime
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaIoBaseDownload
from environs import Env


env = Env()
env.read_env()

# Authentification for Google API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    env('CREDENTIALS_FILE'),
    env.list('SCOPES'))
httpAuth = credentials.authorize(httplib2.Http())
service = build('docs', 'v1', http=httpAuth)
drive_service = build('drive', 'v3', http=httpAuth)

def generate_doc(func):  # noqa D103
    def wrapper(*args):
        request = func(*args)
        service.documents().batchUpdate(
            documentId=env('DOCUMENT_ID'), body={'requests': request}
        ).execute()
    return wrapper


class GoogleDocsManager:
    """Requests for Google-docs API."""

    paragraph1 = 'Отчет о выполненных задачах за неделю'
    paragraph2 = 'Выполнены:\n'
    paragraph3 = 'Выполнены, но не проверены:\n'
    TEXT = f'{paragraph1}\n{paragraph2}'
    DEFAULT = TEXT
    document_index = len(TEXT)
    end_list1_index = 0
    start_list2_index = 0
    end_list2_index = 0

    def generate_paragraph_bullets(self) -> list:
        """Convert words on a new line to a list in a given range.

        Before:
            word1
            word2

        After:
            1. word1
            2. word2
        """
        return [
            {
                'createParagraphBullets': {
                    'range': {
                        'startIndex': len(self.DEFAULT) + 1,
                        'endIndex': self.end_list1_index
                    },
                    'bulletPreset': 'NUMBERED_DECIMAL_NESTED',
                }
            },
            {
                'createParagraphBullets': {
                    'range': {
                        'startIndex': self.start_list2_index + 1,
                        'endIndex': self.end_list2_index
                    },
                    'bulletPreset': 'NUMBERED_DECIMAL_NESTED',
                }
            }]

    def _create_list_tasks(self, cards: list) -> list:
        """Get descriptions from Trello cards."""
        return [card['name'] for card in cards]

    def _generate_tasks_for_document(self, cards: list) -> list:
        """Generate response from card's descriptions."""
        self.start_list_idx = self.document_index
        if len(cards) > 0:
            tasks = self._create_list_tasks(cards)
            text = ''
            for item in tasks:
                text += f'{item}\n'
            self.end_list_idx = self.start_list_idx + len(text)
            return text

    def generate_text(self, *text) -> list:
        """Generate paragraph1-2."""
        self.TEXT += text[0]  # карточки Done PROD
        self.end_list1_index = len(self.TEXT)
        self.TEXT += self.paragraph3
        self.start_list2_index = len(self.TEXT)
        try:
            self.TEXT += text[1]  # карточки Testing PROD
        except Exception:
            self.TEXT += ''
        try:
            self.TEXT += text[2]  # карточки Deploy PROD
        except Exception:
            self.TEXT += ''
        try:
            self.TEXT += text[3]  # карточки Testing DEV
        except Exception:
            self.TEXT += ''
        self.end_list2_index = len(self.TEXT)
        return [    
                {
                    'insertText': {
                        'location': {
                            'index': 1,
                        },
                        'text': self.TEXT
                    }
                }]

    def generate_styles(self):
        """Set style for text in document."""

        return [
            {
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': 1,
                        'endIndex':  len(self.paragraph1) + 1
                    },
                    'paragraphStyle': {
                        'namedStyleType': 'NORMAL_TEXT',
                        'alignment': 'CENTER'
                    },
                    'fields': 'namedStyleType, alignment'
                }
            },
            {
                'updateTextStyle': {
                        'range': {
                            'startIndex': 1,
                            'endIndex': len(self.paragraph1) + 1
                        },
                        'textStyle': {
                            'bold': True,
                            'weightedFontFamily': {
                            'fontFamily': 'Times New Roman'
                        },
                            'fontSize': {
                                'magnitude': 14,
                                'unit': 'PT'
                            }
                        },
                        'fields': '*'
                }
            }]
        
    def download_document(self):
        current_directory = f'{os.getcwd()}/archive/' # /archive/
        date = datetime.date(datetime.now())
        
        request = drive_service.files().export_media(fileId=env('DOCUMENT_ID'),
            mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        fh = io.FileIO(f'{current_directory}отчет {date}', 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            done = downloader.next_chunk()
        
    @generate_doc
    def clear(self) -> dict:
        """Clear document."""
        # запрос на последний индекс документа
        last_index = int(service.documents().get(
            documentId=env('DOCUMENT_ID')).execute()['body']['content'][-1]['endIndex'])  # noqa E501
        self.TEXT = self.DEFAULT
        self.end_list1_index = 0
        self.start_list2_index = 0
        self.end_list2_index = 0
        return {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': last_index - 1
                    }
                }}

    @generate_doc
    def write(self, *args) -> list:
        """Write text in document."""
        request = []
        for item in args:
            request += item
        return request
