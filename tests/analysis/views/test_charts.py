from src.app.analysis.parser.parser import Parser
import unittest


class TestCharts(unittest.TestCase):

    def test_burndown_chart(self):
        result = Parser("tests/test_files/Report_Q-9.pdf").parse()
        