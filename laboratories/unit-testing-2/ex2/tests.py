import unittest
from ex2 import get_marks
from requests.exceptions import Timeout
from unittest.mock import patch

class TestMarks(unittest.TestCase):
    def test_get_marks_timeout(self, mock_requests):
        return 0

if __name__ == '__main__':
    unittest.main()