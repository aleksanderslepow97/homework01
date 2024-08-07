import pytest
from src.widget import get_date, mask_account_card


@pytest.fixture
def my_card_number():
    return "Maestro 1596837868705199"


def test_mask_account_card(my_card_number):
    assert mask_account_card(my_card_number) == "Maestro  1596 83** **** 5199"


@pytest.fixture
def data():
    return "2018-07-11T02:26:18.671407"


def test_get_date(data):
    assert get_date(data) == "11.07.2018"
