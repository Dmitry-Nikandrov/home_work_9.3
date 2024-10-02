def filter_by_state(list_data, state = 'EXECUTED'):
    '''принимает список данных и возвращает отфильтрованный список по параметру "state"'''
    list_filtered = []
    for i in list_data:
        if i.get('state',-1)!=-1:
            if i['state']==state:
                list_filtered.append(i)
    return list_filtered

def sort_by_date(list_data,reverse=True):
    '''принимает список данных и возвращает отфильтрованный список по убыванию даты'''
    sorted_list = sorted(list_data,key=lambda x: x['date'],reverse=reverse)
    return sorted_list

