from evrythng import utils
from . import validate_field_specs


field_specs = {
    'datatypes': {
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
    },
    'required': ('type',),
    'readonly': ('id', 'user', 'createdAt', 'createdByProject, createdByApp'),
    'writable': ('thng', 'product', 'collection', 'timestamp', 'identifiers',
                 'location', 'locationSource', 'context', 'customFields'),
}


def create_action(type_, thng=None, product=None, collection=None,
                  timestamp=None, identifiers=None, location=None,
                  locationSource=None, context=None, customFields=None,
                  api_key=None):
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    validate_field_specs(kwargs, field_specs)
    url = '/actions/{}'.format(type_)
    return utils.request('POST', '/actions', data=kwargs, api_key=api_key)


def list_actions(type_, api_key=None):
    url = '/actions/{}'.format(type_)
    return utils.request('GET', url, api_key=api_key)


def read_action(type_, action_id, api_key=None):
    url = '/actions/{}/{}'.format(type_, action_id)
    return utils.request('GET', url, api_key=api_key)
