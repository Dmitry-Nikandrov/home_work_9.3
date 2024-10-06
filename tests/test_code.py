import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


@pytest.fixture
def card_number_small():
    return "1234567890167890"


@pytest.fixture
def bill_with_letter():
    return "123456789016789a"


@pytest.fixture
def card_number_long():
    return "123456789016789012334"


@pytest.fixture
def card_number_zero():
    return "0"


@pytest.fixture
def card_number():
    return "59872364587512369547"


def test_get_mask_card_number(card_number, card_number_small, bill_with_letter, card_number_long, card_number_zero):
    assert get_mask_card_number(card_number) == "5987 23** **** **** 9547"
    assert get_mask_card_number(card_number_small) == "1234 56** **** 7890"
    assert get_mask_card_number(bill_with_letter) == "присутствие нечисловых символов"
    assert get_mask_card_number(card_number_zero) == "00"
    assert get_mask_card_number(card_number_long) == "слишком длинный номер карты"


@pytest.fixture
def bill_long():
    return "5987236458751236954712"


def test_get_mask_account(card_number_small, bill_long):
    assert get_mask_account(card_number_small) == "**7890"
    assert get_mask_account(bill_long) == "число цифр в счете больше 20"
    assert get_mask_account("12345678901678877901") == "**7901"


@pytest.fixture
def date_normal():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date_with_letters():
    return "2025-03-132T02:26****"


def test_get_date(date_normal, date_with_letters):
    assert get_date(date_normal) == "11-03-2024"
    assert get_date(date_with_letters) == "13-03-2025"
    assert get_date("0") == "0"
    assert get_date(None) == "0"
    assert get_date("25-03-13") == ("недопустимая длина строки")


@pytest.fixture
def card_visa():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def card_maestro():
    return "Maestro 1596837868705199"


@pytest.fixture
def account():
    return "Счет 64686473678894779589"


def test_mask_account_card_2(card_visa, card_maestro, account):
    assert mask_account_card(card_visa) == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(account) == "Счет **9589"
    assert mask_account_card(card_maestro) == "Maestro 1596 83** **** 5199"
    assert mask_account_card("0") == "данные отсутствуют или заданы неправильно"
    assert mask_account_card(None) == "данные отсутствуют или заданы неправильно"


@pytest.mark.parametrize(
    "card_info, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_1(card_info, expected_result):
    assert mask_account_card(card_info) == expected_result


@pytest.mark.parametrize(
    "list_data, state, expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED"},
                {"id": 939719570, "state": "EXECUTED"},
                {"id": 145873269, "state": "CANCELED"},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED"}, {"id": 939719570, "state": "EXECUTED"}],
        ),
        (
            [{"id": 41428829, "state": "None"}, {"id": 939719570}, {"id": 145873269, "state": "EXECUTED"}],
            "EXECUTED",
            [{"id": 145873269, "state": "EXECUTED"}],
        ),
        (
            [{"id": 41428829, "state": "None"}, {"id": 939719570}, {"id": 145873269, "state": "EXECUTED"}],
            "CANCELED",
            [],
        ),
        (
            [{"id": 41428871, "state": "EXECUTED"}, {"id": 939719570}, {"id": 145873269, "state": "CANCELED"}],
            "CANCELED",
            [{"id": 145873269, "state": "CANCELED"}],
        ),
        ([], None, []),
    ],
)
def test_filter_by_state(list_data, state, expected_result):
    assert filter_by_state(list_data, state) == expected_result


@pytest.fixture
def data_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def data_equal():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def data_incorrect():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": None},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_sort_by_date(data_list, data_equal, data_incorrect):
    assert sort_by_date(data_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(data_equal) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    assert sort_by_date(data_incorrect) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": None},
    ]
