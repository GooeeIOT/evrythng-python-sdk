import json

from evrythng.exceptions import (
    ExtraDataSubmittedException,
    InvalidDatatypeException,
    InvalidValueException,
    ReadOnlyFieldWrittenToException,
    RequiredFieldException,
)


def validate_field_specs(fields, field_specs):
    """Sanity checking of data that is submitted to evrythng."""
    required(fields, field_specs['required'])
    readonly(fields, field_specs['readonly'])
    no_extras(
        fields,
        field_specs['required'] + field_specs['writable'] +
            field_specs['readonly']
    )
    datatypes(fields, field_specs['datatypes'])


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
            assert field not in readonly_fields \
                   or supplied_fields[field] is None
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


def datatype_dict_of_str(field, value):
    """Assert that the value is a dict of str's."""
    datatype_dict(field, value)
    for k, v in value.items():
        try:
            assert isinstance(k, str)
        except:
            raise InvalidDatatypeException(
                    '{}[{}]'.format(field, k), str, type(k))
        try:
            assert isinstance(v, str)
        except:
            raise InvalidDatatypeException(
                    '{}[{}].value'.format(field, k), str, type(v))


def datatype_list_of_str(field, value):
    """Assert that the value is of type list containing str."""
    try:
        assert isinstance(value, (list, tuple))
        for i, val in enumerate(value):
            try:
                assert isinstance(val, str)
            except AssertionError:
                raise InvalidDatatypeException(
                    '{}[{}]'.format(field, i), str, type(val))
    except AssertionError:
        raise InvalidDatatypeException(field, (list, tuple), type(value))


def datatype_gender(field, value):
    valid_values = ('male', 'female')
    if value not in valid_values:
        raise InvalidValueException(field, value, ', '.join(valid_values))


def datatype_list_of_social_networks(field, value):
    # TODO: figure our how to serialize this.
    return ''


def datatype_birthday(field, value):
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

        keyval = value[key]

        if key == 'month' and not (1 <= keyval <= 12):
            raise InvalidValueException(
                '{}[{}]'.format(field, key), keyval, '1-12')
        elif key == 'day' and not (1 <= keyval <= 31):
            raise InvalidValueException(
                '{}[{}]'.format(field, key), keyval, '1-31')
        elif key == 'year' and not (1800 <= keyval <= 2100):
            raise InvalidValueException(
                '{}[{}]'.format(field, key), keyval, '1800-2100')


def datatype_location(field, value):
    datatype_dict(field, value)
    try:
        assert 'position' in value
    except AssertionError:
        raise RequiredFieldException('position')

    try:
        assert 'type' in value['position']
    except AssertionError:
        raise RequiredFieldException('position[type]')

    try:
        assert value['position']['type'] == 'Point'
    except AssertionError:
        raise RequiredFieldException('position[type] != Point')

    try:
        assert 'coordinates' in value['position']
    except AssertionError:
        raise RequiredFieldException('position[coordinates]')

    coordinates = value['position']['coordinates']

    try:
        assert len(coordinates) == 2
    except AssertionError:
        raise ValueError(
            'location[position][coordinates] must be an array of 2 floats: '
            '[float, float]')


def datatype_address(field, value):
    valid_keys = (
        'extension',
        'street',
        'postalCode',
        'city',
        'county',
        'state',
        'country',
        'countryCode',
        'district',
        'buildingName',
        'buildingFloor',
        'buildingRoom',
        'buildingZone',
        'crossing1',
        'crossing2',
    )

    if not isinstance(value, dict):
        raise InvalidDatatypeException(field, dict, type(value))

    # Make sure the user didn't submit an unexpected key.
    for key in value:
        if key not in valid_keys:
            raise ExtraDataSubmittedException(field, key)

    # Make sure all values are str.
    for k, v in value.items():
        if v is not None and not isinstance(v, str):
            raise InvalidDatatypeException('{}[{}]'.format(
                field, v), str, type(v))


def datatype_geojson(field, value):
    pass


def datatype_ref(field, value):
    # TODO: does this need to be more strict?
    # import re
    # uuid4hex = re.compile('[0-9a-f]{32}\Z', re.I)
    # try:
    #     assert uuid4hex.match(value)
    # except:
    #     raise InvalidValueException(field, value, 'UUID')
    datatype_str(field, value)


def datatype_number(field, value):
    """Assert that the value is a number (int or float)."""
    try:
        float(value)
    except (TypeError, ValueError):
        raise InvalidDatatypeException(field, (int, float), type(value))


def datatype_bool(field, value):
    try:
        assert isinstance(value, bool)
    except AssertionError:
        raise InvalidDatatypeException(field, bool, type(value))


def datatype_json(field, value):
    """
    Evrythng parses the value into its native JSON datatype, so the
    value must be JSONifiable.
    """
    try:
        json.dumps(value)
    except (ValueError, TypeError):
        raise InvalidDatatypeException(field, json, type(value))


def datatype_enum(field, value, *extra):
    """Make sure the value is one of a few specific choices."""
    possible = extra[0].split(',')
    if value not in possible:
        raise InvalidValueException(field, value, possible)


def datatype_not_implemented(field, value):
    """A datatype was not yet implemented or decided upon."""
    pass


def datatypes(supplied_fields, datatype_specs):
    """A helper for routing values to their type validators."""
    for field in supplied_fields:
        value = supplied_fields[field]
        if value is None:
            continue
        spec = datatype_specs[field]
        split = spec.split('|')
        validator_name = split[0]
        validator = file_locals['datatype_{}'.format(validator_name)]
        extra = split[1:] if (len(split) > 1) else None
        if extra:
            validator(field, supplied_fields[field], *extra)
        else:
            validator(field, supplied_fields[field])


file_locals = locals()
