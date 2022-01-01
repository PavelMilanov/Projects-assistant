import requests
from environs import Env


env = Env()
env.read_env()


class TrelloRequest:
    """Request for Trello by Trello API."""
    
    params = {
        'key': env('API_KEY'),
        'token': env('API_TOKEN')
    }
    done_prod = env('DONE_PROD')


    def __init__(self):
        pass

    def get_done_cards(self):
        """Get cards for Done PROD 🎉 list."""
        r = requests.get(
            'https://trello.com/1/lists/5fde6c0e6837394e7ec3ea2d/cards?',
            params=self.params
        )
        print(r.text)
        return r.text
    
    def get_testing_prod_cards(self):
        """Get cards for Testing PROD list"""
        r = requests.get(
            'https://trello.com/1/lists/5fde8524864ca6204bd273e2/cards?',
            params=self.params
        )
        print(r.text)
        return r.text
    
    def get_testing_dev_cards(self):
        """Get cards for Testing DEV list"""
        r = requests.get(
            'https://trello.com/1/lists/5fde6c0e6837394e7ec3ea2c/cards?',
            params=self.params
        )
        print(r.text)
        return r.text        

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
