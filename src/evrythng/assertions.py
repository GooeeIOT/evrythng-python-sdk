from evrythng.exceptions import (
    ExtraDataSubmittedException,
    InvalidDatatypeException,
    InvalidValueException,
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
            assert field not in readonly_fields or supplied_fields[field] is None
        except AssertionError:
            raise ReadOnlyFieldWrittenToException(field, supplied_fields[field])


def no_extras(supplied_fields, possible_fields):
    """Assert that there are no extra fields in the supplied_fields."""
    for field in supplied_fields:
        try:
            assert field in possible_fields
        except AssertionError:
            raise ExtraDataSubmittedException(field, supplied_fields[field])


def datatype_str(field, value, spec):
    """Assert that the value is of type str."""
    try:
        assert isinstance(value, str)
    except AssertionError:
        raise InvalidDatatypeException(field, str, type(value))


def datatype_time(field, value, spec):
    """Assert that the value is of type int."""
    try:
        assert isinstance(value, int)
    except AssertionError:
        raise InvalidDatatypeException(field, int, type(value))


def datatype_dict(field, value, spec):
    """Assert that the value is of type dict."""
    try:
        assert isinstance(value, dict)
    except AssertionError:
        raise InvalidDatatypeException(field, dict, type(value))

    for i, (k, v) in enumerate(value.items()):
        try:
            assert isinstance(k, str)
        except:
            raise InvalidDatatypeException(
                    '{}[{}].key'.format(field, i), str, type(k))
        try:
            assert isinstance(v, str)
        except:
            raise InvalidDatatypeException(
                    '{}[{}].value'.format(field, i), str, type(v))


def datatype_list_of_str(field, value, spec):
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

    spec = spec.split('|')
    if len(spec) > 1:
        required_values = spec[1].split(',')
        if value not in required_values:
            raise InvalidValueException(
                field, value, ', '.join(required_values))


def datatype_list_of_social_networks(field, value, spec):
    # TODO: figure our how to serialize this.
    return ''


def datatype_birthday(field, value, spec):
    try:
        assert isinstance(value, dict)
    except AssertionError:
        raise InvalidDatatypeException(field, dict, type(value))

    required_keys = ('day', 'month', 'year')

    for key in value:
        if key not in required_keys:
            raise ValueError(
                'Invalid key of {} ... must be one of day|month|year.'.format(
                    key))

        try:
            assert isinstance(value[key], int)
        except AssertionError:
            raise InvalidDatatypeException(
                '{}[{}]'.format(field, key), int, type(value[key]))


def datatypes(supplied_fields, datatype_specs):
    """A helper for routing values to their type validators."""
    for field in supplied_fields:
        value = supplied_fields[field]
        if value is None:
            continue
        spec = datatype_specs[field]
        validator_name = spec.split('|')[0]
        validator = file_locals['datatype_{}'.format(validator_name)]
        validator(field, supplied_fields[field], spec)


file_locals = locals()
