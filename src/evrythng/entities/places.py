from evrythng import assertions, utils


datatype_specs = {
    'position': 'geojson',
    'address': 'address',
    'description': 'str',
    'icon': 'str',
    'tags': 'list_of_str',
    'customFields': 'dict_of_str',
}
required_fields = ('name',)
readonly_fields = ('id', 'createdAt', 'updatedAt')
writable_fields = ('position', 'address', 'description', 'icon', 'tags',
                   'customFields')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_place(name, position=None, address=None, description=None,
                 icon=None, tags=None, customFields=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request('POST', '/places', data=kwargs)


def read_place(place_id, api_key=None):
    url = '/places/{}'.format(place_id)
    return utils.request('GET', url, api_key=api_key)


def update_place(place_id, name=None, position=None, address=None, description=None,
                 icon=None, tags=None, customFields=None):
    kwargs = locals()
    place_id = kwargs.pop('place_id')
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    url = '/places/{}'.format(place_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


def delete_place(place_id, api_key=None):
    url = '/places/{}'.format(place_id)
    return utils.request('DELETE', url, api_key=api_key)


def list_places(api_key=None):
    return utils.request('GET', '/places', api_key=api_key)
