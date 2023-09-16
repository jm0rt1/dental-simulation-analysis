
from dataclasses import dataclass

from dataclasses import dataclass
from typing import Optional

from src.app.analysis.parser.parser_interfaceable import ParserInterfaceable


@dataclass
class Space(ParserInterfaceable):
    rent: float
    utilities: float
    depreciation: float
    total_space: float

    repairs: Optional[float] = None

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        space = cls(
            rent=float(lines_list[68]),
            utilities=float(lines_list[69]),
            depreciation=float(lines_list[70]),
            total_space=float(lines_list[83])
        )

        return space

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        space = cls(
            rent=float(lines_list[96].replace(",", "")),
            utilities=float(lines_list[97].replace(",", "")),
            depreciation=float(lines_list[99].replace(",", "")),
            repairs=float(lines_list[98].replace(",", "")),
            total_space=float(lines_list[113].replace(",", ""))
        )

        return space


@dataclass
class Staff(ParserInterfaceable):
    wages: float
    office_payroll_taxes: float
    hiring_and_training_costs: float
    total_staff: float
    employee_benefits: Optional[float] = None
    employee_pension: Optional[float] = None

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        staff = cls(
            wages=float(lines_list[71]),
            office_payroll_taxes=float(lines_list[72]),
            hiring_and_training_costs=float(lines_list[73]),
            total_staff=float(lines_list[84])
        )
        return staff

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        staff = cls(
            wages=float(lines_list[91].replace(",", "")),
            employee_benefits=float(lines_list[92].replace(",", "")),
            employee_pension=float(lines_list[93].replace(",", "")),
            office_payroll_taxes=float(lines_list[94].replace(",", "")),
            hiring_and_training_costs=float(lines_list[95].replace(",", "")),
            total_staff=float(lines_list[112].replace(",", ""))
        )
        return staff


@dataclass
class TaxesAndInsurance(ParserInterfaceable):
    business_taxes: float
    bussiness_insurance: float
    total_taxes_and_insurance: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        t_and_i = cls(
            business_taxes=float(
                lines_list[74]),
            bussiness_insurance=float(lines_list[75]),
            total_taxes_and_insurance=float(lines_list[85])
        )
        return t_and_i

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        t_and_i = cls(
            business_taxes=float(
                lines_list[100].replace(",", "")),
            bussiness_insurance=float(lines_list[101].replace(",", "")),
            total_taxes_and_insurance=float(lines_list[114].replace(",", ""))
        )
        return t_and_i


@dataclass
class Marketing(ParserInterfaceable):
    advertising: float
    total_marketing: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        marketing = cls(
            advertising=float(lines_list[76]),
            total_marketing=float(lines_list[86])
        )

        return marketing

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        marketing = cls(
            advertising=float(lines_list[102].replace(",", "")),
            total_marketing=float(lines_list[115].replace(",", ""))
        )

        return marketing


@dataclass
class Other(ParserInterfaceable):
    office_expenses: float
    dues_and_continuing_ed: float
    auto_expenses: float
    miscellaneous: float
    total_other: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        other = cls(
            office_expenses=float(lines_list[77]),
            dues_and_continuing_ed=float(lines_list[78]),
            auto_expenses=float(lines_list[79]),
            miscellaneous=float(lines_list[80]),
            total_other=float(lines_list[87])
        )
        return other

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        other = cls(
            office_expenses=float(lines_list[107].replace(",", "")),
            dues_and_continuing_ed=float(lines_list[108].replace(",", "")),
            auto_expenses=float(lines_list[109].replace(",", "")),
            miscellaneous=float(lines_list[110].replace(",", "")),
            total_other=float(lines_list[118].replace(",", ""))
        )
        return other


@dataclass
class VariableCosts(ParserInterfaceable):
    clinical_supplies: float
    dental_lab: float
    office_supplies: float
    total_variable_costs: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        variable_costs = cls(
            clinical_supplies=float(lines_list[65]),
            dental_lab=float(lines_list[66]),
            office_supplies=float(lines_list[67]),
            total_variable_costs=float(lines_list[82])
        )
        return variable_costs

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        variable_costs = cls(
            dental_lab=float(lines_list[32].replace(",", "")),
            clinical_supplies=float(lines_list[33].replace(",", "")),
            office_supplies=float(lines_list[34].replace(",", "")),
            total_variable_costs=float(lines_list[111].replace(",", ""))
        )
        return variable_costs


