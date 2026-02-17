import requests


def get_card_by_coord_and_size(lan, lot, z):
    api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    url = "https://static-maps.yandex.ru/v1?"
    params = {
        "apikey": api_key,
        "ll": f'{lan},{lot}',
        "z": z
    }
    response = requests.get(url, params=params)
    if response:
        return response
    else:
        print("Ошибка выполнения запроса:")
        print(url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None