from src.re_collections_random import count_transactions, search_string


def test_search_string_1():
    assert search_string(
        [
            {
                "date": "2019-08-26T10:50:58.294041",
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "id": 441945886,
                "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
                "state": "EXECUTED",
                "to": "Счет 64686473678894779589",
            },
            {
                "date": "2019-07-03T18:35:29.512364",
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "id": 41428829,
                "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 35383033474447895560",
            },
            {
                "date": "2018-06-30T02:08:58.425572",
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "id": 939719570,
                "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 11776614605963066702",
            },
            {
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "id": 142264268,
                "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 75651667383060284188",
            },
            {
                "date": "2019-03-23T01:09:46.296404",
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "id": 873106923,
                "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
                "state": "EXECUTED",
                "to": "Счет 74489636417521191160",
            },
        ],
        "Перевод",
    ) == [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        },
        {
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "id": 41428829,
            "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 35383033474447895560",
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_search_string_2():
    assert (
        search_string(
            [
                {
                    "date": "2019-08-26T10:50:58.294041",
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "id": 441945886,
                    "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "date": "2019-07-03T18:35:29.512364",
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "id": 41428829,
                    "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 35383033474447895560",
                },
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "date": "2019-04-04T23:20:05.206878",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "id": 142264268,
                    "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "date": "2019-03-23T01:09:46.296404",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "id": 873106923,
                    "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 74489636417521191160",
                },
            ],
            "1",
        )
        == []
    )


def test_count_transactions_1():
    assert count_transactions(
        [
            {
                "date": "2019-08-26T10:50:58.294041",
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "id": 441945886,
                "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
                "state": "EXECUTED",
                "to": "Счет 64686473678894779589",
            },
            {
                "date": "2019-07-03T18:35:29.512364",
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "id": 41428829,
                "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 35383033474447895560",
            },
            {
                "date": "2018-06-30T02:08:58.425572",
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "id": 939719570,
                "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 11776614605963066702",
            },
            {
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "id": 142264268,
                "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 75651667383060284188",
            },
            {
                "date": "2019-03-23T01:09:46.296404",
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "id": 873106923,
                "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
                "state": "EXECUTED",
                "to": "Счет 74489636417521191160",
            },
        ],
        ["Перевод организации", "Открытие вклада", "Перевод со счета на счет"],
    ) == {"Перевод организации": 3, "Перевод со счета на счет": 2}


def test_count_transactions_2():
    assert count_transactions([], ["Перевод организации", "Открытие вклада", "Перевод со счета на счет"]) == {}


def test_count_transactions_3():
    assert (
        count_transactions(
            [
                {
                    "date": "2019-08-26T10:50:58.294041",
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "id": 441945886,
                    "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "date": "2019-07-03T18:35:29.512364",
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "id": 41428829,
                    "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 35383033474447895560",
                },
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "date": "2019-04-04T23:20:05.206878",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "id": 142264268,
                    "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "date": "2019-03-23T01:09:46.296404",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "id": 873106923,
                    "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 74489636417521191160",
                },
            ],
            [
                "Открытие вклада",
            ],
        )
        == {}
    )


def test_count_transactions_4():
    assert (
        count_transactions(
            [
                {
                    "date": "2019-08-26T10:50:58.294041",
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "id": 441945886,
                    "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "date": "2019-07-03T18:35:29.512364",
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "id": 41428829,
                    "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 35383033474447895560",
                },
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "date": "2019-04-04T23:20:05.206878",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "id": 142264268,
                    "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "date": "2019-03-23T01:09:46.296404",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "id": 873106923,
                    "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 74489636417521191160",
                },
            ],
            123,
        )
        == []
    )
