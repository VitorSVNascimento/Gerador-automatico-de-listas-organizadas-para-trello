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
        __add_card_on_list(card,to_do_list_code,cards)

    pass

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

def __add_card_on_list(card,list_id,card_list):
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    name = card['nome']
    description = card['descricao']
    prerequisites = card['pre_requisitos']
    priority = card['prioridade']
    query = {
        'idList': list_id,
        'name':name,
        'desc':description,
        'pos':'bottom',
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'
    }

    new_card = call_trello_api(url,query,POST_METHOD,headers)
    new_card_json = json.loads(new_card.text)
    if len(prerequisites) > 0:
        __create_prerequisites_list( new_card_json['id'],__get_prerequisites_names(card_list,prerequisites))
    __add_label_on_card(new_card_json['id'],priority)
    return new_card

def __get_prerequisites_names(cards,prerequisites_codes):
    prerequisites_name = [cards[int(code) -1]['nome'] for code in prerequisites_codes]
    return prerequisites_name

def __create_prerequisites_list(card_id,pre_requisites_names):
    url = "https://api.trello.com/1/checklists"
    print('cards_id == ',card_id)

    query = {
        'idCard': card_id,
        'name':'Pré requisitos',
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'
    }
    check_list = json.loads(call_trello_api(url,query,POST_METHOD).text)
    check_list_id = check_list['id']
    print('check_list_id == ',check_list_id)

    url = f"https://api.trello.com/1/checklists/{check_list_id}/checkItems"
    print(pre_requisites_names)
    for name in pre_requisites_names:
        query = {
            'name': f'{name}',
            'key': f'{__trello_key}',
            'token': f'{__trello_token}'
        }
        call_trello_api(url,query,POST_METHOD)

def __add_label_on_card(card_id,priority):
    url = f"https://api.trello.com/1/cards/{card_id}/labels"
    query = {
        'color': f'{labels[priority.lower()]}',
        'name' : f'Prioridade {priority.lower()}',
        'key': f'{__trello_key}',
        'token': f'{__trello_token}'
    }
    call_trello_api(url,query,POST_METHOD)

def call_trello_api(url,query,method,headers={}):
    
    response = requests.request(method,url,params=query) if headers == {} else requests.request(method,url,headers=headers,params=query)
    print(response.text) 
    return response

        