import requests
import json


url= "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,tether&vs_currencies=usd,eur,rub"
response = requests.get(url)

def save_rate(data):
    with open("rate.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print("Сохранено!")

if response.status_code == 200:
    data = response.json()
    print(f"КУРС BITCOIN К ДОЛЛАРУ -> {data['bitcoin']['usd']} USD")
    print(f"КУРС BITCOIN К ЕВРО -> {data['bitcoin']['eur']} EUR")
    print(f"КУРС BITCOIN К РУБЛЮ -> {data['bitcoin']['rub']} RUB")
    print(f"КУРС USDT К ДОЛЛАРУ -> {data['tether']['usd']} USD")
    save_rate(data)
else:
    print("Ошибка подключения!")
    exit()


