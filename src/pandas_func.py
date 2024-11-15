import csv

import pandas as pd


def read_transaction_csv(path='../data/transactions.csv'):
    with open(path, encoding="utf-8") as file:
        fieldnames = ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        reader = csv.DictReader(file, delimiter=";", fieldnames=fieldnames)
        list_dict = []
        for row in reader:
            list_dict.append(row)
        return list_dict


def read_transaction_xls(path='../data/transactions_excel.xlsx'):
    """считывает данные из файла excel и возвращает их списком словаре питон"""
    df = pd.read_excel(path)
    list_dict = df.to_dict(orient='records')
    return list_dict
