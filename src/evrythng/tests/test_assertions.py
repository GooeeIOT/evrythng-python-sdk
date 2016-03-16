from unittest import TestCase

from evrythng.entities import assertions
from evrythng.exceptions import InvalidDatatypeException


class AssertionsTest(TestCase):

    def test_datatype_json_with_str(self):
        self.assertIsNone(assertions.datatype_json('whatever', 'hi'))

    def test_datatype_json_with_int(self):
        self.assertIsNone(assertions.datatype_json('whatever', 1))

    def test_datatype_json_with_float(self):
        self.assertIsNone(assertions.datatype_json('whatever', 1.0))

    def test_datatype_json_with_bool(self):
        self.assertIsNone(assertions.datatype_json('whatever', True))

    def test_datatype_json_with_dict(self):
        self.assertIsNone(assertions.datatype_json(
            'whatever', {'foo': 'bar'}))

    def test_datatype_json_with_list(self):
        self.assertIsNone(assertions.datatype_json(
            'whatever', [{'foo': 'bar'}]))

    def test_datatype_json_with_set(self):
        self.assertRaises(
            InvalidDatatypeException, assertions.datatype_json,
            'whatever', set((1, 2, 3)))
