import json
import os

from src.external_api import convert_currency


def get_json_data(filename):
    """считывает json данные их стороннего файла и преобразовывает их в пайтон объект"""
    path_to_file = os.path.join(os.path.dirname(__file__)[:-3], "data", filename)
    try:
        with open(path_to_file, encoding="utf-8") as file:
            data_list = json.load(file)
            if type(data_list) == list:
                return data_list
            else:
                return []
    except Exception:
        return []


def result_transactions(data):
    """возвращает сумму сделки согласно данным транзакций"""
    if data["operationAmount"]["currency"]["code"] in ["EUR", "USD"]:
        return convert_currency(data["operationAmount"]["currency"]["code"], float(data["operationAmount"]["amount"]))
    else:
        return float(data["operationAmount"]["amount"])
