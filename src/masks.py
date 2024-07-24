from typing import Union


def get_mask_card_number(card_number: str) -> Union[str, None]:
    """Функция маскировки номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        # logger.info(f"Производим маскировку номера карты {card_number}")
        masks_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        return masks_card
    else:
        return None


def get_mask_account(account: str) -> Union[str, None]:
    """Функция маскировки номера счета"""
    if account.isdigit() and len(account) == 20:
        # logger.info(f"Производим маскировку номера счета {account}")
        masks_account = f"**{account[-4::]}"
        return masks_account
    else:
        return None


def mask_account_card(account_card: str) -> Union[str, None]:
    """Функция маскировки номера карты или номера счета"""
    numeral = account_card[-20:]
    if numeral.isdigit():  # account_card[:3] == "Счет" and
        account = str(numeral)
        return f"{account_card[0:-20]} {get_mask_account(account)}"
    else:
        card_number = str(account_card[-16:])
        return f"{account_card[0:-16]} {get_mask_card_number(card_number)}"
