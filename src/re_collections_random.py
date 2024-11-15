import re
from collections import Counter

from src.utils import get_json_data
from collections import Counter


tra=get_json_data()

def search_string (list_dict,str_search):
    '''возвращает список словарей транзакций по выбранному описанию транзакции'''
    pattern = re.compile(str_search)
    return [i for i in list_dict if i.get("description") is not None and pattern.search(i["description"])]
print(search_string(tra,'Открыти'))

def count_transactions (list_dict,categories):
    '''возвращает наименование транзакций и их количество'''
    return Counter([i["description"] for i in list_dict if i.get("description") is not None and i["description"] in categories])
