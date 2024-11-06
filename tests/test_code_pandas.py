from unittest.mock import Mock, mock_open, patch

import pytest

from src.pandas_func import read_transaction, read_transaction_xls


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="141605;CANCELED;2023-10-07T19:46:26Z;33915;Yuan Renminbi;CNY;Discover 6442824834772713;"
              "American Express 1908030991731165;Перевод с карты на карту",
)
def test_read_transaction(mock_file):
    transactions = read_transaction("data/operations.json")
    assert transactions == [
        {
            "id": "141605",
            "state": "CANCELED",
            "date": "2023-10-07T19:46:26Z",
            "amount": "33915",
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Discover 6442824834772713",
            "to": "American Express 1908030991731165",
            "description": "Перевод с карты на карту",
        }
    ]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_transaction_null(mock_file):
    transactions = read_transaction("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data="None")
def test_read_transaction_none(mock_file):
    transactions = read_transaction("data/operations.json")
    assert transactions == [
        {
            "amount": None,
            "currency_code": None,
            "currency_name": None,
            "date": None,
            "description": None,
            "from": None,
            "id": "None",
            "state": None,
            "to": None,
        }
    ]


@pytest.fixture
def exit_data():
    return [
        {"id": {0: "650703"}},
        {"state": {0: "EXECUTED"}},
        {"amount": {0: 16210}},
        {"currency_name": {0: "Sol"}},
        {"from": {0: "Счет 58803664561298323391"}},
        {"to": {0: "Счет 39745660563456619397"}},
        {"description": {0: "Перевод организации"}},
    ]


@patch("pandas.read_excel")
def test_read_transaction_xls(mock_read_excel, exit_data):
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = exit_data
    mock_read_excel.return_value = mock_dataframe
    assert read_transaction_xls("../data/transactions2.xlsx") == exit_data


@patch("pandas.read_excel")
def test_read_transaction_xls_null(mock_read_excel):
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = []
    mock_read_excel.return_value = mock_dataframe
    assert read_transaction_xls("") == []
