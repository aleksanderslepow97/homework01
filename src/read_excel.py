import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.сonfig import ROOT_PATH


def read_excel(path_to_file: Path) -> list:
    """Функция чтения транзакций из excel-файла"""
    with open(path_to_file, "r", encoding="utf-8") as excel_file:
        try:
            df = pd.read_excel(path_to_file)
            # df = my_df.astype(float)
            transactions = []
            for i in range(0, len(df)):
                row_dict = {
                    "id": df.loc[i, "id"],
                    "date": df.loc[i, "date"],
                    "state": df.loc[i, "state"],
                    "operationAmount": {
                        "amount": df.loc[i, "amount"],
                        "currency": {
                            "name": df.loc[i, "currency_name"],
                            "code": df.loc[i, "currency_code"],
                        },
                    },
                    "description": df.loc[i, "description"],
                    "from": df.loc[i, "from"],
                    "to": df.loc[i, "to"],
                }
                transactions.append(row_dict)
            return transactions
        except Exception:
            print("Ошибка чтения excel")
            return []
