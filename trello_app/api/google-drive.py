import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from environs import Env


env = Env()
env.read_env()


class GoogleDriveAssistant:
    
    service = None
    paragraph1 = 'Отчет о выполненных задачах с X по X\n'
    paragraph2 = 'Выполнены:\n'
    paragraph3 = 'Выполнены, но не проверены:\n'
    
     
    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            env('CREDENTIALS_FILE'),
            env.list('SCOPES'))
        httpAuth = credentials.authorize(httplib2.Http())
        self.service = build('docs', 'v1', http=httpAuth)

    def write(self):
        """Write text in document."""
        
        return [
                    {
                    'insertText': {
                        'location': {
                            'index': 1,
                        },
                        'text': self.paragraph1
                    }
                },
                    {
                        'insertText': {
                            'location': {
                                'index': len(self.paragraph1)+1
                            },
                        'text': self.paragraph2
                        }
                    },
                    {
                        'insertText': {
                            'location': {
                                'index': 40
                            },
                        'text': 'text1'
                        }
                    },
                
                    # {
                    #     'insertText': {
                    #         'location': {
                    #             'index': len(self.paragraph1)+len(self.paragraph2)+1
                    #         },
                    #     'text': self.paragraph3
                    #     }
                    # }  
            ]

    def styles(self):
        """Set style for text in document."""
        
        return [
                    {
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': 1,
                            'endIndex':  37
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
                                'endIndex': 37
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

    def clear(self):
        """Clear document"""
        
        return [
            {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': len(self.paragraph1)+len(self.paragraph2)+len(self.paragraph3)
                    }
                }
            }
        ]
        
 
    def write_document(self,requests):
        self.service.documents().batchUpdate(
            documentId=env('DOCUMENT_ID'), body={'requests': requests}
        ).execute()

if __name__ == '__main__':
    assistant = GoogleDriveAssistant()
    assistant.write_document(assistant.write())
    # assistant.write_document(assistant.clear())

    
