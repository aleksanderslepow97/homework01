import pytest

from src.masks import masked_card_num, masked_account_num


@pytest.mark.parametrize("string, expected_result", [
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 12345678901234567890", "Счет **7890"),
])
def test_masked_card_num(string, expected_result):
    assert masked_card_num(string) == expected_result


@pytest.fixture
def date():
    return "2018-07-11T02:26:18.671407"


@pytest.mark.parametrize("string, expected_result", [
    ("7158300734726758", "7158 30** **** 6758"),
    ("7158300734726759", "7158 30** **** 6759"),
])
def test_masked_card_num(string, expected_result):
    assert masked_card_num(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("12345678901234567340", "**7340"),
    ("12345678901234567890", "**7890"),
])
def test_masked_account_num(string, expected_result):
    assert masked_account_num(string) == expected_result
