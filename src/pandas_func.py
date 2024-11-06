import csv

import pandas as pd


def read_transaction(path):
    with open(path, encoding="utf-8") as file:
        fieldnames = ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        reader = csv.DictReader(file, delimiter=";", fieldnames=fieldnames)
        list_dict = []
        for row in reader:
            list_dict.append(row)
        return list_dict


def read_transaction_xls(path):
    """считывает данные из файла excel и возвращает их списком словаре питон"""
    df = pd.read_excel(path)
    list_dict = df.to_dict()
    return list_dict
