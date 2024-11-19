import json
import logging
import os

from src.external_api import convert_currency

# get_json_data_logger = logging.getLogger("get_json_data")
# get_json_data_handler = logging.FileHandler(filename="../logs/get_json_data.log", mode="w", encoding="utf-8")
# get_json_data_formatter = logging.Formatter(
#     "%(asctime)s - %(filename)s - %(funcName)s - %(name)s - %(levelname)s - %(message)s"
# )
# get_json_data_handler.setFormatter(get_json_data_formatter)
# get_json_data_logger.addHandler(get_json_data_handler)
# get_json_data_logger.setLevel(logging.DEBUG)
#
# result_transactions_logger = logging.getLogger("result_transactions")
# result_transactions_handler = logging.FileHandler(
#     filename="../logs/result_transactions.log", mode="w", encoding="utf-8"
# )
# result_transactions_formatter = logging.Formatter(
#     "%(asctime)s - %(filename)s - %(funcName)s - %(name)s - %(levelname)s - %(message)s"
# )
# result_transactions_handler.setFormatter(result_transactions_formatter)
# result_transactions_logger.addHandler(result_transactions_handler)
# result_transactions_logger.setLevel(logging.DEBUG)


def get_json_data(path="../data/operations.json"):
    """считывает json данные их стороннего файла и преобразовывает их в пайтон объект"""
    # path_to_file = os.path.join(os.path.dirname(__file__)[:-3], "data", filename)
    # get_json_data_logger.info(f"Получение динамической ссылки на json-файл:{path}")
    try:
        with open(path, encoding="utf-8") as file:
            data_list = json.load(file)
            # get_json_data_logger.info(f"Преобразование в объект python json-файла")
            if type(data_list) == list:
                # get_json_data_logger.info(f"Окончание преобразования json-файла в объект python")
                return data_list
            else:
                return []
    except Exception:
        # get_json_data_logger.error(f"ошибка преобразования json-файла в объект python")
        return []


# "Примеры логирования функции get_json_data с записью в соответствующем файле .log в папке logs"
# print(get_json_data("operations.json"))
# print(get_json_data("operationss.json"))


def result_transactions(data):
    """возвращает сумму сделки согласно данным транзакций"""
    if data["operationAmount"]["currency"]["code"] in ["EUR", "USD"]:
        # if (
            # type(
               # convert_currency(data["operationAmount"]["currency"]["code"], float(data["operationAmount"]["amount"]))
            # ) == list
        # ):
            #result_transactions_logger.info(f"""успешное завершение конвертации {data["operationAmount"]
        # ["currency"]["code"]} в рубли и возвращение рублевой суммы транзакции""")
        # else:
            # result_transactions_logger.info(f"""неудачная попытка конвертации {data
            # ["operationAmount"]["currency"]["code"]} в рубли """)
        return convert_currency(data["operationAmount"]["currency"]["code"], float(data["operationAmount"]["amount"]))
    else:
        # result_transactions_logger.info(f"""отображение рублевой суммы транзакции (исходный код валюты -
        # {data["operationAmount"]["currency"]["code"]}"""
        # )
        return float(data["operationAmount"]["amount"])


"Примеры логирования функции result_transactions с записью в соответствующем файле .log в папке logs"
# print(
#     result_transactions(
#         {
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Maestro 1596837868705199",
#             "to": "Счет 64686473678894779589",
#         }
#     )
# )
#
# print(
#     result_transactions(
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560",
#         }
#     )
# )
# print(
#     result_transactions(
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         }
#     )
# )
