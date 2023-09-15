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
            ending_cash_last_quarter=float(lines_list[86].replace(",", "")),
            ending_cash_this_quarter=float(lines_list[87].replace(",", "")),
            overdrawn_checks_paid=float(lines_list[88].replace(",", "")),
            profit_loss=float(lines_list[89].replace(",", "")),
            depreciation_expense=float(lines_list[90].replace(",", "")),
            loan_addition=float(lines_list[91].replace(",", "")),
            normal_loan_principal_payment=float(
                lines_list[92].replace(",", "")),
            draw=float(lines_list[93].replace(",", ""))
        )
        return cash_management

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        cash_management = cls(
            ending_cash_last_quarter=float(lines_list[86].replace(",", "")),
            ending_cash_this_quarter=float(lines_list[87].replace(",", "")),
            overdrawn_checks_paid=float(lines_list[88].replace(",", "")),
            profit_loss=float(lines_list[89].replace(",", "")),
            depreciation_expense=float(lines_list[90].replace(",", "")),
            loan_addition=float(lines_list[91].replace(",", "")),
            normal_loan_principal_payment=float(
                lines_list[92].replace(",", "")),
            draw=float(lines_list[93].replace(",", ""))
        )
        return cash_management
