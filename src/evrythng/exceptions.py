class ExtraDataSubmittedException(Exception):

    def __init__(self, field_name, value):
        message = '"{}" is not a valid key for the "{}" field.'.format(
            value, field_name)
        super(ExtraDataSubmittedException, self).__init__(message)


class InvalidDatatypeException(Exception):

    def __init__(self, field_name, expected_type, received_type):
        if isinstance(expected_type, tuple):
            expected_type = ' or '.join(
                str(type(expect_type)) for expect_type in expected_type)
        message = '"{}" expects a {} but received a {}'.format(
            field_name, expected_type, received_type)
        super(InvalidDatatypeException, self).__init__(message)


class InvalidValueException(Exception):

    def __init__(self, field_name, value, good_values):
        message = '"{}" has a value of "{}" but need to be one of {}.'.format(
            field_name, value, good_values)
        super(InvalidValueException, self).__init__(message)


class ReadOnlyFieldWrittenToException(Exception):

    def __init__(self, field_name, value):
        message = '"{}" is a read-only field and was written to with "{}"'.format(
            field_name, value)
        super(ReadOnlyFieldWrittenToException, self).__init__(message)


class RequiredFieldException(Exception):

    def __init__(self, field_name):
        message = '"{}" is a required field.'.format(field_name)
        super(RequiredFieldException, self).__init__(message)
