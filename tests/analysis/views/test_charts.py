from pathlib import Path
from src.app.analysis.parser.parser import Parser
from src.app.analysis.idr.data_classes.report import Report, reports_to_dataframe
from src.app.views.charts import project_burndown_chart_advanced
import unittest


class TestCharts(unittest.TestCase):

    def test_burndown_chart(self):
        result0 = Parser(Path("tests/test_files/Report_Q-1-3.pdf")).parse()
        result1 = Parser(Path("tests/test_files/Report_Q-2-3.pdf")).parse()
        result2 = Parser(Path("tests/test_files/Report_Q-3-2.pdf")).parse()
        result3 = Parser(Path("tests/test_files/Report_Q-4-2.pdf")).parse()

        project_burndown_chart_advanced([result0, result1, result2, result3])
        project_burndown_chart_advanced([result0, result1, result2])
        project_burndown_chart_advanced([result0, result1])
        project_burndown_chart_advanced([result0])
