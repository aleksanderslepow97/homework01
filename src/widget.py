from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(string_number: str) -> str:
    """функция обработки информации о картах и счетах"""
    if len(string_number.split()[-1]) == 16:
        new_number = get_mask_card_number(string_number.split()[-1])
        result = f"{string_number[:-16]}{new_number}"
    elif len(string_number.split()[-1]) == 20:
        new_number =  get_mask_card_number(string_number.split()[-1])
        result = f"{string_number[:-20]}{new_number}"
    return result


def get_date(one_data: str) -> str:
    """функция приема и возврата строки с датой"""
    two_data = one_data[0:10].split("-")
    return "-".join(two_data[::-1])
