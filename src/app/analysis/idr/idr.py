
# idr  =  "Internal Data Representation"

from src.app.analysis.idr.cash_management import CashManagement
from src.app.analysis.idr.income_expense_data import IncomeExpenseData
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


class idr(ParserInterfaceable):
    def __init__(self) -> None:
        self.data = None

    @classmethod
    def from_lines_list(cls, lines_list: list[str]) -> "idr":
        idr = cls(IncomeExpenseData.from_lines_list(lines_list=lines_list),
                  CashManagement.from_lines_list(lines_list=lines_list)
        return idr
