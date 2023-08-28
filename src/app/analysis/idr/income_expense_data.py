
from dataclasses import dataclass


@dataclass
class Space:
    rent: float
    utilities: float
    depreciation: float
    total_space: float


@dataclass
class Staff:
    wages: float
    office_payroll_taxes: float
    hiring_and_training_costs: float
    total_staff: float


@dataclass
class Office:
    business_taxes_and_insurance: float
    office_expenses: float
    total_office: float


@dataclass
class Marketing:
    advertising: float
    total_marketing: float


@dataclass
class Other:
    professional_services: float
    interest_expense: float
    bank_charges: float
    miscellaneous: float
    total_other: float


@dataclass
class VariableCosts:
    dental_supplies: float
    dental_lab: float
    office_supplies: float
    total_variable_costs: float


@dataclass
class FixedCosts:
    space: Space
    staff: Staff
    office: Office
    marketing: Marketing
    other: Other


@dataclass
class Income:
    production: float
    positive_payments_from_ar: float
    negative_payments_from_ar: float
    collections: float


@dataclass
class Expenses:
    variable_costs: VariableCosts
    fixed_costs: FixedCosts


@dataclass
class IncomeExpenseData:
    income: Income
    expenses: Expenses
    total_expenses: float
    profit_loss_this_qtr: float
