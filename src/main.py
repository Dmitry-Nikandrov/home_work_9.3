from locale import currency

from src.utils import get_json_data
from src.widget import get_date,mask_account_card
from src.pandas_func import read_transaction_csv, read_transaction_xls
from src.processing import filter_by_state, sort_by_date
from generators import filter_by_currency_json,filter_by_currency_csv_excel
from src.re_collections_random import search_string,count_transactions

'словарь возвращает необходимые действия с входными файлами в зависимости от выбранного пользователем варианта'
dict_actions = [{1: {'Для обработки выбран JSON-файл.':get_json_data()}},
                {2: {'Для обработки выбран CSV-файл.':read_transaction_csv()}},
                {3: {'Для обработки выбран Excel-файл.':read_transaction_xls()}}]

def main():
    transactions =[]
    choic = int(input('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n'''))

    for i in dict_actions:
        for number,value in i.items():
            if number==choic:
                for legend,func in value.items():
                    print(legend)
                    transactions = func

    while True:
        answer_filter = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''')
        if answer_filter.upper() not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Статус операции "{answer_filter}" недоступен.')
        else:
            transactions = filter_by_state(transactions)
            break

    answer_sort = input('''Отсортировать операции по дате? Да/Нет\n''')
    if answer_sort.lower() =='да':
        answer_sort_upper = input('Отсортировать по возрастанию или по убыванию?\n')
        if answer_sort_upper.lower() == 'по возрастанию':
            transactions=sort_by_date(transactions,rev=False)
        else:
            transactions = sort_by_date(transactions,rev=True)

    answer_rub = input('''Выводить только рублевые транзакции? Да/Нет\n''')
    if answer_rub.lower() == 'да':
        if choic == 1:
            transactions = list(filter_by_currency_json(transactions, currency="руб."))
        else:
            transactions = list(filter_by_currency_csv_excel(transactions, currency='RUB'))

    answer_discript = input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n''')
    if answer_discript.lower() == 'да':
        key_answer = input('''Введите слово для отбора транзакций\n''')
        transactions = search_string(transactions,key_answer)
    #print(transactions)

    print('Программа: Распечатываю итоговый список транзакций...\n')
    print(f'Всего банковских операций в выборке: {len(transactions)}\n')

    if not transactions:
        return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'
    else:
        for transaction in transactions:
            print(get_date(transaction['date']), transaction['description'])
            if transaction['description'] == 'Открытие вклада':
                print(mask_account_card(transaction['to']))
            else:
                print(mask_account_card(transaction['from']),' -> ',mask_account_card(transaction['to']))
            if choic ==1:
                print(f'Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']}\n')
            else:
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')
        return 'Завершение программы'
print(main())