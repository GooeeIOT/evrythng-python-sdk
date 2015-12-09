import os

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json
import requests

from evrythng.exceptions import (
    ExtraDataSubmittedException,
    InvalidDatatypeException,
    ReadOnlyFieldWrittenToException,
    RequiredFieldException,
)


def request(self, request_type, resource_url, data=None,
            api_key=None, content_type='application/json'):
    if api_key is None:
        os.getenv('EVRYTHNG_API_TOKEN')
    request_func = getattr(requests, request_type.lower())
    url = '{}{}'.format(self.base_url, resource_url)
    kwargs = {
        'headers': {'Content-Type': content_type},
    }

    if api_key:
        kwargs['Authorization'] = 'Token {}'.format(api_key)

    if data:
        kwargs['json'] = json.dumps(data)

    response = request_func(url, **kwargs)

    return response


def assert_required(supplied_fields, required_fields):
    """Assert that all required fields are in the supplied_fields."""
    for field in required_fields:
        try:
            assert field in locals
        except AssertionError:
            raise RequiredFieldException(field)


def assert_readonly(supplied_fields, readonly_fields):
    """Assert that a read only field wasn't supplied as a field/value."""
    for field in readonly_fields:
        try:
            assert field not in locals
        except AssertionError:
            raise ReadOnlyFieldWrittenToException(field, supplied_fields[field])


def assert_no_extras(supplied_fields, possible_fields):
    """Assert that there are no extra fields in the supplied_fields."""
    for field in supplied_fields:
        try:
            assert field in possible_fields
        except AssertionError:
            raise ExtraDataSubmittedException(field, supplied_fields[field])


def assert_datatype_str(field, value):
    """Assert that the value is of type str."""
    try:
        assert isinstance(value, str)
    except AssertionError:
        raise InvalidDatatypeException(field, str, type(value))


def assert_datatype_time(field, value):
    """Assert that the value is of type int."""
    try:
        assert isinstance(value, int)
    except AssertionError:
        raise InvalidDatatypeException(field, int, type(value))


def assert_datatype_dict(field, value):
    """Assert that the value is of type dict."""
    try:
        assert isinstance(value, dict)
    except AssertionError:
        raise InvalidDatatypeException(field, dict, type(value))


def assert_datatype_list_of_str(field, value):
    """Assert that the value is of type list containing str."""
    try:
        assert isinstance(value, (list, tuple))
        for i, val in enumerate(value):
            try:
                assert isinstance(value, str)
            except AssertionError:
                raise InvalidDatatypeException(
                    '{}[{}]'.format(field, i), str, type(value))
    except AssertionError:
        raise InvalidDatatypeException(field, (list, tuple), type(value))


def assert_datatypes(supplied_fields, datatype_specs):
    """A helper for routing values to their type validators."""
    kwargs = locals()
    for field in supplied_fields:
        spec = datatype_specs[field]
        validator = kwargs['assert_datatype_{}'.format(spec)]
        validator(field, supplied_fields[field])
