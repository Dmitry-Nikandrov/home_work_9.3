import os
from typing import Any, Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_key = os.getenv("API_KEY")


def convert_currency(currency: str, ammount: Union[float, int]) -> Any:
    """динамически пересчитывает курс доллара или евро к рублю"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_key}
    payload = {"amount": ammount, "from": currency, "to": "RUB"}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        return f"Неудачная попытка входа, статус {response.status_code}"
