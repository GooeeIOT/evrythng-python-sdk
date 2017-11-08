"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/thngs
"""
from evrythng import assertions, utils
from evrythng.entities.actions import field_specs as action_field_specs

field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'product': 'ref',
        'location': 'location',
        'identifiers': 'dict_of_dict',
        'properties': 'dict',
        'tags': 'list_of_str',
        'collections': 'list_of_str',
        'customFields': 'dict',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt', 'activatedAt'),
    'writable': ('description', 'product', 'location', 'identifiers',
                 'properties', 'tags', 'collections', 'customFields'),
}


def create_thng_action(type_, thng, timestamp=None, identifiers=None,
                       location=None, locationSource=None, context=None,
                       customFields=None, api_key=None, request_kwargs=None):
    """Create an Action for a Thng."""
    kwargs = locals()
    del kwargs['request_kwargs']
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, action_field_specs)
    url = '/thngs/{}/actions/{}'.format(thng, type_)
    return utils.request('POST', url, data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def read_thng_actions(thng, type_, api_key=None, request_kwargs=None):
    """Read Actions for a Thng."""
    assertions.datatype_str('thng', thng)
    assertions.datatype_str('type_', type_)
    url = '/thngs/{}/actions/{}'.format(thng, type_)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def create_thng(name, description=None, product=None, location=None,
                identifiers=None, properties=None, tags=None, collections=None,
                customFields=None, api_key=None, request_kwargs=None):
    kwargs = locals()
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/thngs', data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def list_thngs(api_key=None, request_kwargs=None):
    return utils.request('GET', '/thngs', api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def read_thng(thng, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    url = '/thngs/{}'.format(thng)
    return utils.request('GET', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def update_thng(thng, name=None, description=None, product=None,
                location=None, identifiers=None, properties=None, tags=None,
                collections=None, customFields=None, api_key=None,
                request_kwargs=None):
    kwargs = locals()
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    thng = kwargs.pop('thng')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/thngs/{}'.format(thng)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key, **(request_kwargs or {}))


def delete_thng(thng, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    url = '/thngs/{}'.format(thng)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))


def create_device_thng(thng, thngApiKey, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    assertions.datatype_str('thngApiKey', thngApiKey)
    data = {'thng': thng, 'thngApiKey': thngApiKey}
    return utils.request(
        'POST', '/auth/evrythng/thngs', data=data, api_key=api_key,
        **(request_kwargs or {}))


def read_device_thng(thng, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    url = '/auth/evrythng/thngs/{}'.format(thng)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def delete_device_thng(thng, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    url = '/auth/evrythng/thngs/{}'.format(thng)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))
