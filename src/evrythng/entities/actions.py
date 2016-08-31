"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/actions
"""
from evrythng import assertions, utils


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
        'customFields': 'dict',
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
    """Create an Action"""
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/actions/{}'.format(type_)
    return utils.request('POST', url, data=kwargs, api_key=api_key)


def delete_action(type_, action_id, api_key=None):
    """Delete an Action"""
    assertions.datatype_str('type_', type_)
    assertions.datatype_str('action_id', action_id)
    url = '/actions/{}/{}'.format(type_, action_id)
    return utils.request('DELETE', url, api_key=api_key)


def list_actions(type_, api_key=None, **request_kwargs):
    """List Actions"""
    assertions.datatype_str('type_', type_)
    url = '/actions/{}'.format(type_)
    return utils.request('GET', url, api_key=api_key, **request_kwargs)
