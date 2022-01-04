import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from environs import Env


env = Env()
env.read_env()

# Authentification for Google API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    env('CREDENTIALS_FILE'),
    env.list('SCOPES'))
httpAuth = credentials.authorize(httplib2.Http())
service = build('docs', 'v1', http=httpAuth)
# 

def generate_doc(func):
    def wrapper(*args):
        request = func(*args)
        service.documents().batchUpdate(
            documentId=env('DOCUMENT_ID'), body={'requests': request}
        ).execute()
    return wrapper


class GoogleDocsManager:
    """Requests for Google-docs API."""
    
    paragraph1 = 'Отчет о выполненных задачах за неделю\nВыполнены:\n'
    paragraph2 = '\nВыполнены:\n'
    paragraph3 = 'Выполнены, но не проверены:\n'
    document_index = len(paragraph1) + len(paragraph2)+1
    
    def _generate_paragraph_bullets(self, start_idx, end_idx) -> dict:
        """Converts words on a new line to a list in a given range.

        Before:
            word1
            word2

        After:
            1. word1
            2. word2
        """
        
        return {
                    'createParagraphBullets': {
                        'range': {
                            'startIndex': start_idx,
                            'endIndex': end_idx
                        },
                        'bulletPreset': 'NUMBERED_DECIMAL_NESTED',
                    }
                }

    def _create_list_tasks(self, cards: list) -> list:
        """Get descriptions from Trello cards."""
        return [card['name'] for card in cards]
    
    def _generate_tasks_for_document(self, cards: list) -> list:
        """Generate response from card's descriptions."""
        first_index = self.document_index
        tasks = self._create_list_tasks(cards)
        response = []
        for item in tasks:
            template = {
                'insertText': {
                    'location': {
                        'index': self.document_index
                    },
                        'text': f'{item}\n'
                }
            }
            self.document_index += len(template['insertText']['text'])
            response.append(template)
        response.append(self._generate_paragraph_bullets(first_index, self.document_index))
        return response
    
    def _generate_header(self) -> list:
        """Generate paragraph1-2."""
        return [
                    {
                        'insertText': {
                            'location': {
                                'index': 1,
                            },
                            'text': self.paragraph1
                        }
                    },
                    # {
                    #     'insertText': {
                    #         'location': {
                    #             'index': len(self.paragraph1)
                    #         },
                    #         'text': self.paragraph2
                    #     }
                    # }
                ]
    
    def _generate_paragraph3(self) -> list:
        response = [
                    {
                        'insertText': {
                            'location': {
                                'index': self.document_index+1
                            },
                            'text': self.paragraph3
                        }
                    } 
                ]
        self.document_index += len(self.paragraph3)+1
        return response

        
    def _generate_styles(self):
        """Set style for text in document."""

        return [
                {
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': 1,
                            'endIndex':  len(self.paragraph1)
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
                                'endIndex': len(self.paragraph1)
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

    @generate_doc
    def clear(self) -> dict:
        """Clear document"""
        response = {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': self.document_index+1
                    }
                }
            }
        self.document_index = len(self.paragraph1) + len(self.paragraph2)+1
        return response

    @generate_doc
    def write(self, request) -> list:
        """Write text in document."""
        return request
