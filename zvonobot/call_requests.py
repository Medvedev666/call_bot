import requests
import json

from config.config import logger
from .request_body import get_data_dict

api_key = '#'

def make_call(apiKey, phone, gender,
        doctor, full_name, data_birth,
        insurance_name, insurance_number,
        comfort_date, my_phone, user_id
    ):
    url = 'https://lk.zvonobot.ru/apiCalls/create'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    data = get_data_dict(apiKey, phone, gender,
        doctor, full_name, data_birth,
        insurance_name, insurance_number,
        comfort_date, my_phone, user_id
    )

    try:
        response = requests.post(url, json=data, headers=headers)
    except Exception as e:
        logger.error(f'Error: {e}')

    logger.info('Start call')
    logger.info(response.text.encode('utf-8').decode('unicode-escape'))
    logger.info('Сделали')



def get_acc_info():
    # Формируем данные для запроса в виде словаря
    request_data = {
        'apiKey': api_key
    }

    # Преобразуем данные в JSON формат
    json_data = json.dumps(request_data)

    # URL для запроса к API Zvonobot
    url = 'https://lk.zvonobot.ru/apiCalls/userInfo'

    # Устанавливаем заголовки запроса
    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    # Отправляем POST запрос с использованием requests
    response = requests.post(url, headers=headers, data=json_data)

    # Печатаем ответ сервера
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Ошибка при выполнении запроса: {response.status_code}')


def get_api_call():
    url = 'https://lk.zvonobot.ru/apiCalls/get?apiCallIdList[]=1'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    payload = {
        'apiKey': api_key
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"


