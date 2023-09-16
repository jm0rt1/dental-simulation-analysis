from dataclasses import dataclass
from typing import Optional
from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


@dataclass
class CashManagementData(ParserInterfaceable):
    ending_cash_last_quarter: float
    ending_cash_this_quarter: float
    overdrawn_checks_paid: float
    depreciation_expense: float
    loan_addition: float
    normal_loan_principal_payment: float
    draw: float
    profit_loss: Optional[float] = None
    collections: Optional[float] = None
    cds_redeemed: Optional[float] = None
    interest_earned: Optional[float] = None
    estimated_tax_payment: Optional[float] = None
    personal_retirement_plan_contribution: Optional[float] = None
    total_expenses: Optional[float] = None
    cds_purchased: Optional[float] = None
    income_tax_paid_or_refund: Optional[float] = None

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
        income_tax_paid_or_refund = lines_list[230].replace(",", "")
        if income_tax_paid_or_refund.find("(") != -1:
            income_tax_paid_or_refund = float(
                income_tax_paid_or_refund.replace("(", "").replace(")", "")) * -1
        else:
            income_tax_paid_or_refund = float(
                income_tax_paid_or_refund.replace(",", ""))

        cash_management = cls(
            ending_cash_last_quarter=float(lines_list[217].replace(",", "")),
            overdrawn_checks_paid=float(lines_list[218].replace(",", "")),
            collections=float(lines_list[219].replace(",", "")),
            loan_addition=float(lines_list[220].replace(",", "")),
            depreciation_expense=float(lines_list[221].replace(",", "")),
            cds_redeemed=float(lines_list[222].replace(",", "")),
            interest_earned=float(lines_list[223].replace(",", "")),
            estimated_tax_payment=float(lines_list[224].replace(",", ""))*-1,
            normal_loan_principal_payment=float(
                lines_list[225].replace(",", ""))*-1,
            personal_retirement_plan_contribution=float(
                lines_list[226].replace(",", ""))*-1,
            draw=float(lines_list[227].replace(",", ""))*-1,
            total_expenses=float(lines_list[228].replace(",", ""))*-1,
            cds_purchased=float(lines_list[229].replace(",", ""))*-1,
            income_tax_paid_or_refund=income_tax_paid_or_refund,
            ending_cash_this_quarter=float(lines_list[231].replace(",", "")),
        )
        return cash_management
