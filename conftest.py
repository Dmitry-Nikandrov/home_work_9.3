import pytest


@pytest.fixture
def card_number_small():
    return '1234567890167890'

@pytest.fixture
def bill_with_letter ():
    return '123456789016789a'

@pytest.fixture
def card_number_long ():
    return '123456789016789012334'

@pytest.fixture
def card_number_zero ():
    return '0'
@pytest.fixture
def card_number ():
    return '59872364587512369547'

@pytest.fixture
def bill_long ():
    return '5987236458751236954712'

@pytest.fixture
def date_normal ():
    return '2024-03-11T02:26:18.671407'

@pytest.fixture
def date_with_letters ():
    return '2025-03-132T02:26****'

@pytest.fixture
def card_visa():
    return 'Visa Platinum 7000792289606361'

@pytest.fixture
def card_maestro():
    return 'Maestro 1596837868705199'

@pytest.fixture
def account():
    return 'Счет 64686473678894779589'

@pytest.fixture
def data_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def data_equal():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]

@pytest.fixture
def data_incorrect():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': None},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]




