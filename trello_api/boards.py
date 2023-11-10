from dotenv import load_dotenv
import os
import requests
load_dotenv()

__trello_key = os.getenv('TRELLO_API_KEY')
__trello_token = os.getenv('TRELLO_API_TOKEN')

def create_board(name:str,cards) -> str:
    TRELLO_URL = 'https://api.trello.com/1/boards/'
    REQUEST_METHOD = 'POST'

    query = {
        'name': f'{name}',
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'       
    }

    response = requests.request(
        REQUEST_METHOD,
        TRELLO_URL,
        params=query
    )

def __add_cards_on_board(board_code,cards):
    pass



        