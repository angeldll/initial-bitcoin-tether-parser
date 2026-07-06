import requests
import json

def fetch_rate():
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,tether,ethereum&vs_currencies=usd,eur,rub"
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

def load_rate(file_name='rate.json'):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Файл не найден! Создаю новый словарь...")
        data = {}
        return data

def old_rate():
    old = load_rate()
    if old != {}:
        print(f"КУРС BITCOIN К ДОЛЛАРУ -> {old['bitcoin']['usd']} USD")
        print(f"КУРС BITCOIN К ЕВРО -> {old['bitcoin']['eur']} EUR")
        print(f"КУРС BITCOIN К РУБЛЮ -> {old['bitcoin']['rub']} RUB")
        print(f"КУРС USDT К ДОЛЛАРУ -> {old['tether']['usd']} USD")

        print("=========================================")

        print(f"КУРС ETHEREUM К ДОЛЛАРУ -> {old['ethereum']['usd']} USD")
        print(f"КУРС ETHEREUM К ЕВРО -> {old['ethereum']['eur']} EUR")
        print(f"КУРС ETHEREUM К РУБЛЮ -> {old['ethereum']['rub']} RUB")
    else:
        print("Данные не найдены!")



response = fetch_rate()
data = response.json()
if response.status_code == 200:
    if data != {}:
        print(f"КУРС BITCOIN К ДОЛЛАРУ -> {data['bitcoin']['usd']} USD")
        print(f"КУРС BITCOIN К ЕВРО -> {data['bitcoin']['eur']} EUR")
        print(f"КУРС BITCOIN К РУБЛЮ -> {data['bitcoin']['rub']} RUB")
        print(f"КУРС USDT К ДОЛЛАРУ -> {data['tether']['usd']} USD")

        print("======================================")

        print(f"КУРС ETHEREUM К ДОЛЛАРУ -> {data['ethereum']['usd']} USD")
        print(f"КУРС ETHEREUM К ЕВРО -> {data['ethereum']['eur']} EUR")
        print(f"КУРС ETHEREUM К РУБЛЮ -> {data['ethereum']['rub']} RUB")

        save_rate(data)
        print("Сохранено!")

    else:
        old_rate()

else:
    print("Ошибка подключения!")
    exit()


