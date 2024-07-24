from typing import Dict, List


def filter_by_state(transactions: List[Dict], key_dict: str = "") -> List[Dict]:
    """Функция фильтрации операций по ключу"""
    filtered_list = []
    for i in range(len(transactions)):
        if str(transactions[i].get("state")).upper() == str(key_dict).upper():
            filtered_list.append(transactions[i])
    # print(f" фильтрация по статусу {filtered_list}")
    return filtered_list


def sort_by_date(transactions: list[Dict], ascending: bool = True) -> list[Dict]:
    """Функция сортировки операций по убыванию даты"""
    for transaction in transactions:
        if transaction.get("date") is None:
            sort_dict = transactions
            return sort_dict
        else:
            sort_dict = sorted(transactions, key=lambda x: x["date"], reverse=ascending)
    return sort_dict
