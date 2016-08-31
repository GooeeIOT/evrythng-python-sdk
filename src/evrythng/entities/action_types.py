"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/actiontypes
"""
from evrythng import assertions, utils


field_specs = {
    'datatypes': {
        'name': 'str',
        'customFields': 'dict',
        'tags': 'dict_of_str',
        'scopes': 'dict',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('customFields', 'tags', 'scopes'),
}


def create_action_type(name, customFields=None, tags=None, scopes=None,
                       api_key=None):
    """Create an Action Type"""
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/actions', data=kwargs, api_key=api_key)


def delete_action_type(name, api_key=None):
    """Delete an Action Type"""
    assertions.datatype_str('name', name)
    url = '/actions/{}'.format(name)
    return utils.request('DELETE', url, api_key=api_key)


def update_action_type(name, customFields=None, tags=None, scopes=None,
                       api_key=None):
    """Update an Action Type"""
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/actions/{}'.format(name)
    return utils.request('POST', '/actions', data=kwargs, api_key=api_key)


def list_action_types(api_key=None, **request_kwargs):
    """List Action Types"""
    url = '/actions'
    return utils.request('GET', url, api_key=api_key, **request_kwargs)
