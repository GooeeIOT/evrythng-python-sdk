from evrythng import assertions, utils


datatype_specs = {
    'position': 'geojson',
    'timestamp': 'time',
}
required_fields = ('position',)
readonly_fields = tuple()
writable_fields = ('timestamp',)


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def update_location(thng_id, position=None, timestamp=None, api_key=None):
    data = {'position': position, 'timestamp': timestamp}
    _validate_data(data)
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('PUT', url, data=data, api_key=api_key)


# def create_thng(name, description=None, brand=None, categories=None,
#                    photos=None, url=None, identifiers=None, properties=None,
#                    tags=None, customFields=None, api_key=None):
#     kwargs = locals()
#     api_key = kwargs.pop('api_key', None)
#     _validate_data(kwargs)
#     return utils.request('POST', '/thngs', data=kwargs, api_key=api_key)


def list_locations(thng_id, api_key=None):
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('GET', url, api_key=api_key)


# def read_thng(thng_id, api_key=None):
#     url = '/thngs/{}'.format(thng_id)
#     return utils.request('GET', url, api_key=api_key)


def delete_location(thng_id, api_key=None):
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)
