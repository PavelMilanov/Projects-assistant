import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from __init__ import env


class GoogleDriveAssistant:
    
    service = None
     
    def __init__(self):
        env.read_env()
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            env('CREDENTIALS_FILE'),
            env.list('SCOPES'))
        httpAuth = credentials.authorize(httplib2.Http())
        self.service = build('docs', 'v1', http=httpAuth)

    def write_heading(self):
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

    def write_document(self,requests):
        self.service.documents().batchUpdate(
            documentId=env('DOCUMENT_ID'), body={'requests': requests}
        ).execute()

if __name__ == '__main__':
    assistant = GoogleDriveAssistant()
    assistant.write_document(assistant.write_heading()) 
