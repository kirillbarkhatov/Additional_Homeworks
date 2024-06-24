import requests
import json


def get_currency_rate(currency):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    result = {"currency_code": currency, "rate": data["Valute"][currency]["Value"]}
    return json.dumps(result, indent=4)


if __name__ == "__main__":
    rate = get_currency_rate("USD")
    print(rate)