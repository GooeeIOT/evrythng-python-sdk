from evrythng import assertions, utils
from . import validate_field_specs


field_specs = {
    'datatypes': {
        'name': 'str',
        'customFields': 'dict_of_str',
        'tags': 'dict_of_str',
        'scopes': 'scopes',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('customFields', 'tags', 'scopes'),
}


def create_action_type(name, customFields=None, tags=None, scopes=None,
                       api_key=None):
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    validate_field_specs(kwargs, field_specs)
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
    validate_field_specs(kwargs, field_specs)
    url = '/actions/{}'.format(type_)
    return utils.request('POST', '/actions', data=kwargs, api_key=api_key)


def list_action_types(type_, api_key=None):
    assertions.datatype_str('type_', type_, None)
    url = '/actions'.format(type_)
    return utils.request('GET', url, api_key=api_key)


def read_action_type(type_, action_id, api_key=None):
    assertions.datatype_str('type_', type_, None)
    assertions.datatype_str('action_id', action_id, None)
    url = '/actions/{}/{}'.format(type_, action_id)
    return utils.request('GET', url, api_key=api_key)
