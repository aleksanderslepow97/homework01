import sys
from pathlib import Path
from unittest.mock import patch

from src.read_csv import read_csv
from src.сonfig import ROOT_PATH

sys.path.append(str(Path(__file__).resolve().parent.parent))

path_to_file = Path(ROOT_PATH, "../data/transactions.csv")


@patch("csv.reader")
def test_read_csv(mock_reader):
    # Настраиваем mock_reader чтобы он возвращал нужный результат
    mock_reader.return_value = iter(
        [
            ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "SoL",
                "PEN",
                "Счет 58803664651298323391",
                "Счет 39746506635466619397",
                "Перевод организации",
            ],
        ]
    )

    result = read_csv(path_to_file)
    expected_result = [
        {
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664651298323391",
            "id": "650703",
            "operationAmount": {"amount": "16210", "currency": {"code": "PEN", "name": "SoL"}},
            "state": "EXECUTED",
            "to": "Счет 39746506635466619397",
        }
    ]
    assert result == expected_result
