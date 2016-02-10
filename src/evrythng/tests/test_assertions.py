from unittest import TestCase

from evrythng.entities import assertions
from evrythng.exceptions import InvalidDatatypeException


class AssertionsTest(TestCase):

    def test_datatype_str_num_bool_with_str(self):
        self.assertIsNone(assertions.datatype_str_num_bool('whatever', 'hi'))

    def test_datatype_str_num_bool_with_int(self):
        self.assertIsNone(assertions.datatype_str_num_bool('whatever', 1))

    def test_datatype_str_num_bool_with_float(self):
        self.assertIsNone(assertions.datatype_str_num_bool('whatever', 1.0))

    def test_datatype_str_num_bool_with_bool(self):
        self.assertIsNone(assertions.datatype_str_num_bool('whatever', True))

    def test_datatype_str_num_bool_with_dict(self):
        self.assertRaises(
            InvalidDatatypeException, assertions.datatype_str_num_bool,
            'whatever', {'foo': 'bar'})

    def test_datatype_str_num_bool_with_list(self):
        self.assertRaises(
            InvalidDatatypeException, assertions.datatype_str_num_bool,
            'whatever', ['foo', 'bar'])

    def test_datatype_str_num_bool_with_none(self):
        self.assertRaises(
            InvalidDatatypeException, assertions.datatype_str_num_bool,
            'whatever', None)
