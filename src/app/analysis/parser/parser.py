from pathlib import Path
import re
import PyPDF2

from src.app.analysis.idr.income_expense_data import Expenses, FixedCosts, Income, IncomeExpenseData, Marketing, Office, Other, Space, Staff, VariableCosts

# Function to extract text from the PDF


class Parser():
    def __init__(self, pdf_path: Path = Path("tests/test_files/Report_Q-9.pdf")):
        self.pdf_path = pdf_path
        if self.pdf_path.suffix != ".pdf":
            raise TypeError("File must be a PDF.")
        if not self.pdf_path.exists():
            raise FileNotFoundError("File does not exist.")

        self.report_text: str = ""

    def extract_text_from_pdf(self, pdf_path: Path) -> str:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
        return text

    def parse(self):
        # Extract text from the provided PDF
        self.report_text = self.extract_text_from_pdf(
            self.pdf_path)

        # Split the report into sections
        sections = re.split(r'\*\*\*', self.report_text)

        # Extract the INCOME AND EXPENSE STATEMENT section
        income_expense_section = sections[2]

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
            business_taxes_and_insurance=float(
                split_income_expense_section[74]),
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

        expenses = Expenses(variable_costs=variable_costs,
                            fixed_costs=fixed_costs)

        self.data = IncomeExpenseData(
            income=income,
            expenses=expenses,
            total_expenses=float(split_income_expense_section[88]),
            profit_loss_this_qtr=float(split_income_expense_section[89])
        )
