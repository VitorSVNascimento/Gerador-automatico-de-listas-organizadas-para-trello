from dotenv import load_dotenv
import os
import requests
import json

from trello_api.enums.visibility import Visibility
from trello_api.labels import labels
load_dotenv()

__trello_key = os.getenv('TRELLO_API_KEY')
__trello_token = os.getenv('TRELLO_API_TOKEN')
POST_METHOD = 'POST'
GET_METHOD = 'GET'
TO_DO_POSITION = 0

def create_board(name:str,cards) -> str:

    BOARDS_URL = 'https://api.trello.com/1/boards/'

    query = {
        'name': f'{name}',
        'prefs_permissionLevel': f'{Visibility.PUBLIC.value}',
        'defaultLabels' : 'false',
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'       
    }

    response = call_trello_api(BOARDS_URL,query,POST_METHOD)
    response_data = json.loads(response.text)

    board_code = response_data['id']
    short_url = response_data['shortUrl']
    # __add_labels_on_board(board_id)
    __add_cards_on_board(board_code,cards)
    return short_url

def __add_cards_on_board(board_code,cards):
    to_do_list_code = __get_to_do_list_id(board_code)
    print(f'to_do_code = {to_do_list_code}')
    for card in cards:
        __add_card_on_list(card,to_do_list_code)

    pass

def __add_card_on_list(card,list_id):
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    position = card['id']
    name = card['nome']
    query = {
        'idList': list_id,
        'name':name,
        'pos':'bottom',
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'
    }

    return call_trello_api(url,query,POST_METHOD,headers)

def __get_to_do_list_id(board_code):
    url = f"https://api.trello.com/1/boards/{board_code}/lists"
    headers = {
         "Accept": "application/json"
    }  
    query = {
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'
    }

    response = call_trello_api(url,query,GET_METHOD,headers)
    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data[TO_DO_POSITION]['id']
    return 'invalid request'

def __add_labels_on_board(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/labels"
    label_number = 0
    for key in labels.keys():
        print(f'chave = {key} e valor = {labels[key]}')
        # query = {
        #     'name': f'{key}',
        #     'color': f'{labels[key]}',
        #     'key': f'{__trello_key}',
        #     'token': f'{__trello_token}'
        # }

        # if call_trello_api(url,query,POST_METHOD).status_code == 200:
        #     label_number+=1
    return label_number

def call_trello_api(url,query,method,headers={}):
    
    response = requests.request(method,url,params=query) if headers == {} else requests.request(method,url,headers=headers,params=query)
    print(response.text) 
    return response

        