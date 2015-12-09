class ExtraDataSubmittedException(Exception):

    def __init__(self, field_name, value):
        message = '"{}" is a read-only field and was written to: {}'.format(
            field_name, value)
        super(ExtraDataSubmittedException, self).__init__(message)


class InvalidDatatypeException(Exception):

    def __init__(self, field_name, expected_type, received_type):
        message = '"{}" expects a {} but recieved a {}'.format(
            field_name, )
        super(InvalidDatatypeException, self).__init__(message)


class ReadOnlyFieldWrittenToException(Exception):

    def __init__(self, field_name, value):
        message = '"{}" is a read-only field and was written to: {}'.format(
            field_name, value)
        super(ReadOnlyFieldWrittenToException, self).__init__(message)


class RequiredFieldException(Exception):

    def __init__(self, field_name):
        message = '"{}" is a required field.'.format(field_name)
        super(RequiredFieldException, self).__init__(message)
