import requests
import sys

# Substitua 'SEU_KEY' e 'SEU_TOKEN' pelos valores reais obtidos na sua conta do Trello
TRELLO_API_KEY = ''
TRELLO_TOKEN = ''
BOARD_ID = ''

def get_trello_cards():
    # URL da API do Trello para obter as listas do quadro
    url = f'https://api.trello.com/1/boards/{BOARD_ID}/lists'

    # Parâmetros da consulta
    params = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
    }

    # Fazendo a chamada à API do Trello para obter as listas
    response = requests.get(url, params=params)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code != 200:
        print(f'Erro na solicitação: {response.status_code}')
        sys.exit()

    try:
        # Tentar converter a resposta para JSON
        lists = response.json()
    except requests.exceptions.JSONDecodeError:
        print('Erro ao decodificar a resposta JSON.')
        sys.exit()

    # Iterando sobre as listas do quadro
    for trello_list in lists:
        list_id = trello_list['id']
        list_name = trello_list['name']

        # URL da API do Trello para obter os cartões da lista
        cards_url = f'https://api.trello.com/1/lists/{list_id}/cards'

        # Fazendo a chamada à API do Trello para obter os cartões
        cards_response = requests.get(cards_url, params=params)

        # Verificar se a solicitação foi bem-sucedida
        if cards_response.status_code != 200:
            print(f'Erro na solicitação de cartões: {cards_response.status_code}')
            sys.exit()

        try:
            # Tentar converter a resposta dos cartões para JSON
            cards = cards_response.json()
        except requests.exceptions.JSONDecodeError:
            print('Erro ao decodificar a resposta JSON dos cartões.')
            sys.exit()

        print(cards)

    print('Operação concluída com sucesso.')

# Chamar a função para obter os cartões
get_trello_cards()
