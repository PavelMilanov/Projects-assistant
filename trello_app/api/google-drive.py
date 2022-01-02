import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials




SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'token.json'
DOCUMENT_ID = '1UfCy_-HvZOhqs1tR3U68WRMzExw84XZNDadHtMEQ7Yc'


credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('docs', 'v1', http=httpAuth)

# Получаем содержимое документа
# document = service.documents().get(documentId=DOCUMENT_ID).execute()

def write_heading():
    return [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': 'Отчет о выполненных задачах с х по у'
                }
            }, 
            {
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': 1,
                        'endIndex':  39
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
                            'endIndex': 39
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
        }
        ]

def write_document(requests):
    service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': requests}
    ).execute()

write_document(write_heading())
