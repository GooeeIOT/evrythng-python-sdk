from evrythng.exceptions import (
    ExtraDataSubmittedException,
    InvalidDatatypeException,
    ReadOnlyFieldWrittenToException,
    RequiredFieldException,
)


def required(supplied_fields, required_fields):
    """Assert that all required fields are in the supplied_fields."""
    for field in required_fields:
        try:
            assert field in supplied_fields
        except AssertionError:
            raise RequiredFieldException(field)


def readonly(supplied_fields, readonly_fields):
    """Assert that a read only field wasn't supplied as a field/value."""
    for field in supplied_fields:
        try:
            assert field not in readonly_fields
        except AssertionError:
            raise ReadOnlyFieldWrittenToException(field, supplied_fields[field])


def no_extras(supplied_fields, possible_fields):
    """Assert that there are no extra fields in the supplied_fields."""
    for field in supplied_fields:
        try:
            assert field in possible_fields
        except AssertionError:
            raise ExtraDataSubmittedException(field, supplied_fields[field])


def datatype_str(field, value):
    """Assert that the value is of type str."""
    try:
        assert isinstance(value, str)
    except AssertionError:
        raise InvalidDatatypeException(field, str, type(value))


def datatype_time(field, value):
    """Assert that the value is of type int."""
    try:
        assert isinstance(value, int)
    except AssertionError:
        raise InvalidDatatypeException(field, int, type(value))


def datatype_dict(field, value):
    """Assert that the value is of type dict."""
    try:
        assert isinstance(value, dict)
    except AssertionError:
        raise InvalidDatatypeException(field, dict, type(value))


def datatype_list_of_str(field, value):
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


def datatypes(supplied_fields, datatype_specs):
    """A helper for routing values to their type validators."""
    for field in supplied_fields:
        value = supplied_fields[field]
        if value is None:
            continue
        spec = datatype_specs[field]
        validator = file_locals['datatype_{}'.format(spec.replace('|', '_of_'))]
        validator(field, supplied_fields[field])

file_locals = locals()
