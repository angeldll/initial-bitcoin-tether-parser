import requests
import json

def fetch_rate():
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,tether&vs_currencies=usd,eur,rub"
    try:
        response = requests.get(URL)
        return response
    except requests.exceptions.ConnectionError:
        print("Нет соединения с API!")
        response = {}
        return response


def save_rate(data):
    with open("rate.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print("Сохранено!")

def load_rate(file_name='rate.json'):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Файл не найден! Создаю новый словарь...")
        data = {}
        return data

response = fetch_rate()
data = response.json()
if response.status_code == 200:
    if data != {}:
        print(f"КУРС BITCOIN К ДОЛЛАРУ -> {data['bitcoin']['usd']} USD")
        print(f"КУРС BITCOIN К ЕВРО -> {data['bitcoin']['eur']} EUR")
        print(f"КУРС BITCOIN К РУБЛЮ -> {data['bitcoin']['rub']} RUB")
        print(f"КУРС USDT К ДОЛЛАРУ -> {data['tether']['usd']} USD")
        save_rate(data)
    else:
        old = load_rate()
        if old != {}:
            print(f"КУРС BITCOIN К ДОЛЛАРУ -> {old['bitcoin']['usd']} USD")
            print(f"КУРС BITCOIN К ЕВРО -> {old['bitcoin']['eur']} EUR")
            print(f"КУРС BITCOIN К РУБЛЮ -> {old['bitcoin']['rub']} RUB")
            print(f"КУРС USDT К ДОЛЛАРУ -> {old['tether']['usd']} USD")
        else:
            print("Данные не найдены!")

else:
    print("Ошибка подключения!")
    exit()