@dataclass
class ProfessionalServices(ParserInterfaceable):
    legal_accounting: float
    market_research: float
    total_professional_services: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        pass

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        professional_services = cls(
            legal_accounting=float(lines_list[103].replace(",", "")),
            market_research=float(lines_list[104].replace(",", "")),
            total_professional_services=float(
                lines_list[116].replace(",", ""))
        )
        return professional_services


@dataclass
class Banking(ParserInterfaceable):
    interest_expense: float
    bank_charges: float
    total_banking: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        raise NotImplementedError()

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        banking = cls(
            interest_expense=float(lines_list[105].replace(",", "")),
            bank_charges=float(lines_list[106].replace(",", "")),
            total_banking=float(lines_list[117].replace(",", ""))
        )
        return banking


@dataclass
class FixedCosts(ParserInterfaceable):
    space: Space
    staff: Staff
    taxes_and_insurance: TaxesAndInsurance
    marketing: Marketing
    other: Other

    professional_services: Optional[ProfessionalServices] = None
    banking: Optional[Banking] = None

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        fixed_costs = cls(
            space=Space.from_lines_list_old(lines_list),
            staff=Staff.from_lines_list_old(lines_list),
            taxes_and_insurance=TaxesAndInsurance.from_lines_list_old(
                lines_list),
            marketing=Marketing.from_lines_list_old(lines_list),
            other=Other.from_lines_list_old(lines_list)
        )
        return fixed_costs

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        fixed_costs = cls(
            space=Space.from_lines_list_new(lines_list),
            staff=Staff.from_lines_list_new(lines_list),
            taxes_and_insurance=TaxesAndInsurance.from_lines_list_new(
                lines_list),
            marketing=Marketing.from_lines_list_new(lines_list),
            professional_services=ProfessionalServices.from_lines_list_new(
                lines_list),
            banking=Banking.from_lines_list_new(lines_list),
            other=Other.from_lines_list_new(lines_list)
        )
        return fixed_costs


@dataclass
class Income(ParserInterfaceable):
    production: float
    positive_payments_from_ar: float
    collections: float
    capitation_payments: Optional[float] = None
    billed_to_accounts_receivable: Optional[float] = None
    negative_payments_from_ar: Optional[float] = None

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        income = cls(
            production=float(lines_list[62]),
            positive_payments_from_ar=float(lines_list[63]),
            negative_payments_from_ar=float(lines_list[64]),
            collections=float(lines_list[81])
        )

        return income

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        income = cls(
            production=float(lines_list[4].replace(",", "")),
            positive_payments_from_ar=float(lines_list[18].replace(",", "")),
            capitation_payments=float(lines_list[19].replace(",", "")),
            billed_to_accounts_receivable=float(
                lines_list[20].replace(",", "")),
            collections=float(lines_list[22].replace(",", ""))
        )

        return income


@dataclass
class Expenses(ParserInterfaceable):
    variable_costs: VariableCosts
    fixed_costs: FixedCosts

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        expenses = cls(variable_costs=VariableCosts.from_lines_list_old(lines_list=lines_list),
                       fixed_costs=FixedCosts.from_lines_list_old(lines_list=lines_list))
        return expenses

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        expenses = cls(variable_costs=VariableCosts.from_lines_list_new(lines_list=lines_list),
                       fixed_costs=FixedCosts.from_lines_list_new(lines_list=lines_list))
        return expenses


@dataclass
class IncomeExpenseData(ParserInterfaceable):
    income: Income
    expenses: Expenses
    total_expenses: float
    profit_loss_this_qtr: float

    @classmethod
    def from_lines_list_old(cls, lines_list: list[str]):
        income_and_expenses = cls(
            income=Income.from_lines_list_old(lines_list),
            expenses=Expenses.from_lines_list_old(lines_list),
            total_expenses=float(lines_list[88]),
            profit_loss_this_qtr=float(lines_list[89])
        )
        return income_and_expenses

    @classmethod
    def from_lines_list_new(cls, lines_list: list[str]):
        profit_loss_this_qtr_str = lines_list[127].replace(",", "")
        if profit_loss_this_qtr_str.find("(") != -1:
            profit_loss_this_qtr = float(
                profit_loss_this_qtr_str.replace("(", "").replace(")", "")) * -1
        else:
            profit_loss_this_qtr = float(profit_loss_this_qtr_str)
        income_and_expenses = cls(
            income=Income.from_lines_list_new(lines_list),
            expenses=Expenses.from_lines_list_new(lines_list),
            total_expenses=float(lines_list[126].replace(",", "")),
            profit_loss_this_qtr=profit_loss_this_qtr
        )
        return income_and_expenses
