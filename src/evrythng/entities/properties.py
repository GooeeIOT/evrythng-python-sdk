from evrythng import assertions, utils


datatype_specs = {
    'key': 'str',
    'value': 'str',
}
required_fields = ('key', 'value')
readonly_fields = ('id', 'createdAt', 'updatedAt', 'activatedAt')
writable_fields = ('description', 'brand', 'categories', 'photos', 'url',
                   'identifiers', 'properties', 'tags', 'customFields')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_property(name, description=None, brand=None, categories=None,
                   photos=None, url=None, identifiers=None, properties=None,
                   tags=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request('POST', '/properties', data=kwargs, api_key=api_key)


def list_properties(api_key=None):
    return utils.request('GET', '/properties', api_key=api_key)


def read_property(property_id, api_key=None):
    url = '/properties/{}'.format(property_id)
    return utils.request('GET', url, api_key=api_key)


def update_property(property_id, name, description=None, brand=None,
                   categories=None, photos=None, url=None, identifiers=None,
                   properties=None, tags=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    property_id = kwargs.pop('property_id')
    _validate_data(kwargs)
    url = '/properties/{}'.format(property_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key)


def delete_property(property_id, api_key=None):
    url = '/properties/{}'.format(property_id)
    return utils.request('DELETE', url, api_key=api_key)
