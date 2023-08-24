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
income_expense_section = sections[1]

# Use regular expressions to extract data from the INCOME AND EXPENSE STATEMENT section
income_expense_data = {
    "Income": {
        "Production": re.search(r'Production\s*(\d+,\d+)', income_expense_section).group(1),
        "Collections": re.search(r'Collections\s*(\d+,\d+)', income_expense_section).group(1),
    },
    "Expenses": {
        "Variable Costs": re.search(r'Variable\nCosts\s*(\d+,\d+)', income_expense_section).group(1),
        "Fixed Costs": re.search(r'Fixed\nCosts\s*(\d+,\d+)', income_expense_section).group(1),
        "Total Expenses": re.search(r'Total\nExpenses\s*(\d+,\d+)', income_expense_section).group(1),
    },
    "Profit (Loss) This Qtr": re.search(r'PROFIT\n\(LOSS\)\nTHIS\nQTR:\s*([\+\-]?\d+,\d+)', income_expense_section).group(1)
}

income_expense_data
pass
