import re
import PyPDF2
from dataclasses import dataclass

# Function to extract text from the PDF


def extract_text_from_pdf(pdf_path: str) -> str:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text


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
class IncomeExpenseData:
    income: Income
    expenses: FixedCosts
    total_expenses: float
    profit_loss_this_qtr: float


# Extract text from the provided PDF
report_text = extract_text_from_pdf("tests/test_files/Report_Q-9.pdf")
# Display the first 1000 characters to get a glimpse of the content
report_text[:1000]
print(report_text[:1000])


# Split the report into sections
sections = re.split(r'\*\*\*', report_text)

# Extract the INCOME AND EXPENSE STATEMENT section
income_expense_section = sections[2]


def extract_value(pattern, text):
    """Helper function to extract values using regex."""
    match = re.search(pattern, text)
    return match.group(1) if match else None


split_income_expense_section = income_expense_section.split("\n")
split_income_expense_section = [item.replace(
    ",", "") for item in split_income_expense_section]

# Now we'll populate our dataclass instances:

space = Space(
    rent=float(split_income_expense_section[68]),
    utilities=float(split_income_expense_section[69]),
    depreciation=float(split_income_expense_section[70]),
    total_space=float(split_income_expense_section[83])
)

staff = Staff(
    wages=float(split_income_expense_section[71]),
    office_payroll_taxes=float(split_income_expense_section[72]),
    hiring_and_training_costs=float(split_income_expense_section[73]),
    total_staff=float(split_income_expense_section[84])
)

office = Office(
    business_taxes_and_insurance=float(split_income_expense_section[74]),
    office_expenses=float(split_income_expense_section[75]),
    total_office=float(split_income_expense_section[85])
)

marketing = Marketing(
    advertising=float(split_income_expense_section[76]),
    total_marketing=float(split_income_expense_section[86])
)

other = Other(
    professional_services=float(split_income_expense_section[77]),
    interest_expense=float(split_income_expense_section[78]),
    bank_charges=float(split_income_expense_section[79]),
    miscellaneous=float(split_income_expense_section[80]),
    total_other=float(split_income_expense_section[87])
)

variable_costs = VariableCosts(
    dental_supplies=float(split_income_expense_section[65]),
    dental_lab=float(split_income_expense_section[66]),
    office_supplies=float(split_income_expense_section[67]),
    total_variable_costs=float(split_income_expense_section[82])
)

fixed_costs = FixedCosts(
    space=space,
    staff=staff,
    office=office,
    marketing=marketing,
    other=other
)

income = Income(
    production=float(split_income_expense_section[62]),
    positive_payments_from_ar=float(split_income_expense_section[63]),
    negative_payments_from_ar=float(split_income_expense_section[64]),
    collections=float(split_income_expense_section[81])
)

data = IncomeExpenseData(
    income=income,
    expenses=fixed_costs,
    total_expenses=float(split_income_expense_section[88]),
    profit_loss_this_qtr=float(split_income_expense_section[89])
)

print(data)
