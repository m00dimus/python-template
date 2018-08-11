import sys
import unittest
from io import StringIO
from unittest.mock import patch

from main import *

class TestDefault(unittest.TestCase):
    """docstring for TestMain"""
    def testTestDefault(self):
        print("\nTesting Default\n")

    def test01(self):
        """ Test main function returns no value """
        want=""
        with patch('sys.stdout', new=StringIO()) as result:
            main()
            got=result.getvalue().strip()
            self.assertEqual(got, want)

if __name__ == '__main__':
    unittest.main()
