
# idr  =  "Internal Data Representation"

from app.analysis.parser.cash_management import CashManagement
from app.analysis.parser.income_expense_data import IncomeExpenseData
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


class IDR(ParserInterfaceable):
    def __init__(self, income_expense_data: IncomeExpenseData, cash_management: CashManagement) -> None:
        self.data = None

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]) -> "IDR":
        idr = cls(IncomeExpenseData.from_lines_list_old(lines_list=lines_list),
                  CashManagement.from_lines_list_old(lines_list=lines_list))
        return idr

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]) -> "IDR":
        idr = cls(IncomeExpenseData.from_lines_list_new(lines_list=lines_list),
                  CashManagement.from_lines_list_new(lines_list=lines_list))
        return idr
