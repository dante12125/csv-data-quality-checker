import unittest

from src.checker import (
    count_missing_values,
    count_duplicates,
    get_basic_statistics,
    find_invalid_numeric_values
)

class TestDataQualityChecker(unittest.TestCase):

    def setUp(self):
        self.rows = [
            {
                "id": "1",
                "name": "Asha",
                "age": "22"
            },
            {
                "id": "2",
                "name": "",
                "age": "25"
            },
            {
                "id": "2",
                "name": "",
                "age": "25"
            }
        ]

    def test_missing_values(self):
        result = count_missing_values(self.rows)

        self.assertEqual(result["name"], 2)
        self.assertEqual(result["age"], 0)

    def test_duplicates(self):
        result = count_duplicates(self.rows)

        self.assertEqual(result, 1)

    def test_statistics(self):
        result = get_basic_statistics(self.rows)

        self.assertEqual(result["rows"], 3)
        self.assertEqual(result["columns"], 3)


if __name__ == "__main__":
    unittest.main()
