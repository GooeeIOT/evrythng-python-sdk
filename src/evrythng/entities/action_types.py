from evrythng import assertions, utils
from evrythng.exceptions import RequiredFieldException

'''
datatype_specs = {
    'type': 'str',
    'thng': 'ref',
    'product': 'ref',
    'collection': 'ref',
    'timestamp': 'time',
    'identifiers': 'dict_of_dict',
    'location': 'location',
    'locationSource': 'str',
    'context': 'dict',
    'customFields': 'dict_of_str',
}
required_fields = ('type',)
readonly_fields = ('id', 'user', 'createdAt', 'createdByProject, createdByApp')
writable_fields = ('thng', 'product', 'collection', 'timestamp', 'identifiers',
                   'location', 'locationSource', 'context', 'customFields')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""

    # # Custom rule specified by evrythng.
    # if kwargs['location'] and not kwargs['locationSource']:
    #     raise RequiredFieldException('locationSource')

    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_action_type(type_, thng=None, product=None, collection=None,
                       timestamp=None, identifiers=None, location=None,
                       locationSource=None, context=None, customFields=None,
                       api_key=None):
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    url = '/actions/{}'.format(type_)
    return utils.request('POST', '/actions', data=kwargs, api_key=api_key)


def update_action_type(type_, thng=None, product=None, collection=None,
                       timestamp=None, identifiers=None, location=None,
                       locationSource=None, context=None, customFields=None,
                       api_key=None):
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    url = '/actions/{}'.format(type_)
    return utils.request('POST', '/actions', data=kwargs, api_key=api_key)


def list_action_types(type_, api_key=None):
    url = '/actions'.format(type_)
    return utils.request('GET', url, api_key=api_key)


def read_action_type(type_, action_id, api_key=None):
    url = '/actions/{}/{}'.format(type_, action_id)
    return utils.request('GET', url, api_key=api_key)
'''
