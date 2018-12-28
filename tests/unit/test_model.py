import unittest
from datetime import datetime as dt
from app.models import Record


class RecordTestCase(unittest.TestCase):

    def test_record_init(self):
        """
        Test that a record instance has the same attributes as given
        """
        data = {
            "value": 10.00,
            "description": "Just a regular record",
            "datetime": dt.now().isoformat(timespec="seconds")
        }
        result = Record(**data)
        self.assertEqual(result.value, data["value"])
        self.assertEqual(result.description, data["description"])
        self.assertEqual(result.datetime, data["datetime"])

    def test_record_no_value(self):
        """
        Test that Record raises TypeError if not given a value upon creation
        """
        data = {
            "description": "Just a regular record",
            "datetime": dt.now().isoformat(timespec="seconds")
        }
        with self.assertRaises(TypeError):
            result = Record(**data)

    def test_record_no_description(self):
        """
        Test that a record instance created without a given description
        has one that is None
        """
        data = {
            "value": 10.00,
            "datetime": dt.now().isoformat(timespec="seconds")
        }
        result = Record(**data)
        self.assertIsNone(result.description)

    def test_record_no_datetime(self):
        """
        Test that a record instance created without a given datetime
        has one earlier or equal than dt.now()
        """
        data = {
            "value": 10.00
        }
        result = Record(**data)
        self.assertLessEqual(
            dt.strptime(result.datetime, "%Y-%m-%dT%H:%M:%S"),
            dt.now())

    def test_record_from_int_value(self):
        """
        Test that a record instance's value is returned as float even if
        it was passed an int
        """
        data = {
            "value": 42
        }
        result = Record(**data)
        self.assertEqual(result.value, float(data["value"]))

    def test_record_negative_value(self):
        """
        Test that a record instance can be created with a negative value
        """
        data = {
            "value": -2.43,
        }
        result = Record(**data)
        self.assertEqual(result.value, data["value"])
