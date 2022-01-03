import requests
from environs import Env


env = Env()
env.read_env()

class TrelloManager:
    """Requests for Trello API."""
            
    params = {
        'key': env('API_KEY'),
        'token': env('API_TOKEN')
    }
    done_prod = env('DONE_PROD')
    testing_prod = env('TESTING_PROD')
    testing_dev = env('TESTING_DEV')
    
    def get_done_cards(self) -> list:
        """Get cards for Done PROD 🎉 list."""
        r = requests.get(
            f'https://trello.com/1/lists/{self.done_prod}/cards?',
            params=self.params
        )
        data = r.json()
        return data
    
    def get_testing_prod_cards(self) -> list:
        """Get cards for Testing PROD list"""
        r = requests.get(
            f'https://trello.com/1/lists/{self.testing_prod}/cards?',
            params=self.params
        )
        data = r.json()
        return data
    
    def get_testing_dev_cards(self) -> list:
        """Get cards for Testing DEV list"""
        r = requests.get(
            f'https://trello.com/1/lists/{self.testing_dev}/cards?',
            params=self.params
        )
        data = r.json()
        return data        

    def archive_done_cards(self):
        """Archive all cards for Done PROD 🎉."""
        r = requests.post(
            f'https://api.trello.com/1/lists/{self.done_prod}/archiveAllCards',
            data=self.params
        )
        if r.status_code == '200':
            print(r.status_code)
        else:
            print(r.status_code)
