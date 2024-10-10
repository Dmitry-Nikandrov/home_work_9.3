def filter_by_currency(list_data, currency):
    """отбирает информацию о транзакциях по указанной валюте"""
    return (i for i in list_data if i["operationAmount"]["currency"]["name"] == currency)


def transaction_descriptions(list_data):
    """отображает описание каждой банковско операции в указанном массиве"""
    for i in list_data:
        yield i["description"]


def card_number_generator(a, b):
    """отображает номер карты по установленному формату по всем значениях итерируемого диапозона"""
    card_numbers = map(lambda x: ((20 - len(str(x))) * "0" + str(x)), range(a, b + 1))

    return map(lambda x: " ".join([x[i : i + 4] for i in range(len(x)) if (i) % 4 == 0]), card_numbers)
