import os
from pathlib import Path
from typing import Any, Dict

import requests
from dotenv import load_dotenv

import src.utils
from src.utils import get_transactions
from src.сonfig import ROOT_PATH

# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")


def transaction_amount(transaction: Dict) -> float | Any:
    """функция, которая принимает транзакцию и возвращает сумму транзакции"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    result: Any = response.json()
    return result["result"]
