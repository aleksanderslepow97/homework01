from typing import Union

from src import masks


def mask_account_card(account_card: str) -> Union[str, None]:
    """Функция маскировки номера карты или номера счета"""
    numeral = account_card[-20:]
    if numeral.isdigit():
        account = str(numeral)
        return f"{account_card[0:-20]} {masks.get_mask_account(account)}"
    else:
        card_number = str(account_card[-16:])
        return f"{account_card[0:-16]} {masks.get_mask_card_number(card_number)}"


def get_date(date: str) -> Union[str, None]:
    """Функция преобразования даты"""
    date_time = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return date_time
