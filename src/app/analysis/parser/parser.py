from pathlib import Path
import re
import PyPDF2

from src.app.analysis.idr.income_expense_data import Expenses, FixedCosts, Income, IncomeExpenseData, Marketing, Other, Space, Staff, VariableCosts
from src.shared.settings.settings import GlobalSettings
# Function to extract text from the PDF


class Parser():
    PARSER_OUTPUT_DIR = GlobalSettings.OUTPUT_DIR/"parser"

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path
        if self.pdf_path.suffix != ".pdf":
            raise TypeError("File must be a PDF.")
        if not self.pdf_path.exists():
            raise FileNotFoundError("File does not exist.")

        self.report_text: str = ""

    @property
    def report_text_file_path(self) -> Path:
        file_path = Parser.PARSER_OUTPUT_DIR / \
            f"report_text_files/{self.pdf_path.stem}.txt"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        return file_path

    @property
    def report_sections_file_path(self) -> Path:
        file_path = self.PARSER_OUTPUT_DIR / \
            f"report_sections/{self.pdf_path.stem}.txt"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        return file_path

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
        # write report text to a file in outputs/report_text_files/{pdf_name}.txt

        with open(self.report_text_file_path, "w") as file:
            file.write(self.report_text)

        # Split the report into sections
        self.sections = re.split(r'\*\*\*', self.report_text)

        # write report sections to a file in outputs/report_sections/{pdf_name}.txt

        with open(self.report_sections_file_path, "w") as file:
            file.write("\n\n".join(self.sections))

        # Extract the INCOME AND EXPENSE STATEMENT section

        # write
        # Extract the INCOME AND EXPENSE STATEMENT section
        income_expense_section = self.sections[12]

        # split the section into lines
        lines_list = income_expense_section.split("\n")

        # lines_list = income_expense_section.split("\n")
        # lines_list = [item.replace(
        #     ",", "") for item in lines_list]

        # Now we'll populate our dataclass instances:

        self.data = IncomeExpenseData.from_lines_list_new(
            lines_list=lines_list)
