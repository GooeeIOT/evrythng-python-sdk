from evrythng import assertions, utils
from . import validate_field_specs


field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'product': 'ref',
        'location': 'location',
        'identifiers': 'dict_of_dict',
        'properties': 'dict',
        'tags': 'list_of_str',
        'collections': 'ref_list',
        'customFields': 'dict_of_str',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt', 'activatedAt'),
    'writable': ('description', 'product', 'location', 'identifiers',
                 'properties', 'tags', 'collections', 'customFields'),
}


def create_thng(name, description=None, product=None, location=None,
                identifiers=None, properties=None, tags=None, collections=None,
                customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/thngs', data=kwargs, api_key=api_key)


def list_thngs(api_key=None):
    return utils.request('GET', '/thngs', api_key=api_key, accept=True)


def read_thng(thng_id, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}'.format(thng_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def update_thng(thng_id, name, description=None, product=None, location=None,
                identifiers=None, properties=None, tags=None, collections=None,
                customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    thng_id = kwargs.pop('thng_id')
    validate_field_specs(kwargs, field_specs)
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
