import pytest

from src.masks import masked_account_num, masked_card_num


@pytest.fixture
def coll():
    return "2018-07-11T02:26:18.671407"


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_add(x, expected):
    assert masked_card_num(x) == expected


def test_dated(coll):
    assert masked_account_num(coll) == "11.07.2018"
