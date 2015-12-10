from evrythng import assertions, utils


datatype_specs = {
    'name': 'str',
    'description': 'str',
    'product': 'ref',
    'location': 'list_of_str',
    'identifiers': 'dict_of_dict',
    'properties': 'dict',
    'tags': 'list_of_str',
    'collections': 'ref_list',
    'customFields': 'dict',
}
required_fields = ('name',)
readonly_fields = ('id', 'createdAt', 'updatedAt', 'activatedAt')
writable_fields = ('description', 'product', 'location', 'identifiers',
                   'properties', 'tags', 'collections', 'customFields')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_thng(name, description=None, product=None, location=None,
                identifiers=None, properties=None, tags=None, collections=None,
                customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request('POST', '/thngs', data=kwargs, api_key=api_key)


def list_thngs(api_key=None):
    return utils.request('GET', '/thngs', api_key=api_key, accept=True)


def read_thng(thng_id, api_key=None):
    url = '/thngs/{}'.format(thng_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def update_thng(thng_id, name, description=None, product=None, location=None,
                identifiers=None, properties=None, tags=None, collections=None,
                customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    thng_id = kwargs.pop('thng_id')
    _validate_data(kwargs)
    url = '/thngs/{}'.format(thng_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key)


def delete_thng(thng_id, api_key=None):
    url = '/thngs/{}'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)


def create_device_thng(thngId, thngApiKey, api_key=None):
    data = {'thngId': thngId, 'thngApiKey': thngApiKey}
    return utils.request(
        'POST', '/auth/evrythng/thngs', data=data, api_key=api_key)


def read_device_thng(thng_id, api_key=None):
    url = '/auth/evrythng/thngs/{}'.format(thng_id)
    return utils.request('GET', url, api_key=api_key)


def delete_device_thng(thng_id, api_key=None):
    url = '/auth/evrythng/thngs/{}'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)
