from pathlib import Path
import unittest
from src.app.analysis.parser.parser import Parser
from src.app.analysis.idr.data_classes.report import Report, reports_to_dataframe
import json

REPORT_Q_9 = Path("tests/test_files/Report_Q-9.pdf")
REPORT_Q_1_3 = Path("tests/test_files/Report_Q-1-3.pdf")


class TestParser(unittest.TestCase):
    def test_parser(self):

        parser = Parser(REPORT_Q_9)
        parser.parse()
        actual = str(parser.data)

        expected = "IncomeExpenseData(income=Income(production=140695.0, positive_payments_from_ar=44837.0, negative_payments_from_ar=66127.0, collections=119405.0), expenses=Expenses(variable_costs=VariableCosts(dental_supplies=5911.0, dental_lab=9345.0, office_supplies=2814.0, total_variable_costs=18070.0), fixed_costs=FixedCosts(space=Space(rent=6000.0, utilities=2500.0, depreciation=1645.0, total_space=10145.0), staff=Staff(wages=32928.0, office_payroll_taxes=4281.0, hiring_and_training_costs=5000.0, total_staff=42209.0), office=Office(business_taxes_and_insurance=1300.0, office_expenses=130.0, total_office=1430.0), marketing=Marketing(advertising=1158.0, total_marketing=1158.0), other=Other(professional_services=350.0, interest_expense=3364.0, bank_charges=0.0, miscellaneous=200.0, total_other=3914.0))), total_expenses=76926.0, profit_loss_this_qtr=42479.0)"
        self.assertEqual(expected, actual)

    def test_parser_on_new_file(self):

        parser = Parser(REPORT_Q_1_3)
        parser.parse()

    def test_parser_data_on_all_files(self):
        datas = []
        for file in Path("tests/test_files").iterdir():
            if file.suffix == ".pdf":

                parser = Parser(file)
                report = parser.parse()

                datas.append(report)
                dicto = report.to_dict()
                with open(file.parent / f"{file.stem}.json", "w") as file:
                    json_string = json.dumps(dicto, indent=4)
                    file.write(json_string)

                pass
        # check if all are the same length
        reports_to_dataframe(datas)
        # self.assertTrue(all(len(data) == len(datas[0]) for data in datas))
