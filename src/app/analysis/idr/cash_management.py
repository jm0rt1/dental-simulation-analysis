from dataclasses import dataclass
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


@dataclass
class CashManagement(ParserInterfaceable):
    ending_cash_last_quarter: float
    ending_cash_this_quarter: float
    overdrawn_checks_paid: float
    profit_loss: float
    depreciation_expense: float
    loan_addition: float
    normal_loan_principal_payment: float
    draw: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        cash_management = cls(
            ending_cash_last_quarter=float(lines_list[86]),
            ending_cash_this_quarter=float(lines_list[87]),
            overdrawn_checks_paid=float(lines_list[88]),
            profit_loss=float(lines_list[89]),
            depreciation_expense=float(lines_list[90]),
            loan_addition=float(lines_list[91]),
            normal_loan_principal_payment=float(lines_list[92]),
            draw=float(lines_list[93])
        )
        return cash_management
