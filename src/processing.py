from typing import Optional


def filter_by_state(list_data: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """принимает список словарей и возвращает отфильтрованный список по параметру state"""

    list_filtered = []
    for i in list_data:
        if i.get("state", -1) != -1:
            if i["state"] == state:
                list_filtered.append(i)
    return list_filtered


def sort_by_date(list_data: list[dict], rev=True) -> list[dict]:
    """принимает список словарей и возвращает отфильтрованный список по убыванию даты"""

    sorted_list = sorted(list_data, key=lambda x: x["date"] if x["date"] is not None else "0", reverse=rev)
    return sorted_list
