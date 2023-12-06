import requests
import csv

# Substitua 'SEU_KEY', 'SEU_TOKEN' e 'SEU_BOARD_ID' pelos valores reais obtidos na sua conta do Trello
TRELLO_API_KEY = ''
TRELLO_TOKEN = ''
BOARD_ID = ''

# URL da API do Trello para obter as listas do board
# URL da API do Trello para obter as listas do board
url_lists = f'https://api.trello.com/1/boards/{BOARD_ID}/lists'

# Parâmetros da consulta para obter as listas
params_lists = {
    'key': TRELLO_API_KEY,
    'token': TRELLO_TOKEN,
}

# Fazendo a chamada à API do Trello para obter as listas
response_lists = requests.get(url_lists, params=params_lists)

# Verificar se a solicitação foi bem-sucedida
if response_lists.status_code != 200:
    print(f'Erro na solicitação de listas: {response_lists.status_code}')
    print(response_lists.text)  # Exibir a resposta completa para diagnóstico
else:
    # Tentar converter a resposta para JSON
    lists = response_lists.json()

    # Abrir o arquivo CSV para escrita
    with open('dados_trello.csv', mode='w', newline='', encoding='utf-8') as file:
        # Criar um objeto CSV writer
        csv_writer = csv.writer(file)

        # Escrever o cabeçalho do CSV
        csv_writer.writerow(['Nome do Cartão', 'Descrição do Cartão', 'Data de Última Atividade'])

        # Iterando sobre as listas do board
        for trello_list in lists:
            list_id = trello_list['id']

            # URL da API do Trello para obter os cartões da lista
            url_cards = f'https://api.trello.com/1/lists/{list_id}/cards'

            # Parâmetros da consulta para obter os cartões da lista
            params_cards = {
                'key': TRELLO_API_KEY,
                'token': TRELLO_TOKEN,
            }

            # Fazendo a chamada à API do Trello para obter os cartões da lista
            response_cards = requests.get(url_cards, params=params_cards)

            # Verificar se a solicitação foi bem-sucedida
            if response_cards.status_code != 200:
                print(f'Erro na solicitação de cartões: {response_cards.status_code}')
                print(response_cards.text)  # Exibir a resposta completa para diagnóstico
            else:
                # Tentar converter a resposta para JSON
                cards = response_cards.json()

                # Iterando sobre os cartões e escrevendo no CSV
                for card in cards:
                    # Escrever os dados no CSV
                    csv_writer.writerow([card["name"], card["desc"], card["dateLastActivity"]])

                    # Imprimir informações na tela (opcional)
                    print(f'Nome do cartão: {card["name"]}')
                    print(f'Descrição do cartão: {card["desc"]}')
                    print(f'Data de última atividade do cartão: {card["dateLastActivity"]}')
                    print('-' * 30)

print("Dados salvos com sucesso no arquivo 'dados_trello.csv'")