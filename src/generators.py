list_data = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 978545569,
        "state": "EXECUTED",
        "date": "2020-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 789654123,
        "state": "EXECUTED",
        "date": "2023-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
]
def filter_by_currency(list_list_data, currency):
    return (i for i in list_list_data if i["operationAmount"]["currency"]["name"]==currency)

#print(filter_by_currency(list_data, "USD"))
usd_transactions = filter_by_currency(list_data, "USD")


def transaction_descriptions(list_data):
    for i in list_data:
        yield i['description']

tran=transaction_descriptions(list_data)
for i in range(len(list_data)):
    print (next(tran))

def card_number_generator(a,b):
    card_numbers = map(lambda x:((20-len(str(x)))*'0'+str(x)), range(a,b+1))

    return map(lambda x: ' '. join([x[i:i+4] for i in range(len(x)) if (i)%4==0]),card_numbers)

#for card_number in card_number_generator(1,100):
    #print (card_number)


