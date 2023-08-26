import re
import PyPDF2

# Function to extract text from the PDF


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text


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
income_expense_data = {
    "Income": {
        "Production": float(split_income_expense_section[62]),
        "positive Payments from A/R": float(split_income_expense_section[63]),
        "negative Payments from A/R": float(split_income_expense_section[64]),
        "Collections": float(split_income_expense_section[81]),
    },
    "Expenses": {
        "Variable Costs": {
            "Dental Supplies": float(split_income_expense_section[65]),
            "Dental Lab": float(split_income_expense_section[66]),
            "Office Supplies": float(split_income_expense_section[67]),
            "Total Variable Costs": float(split_income_expense_section[82]),
        },
        "Fixed Costs": {
            "Space": {
                "Rent": float(split_income_expense_section[68]),
                "Utilities": float(split_income_expense_section[69]),
                "Depreciation": float(split_income_expense_section[70]),
                "Total Space": float(split_income_expense_section[83]),
            },
            "Staff": {
                "Wages": float(split_income_expense_section[71]),
                "Office Payroll Taxes": float(split_income_expense_section[72]),
                "Hiring and Training Costs": float(split_income_expense_section[73]),
                "Total Staff": float(split_income_expense_section[84]),
            },
            "Office": {
                "Businuss Taxes and Insurance": float(split_income_expense_section[74]),
                "Office Expenses": float(split_income_expense_section[75]),
                "Total Office": float(split_income_expense_section[85]),
            },
            "Marketing": {
                "Advertising": float(split_income_expense_section[76]),
                "Total Marketing": float(split_income_expense_section[86]),
            },
            "Other": {
                "Professional Services": float(split_income_expense_section[77]),
                "Intereset Expense": float(split_income_expense_section[78]),
                "Bank Charges": float(split_income_expense_section[79]),
                "Miscellaneous": float(split_income_expense_section[80]),
                "Total Other": float(split_income_expense_section[87]),
            },
        },
        "Total Expenses": float(split_income_expense_section[88]),
    },
    "Profit (Loss) This Qtr": float(split_income_expense_section[89]),
}

income_expense_data

income_expense_data
pass
print(split_income_expense_section)
