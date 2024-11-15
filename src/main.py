from src.utils import get_json_data
from src.pandas_func import read_transaction_csv, read_transaction_xls
from src.processing import filter_by_state, sort_by_date
from generators import filter_by_currency_json,filter_by_currency_csv_excel

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


    return transactions
print(main())