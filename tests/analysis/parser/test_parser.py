import unittest
from src.app.analysis.parser.parser import Parser


class TestParser(unittest.TestCase):
    def test_parser(self):

        parser = Parser()
        parser.parse()
        print(parser.data)
