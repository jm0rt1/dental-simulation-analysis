
# idr  =  "Internal Data Representation"

from app.analysis.parser.cash_management import CashManagement
from app.analysis.parser.income_expense_data import IncomeExpenseData
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


class IDR(ParserInterfaceable):
    def __init__(self):
        
