

import pandas as pd
from dataclasses import dataclass
from src.app.analysis.idr.data_classes.cash_management import CashManagementData
from src.app.analysis.idr.data_classes.income_expense_data import IncomeExpenseData
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


@dataclass
class Report(ParserInterfaceable):
    income_expense_data: IncomeExpenseData
    cash_management_data: CashManagementData

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]) -> "Report":
        report = cls(income_expense_data=lines_list[0],
                     cach_management_data=lines_list[1:])
        return report

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]) -> "Report":
        report = cls(IncomeExpenseData.from_lines_list_new(lines_list=lines_list),
                     CashManagementData.from_lines_list_new(lines_list=lines_list))
        return report


def reports_to_dataframe(reports: list) -> pd.DataFrame:
    data_list = [flatten_dict(report.to_dict()) for report in reports]
    df = pd.DataFrame(data_list)
    print(df)
    pd.DataFrame.to_csv(df, "output.csv")
    return df


def flatten_dict(data, parent_key='', sep='_'):
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items
