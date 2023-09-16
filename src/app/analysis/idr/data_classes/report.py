

from src.app.analysis.idr.data_classes.cash_management import CashManagementData
from src.app.analysis.idr.data_classes.income_expense_data import IncomeExpenseData
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


class Report(ParserInterfaceable):
    def __init__(self, income_expense_data: IncomeExpenseData, cach_management_data: CashManagementData) -> None:
        self.income_expense_data = income_expense_data
        self.cach_management_data = cach_management_data

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
