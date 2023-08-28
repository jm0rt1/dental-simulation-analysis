
from dataclasses import dataclass

from dataclasses import dataclass

from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


@dataclass
class Space(ParserInterfaceable):
    rent: float
    utilities: float
    depreciation: float
    total_space: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        space = cls(
            rent=float(lines_list[68]),
            utilities=float(lines_list[69]),
            depreciation=float(lines_list[70]),
            total_space=float(lines_list[83])
        )

        return space


@dataclass
class Staff(ParserInterfaceable):
    wages: float
    office_payroll_taxes: float
    hiring_and_training_costs: float
    total_staff: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        staff = cls(
            wages=float(lines_list[71]),
            office_payroll_taxes=float(lines_list[72]),
            hiring_and_training_costs=float(lines_list[73]),
            total_staff=float(lines_list[84])
        )
        return staff


@dataclass
class Office(ParserInterfaceable):
    business_taxes_and_insurance: float
    office_expenses: float
    total_office: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        office = cls(
            business_taxes_and_insurance=float(
                lines_list[74]),
            office_expenses=float(lines_list[75]),
            total_office=float(lines_list[85])
        )
        return office


@dataclass
class Marketing(ParserInterfaceable):
    advertising: float
    total_marketing: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        marketing = cls(
            advertising=float(lines_list[76]),
            total_marketing=float(lines_list[86])
        )

        return marketing


@dataclass
class Other(ParserInterfaceable):
    professional_services: float
    interest_expense: float
    bank_charges: float
    miscellaneous: float
    total_other: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        other = cls(
            professional_services=float(lines_list[77]),
            interest_expense=float(lines_list[78]),
            bank_charges=float(lines_list[79]),
            miscellaneous=float(lines_list[80]),
            total_other=float(lines_list[87])
        )
        return other


@dataclass
class VariableCosts(ParserInterfaceable):
    dental_supplies: float
    dental_lab: float
    office_supplies: float
    total_variable_costs: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        variable_costs = cls(
            dental_supplies=float(lines_list[65]),
            dental_lab=float(lines_list[66]),
            office_supplies=float(lines_list[67]),
            total_variable_costs=float(lines_list[82])
        )
        return variable_costs


@dataclass
class FixedCosts(ParserInterfaceable):
    space: Space
    staff: Staff
    office: Office
    marketing: Marketing
    other: Other

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        fixed_costs = cls(
            space=Space.from_lines_list(lines_list),
            staff=Staff.from_lines_list(lines_list),
            office=Office.from_lines_list(lines_list),
            marketing=Marketing.from_lines_list(lines_list),
            other=Other.from_lines_list(lines_list)
        )
        return fixed_costs


@dataclass
class Income(ParserInterfaceable):
    production: float
    positive_payments_from_ar: float
    negative_payments_from_ar: float
    collections: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        income = cls(
            production=float(lines_list[62]),
            positive_payments_from_ar=float(lines_list[63]),
            negative_payments_from_ar=float(lines_list[64]),
            collections=float(lines_list[81])
        )

        return income


@dataclass
class Expenses(ParserInterfaceable):
    variable_costs: VariableCosts
    fixed_costs: FixedCosts

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        expenses = cls(variable_costs=VariableCosts.from_lines_list(lines_list=lines_list),
                       fixed_costs=FixedCosts.from_lines_list(lines_list=lines_list))
        return expenses


@dataclass
class IncomeExpenseData(ParserInterfaceable):
    income: Income
    expenses: Expenses
    total_expenses: float
    profit_loss_this_qtr: float

    @classmethod
    def from_lines_list(cls, lines_list: list[str]):
        income_and_expenses = cls(
            income=Income.from_lines_list(lines_list),
            expenses=Expenses.from_lines_list(lines_list),
            total_expenses=float(lines_list[88]),
            profit_loss_this_qtr=float(lines_list[89])
        )
        return income_and_expenses
