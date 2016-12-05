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


def create_thng_action(type_, thng, timestamp=None, identifiers=None, location=None,
                       locationSource=None, context=None, customFields=None, api_key=None):
    """Create an Action for a Thng"""
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, action_field_specs)

    url = '/thngs/{}/actions/{}'.format(thng, type_)

    return utils.request('POST', url, data=kwargs, api_key=api_key)


def create_thng(name, description=None, product=None, location=None,
                identifiers=None, properties=None, tags=None, collections=None,
                customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/thngs', data=kwargs, api_key=api_key)


def list_thngs(api_key=None, **request_kwargs):
    return utils.request('GET', '/thngs', api_key=api_key, accept=True, **request_kwargs)


def read_thng(thng_id, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}'.format(thng_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def update_thng(thng_id, name=None, description=None, product=None,
                location=None, identifiers=None, properties=None, tags=None,
                collections=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    thng_id = kwargs.pop('thng_id')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/thngs/{}'.format(thng_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key)


def delete_thng(thng_id, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)


def create_device_thng(thng_id, thngApiKey, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    assertions.datatype_str('thngApiKey', thngApiKey)
    data = {'thng_id': thng_id, 'thngApiKey': thngApiKey}
    return utils.request(
        'POST', '/auth/evrythng/thngs', data=data, api_key=api_key)


def read_device_thng(thng_id, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    url = '/auth/evrythng/thngs/{}'.format(thng_id)
    return utils.request('GET', url, api_key=api_key)


def delete_device_thng(thng_id, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    url = '/auth/evrythng/thngs/{}'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)
