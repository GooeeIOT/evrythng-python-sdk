"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/places
"""
from evrythng import assertions, utils


field_specs = {
    'datatypes': {
        'name': 'str',
        'position': 'geojson',
        'address': 'address',
        'description': 'str',
        'icon': 'str',
        'tags': 'list_of_str',
        'customFields': 'dict',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('position', 'address', 'description', 'icon', 'tags',
                 'customFields'),
}


def create_place(name, position=None, address=None, description=None,
                 icon=None, tags=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/places', data=kwargs, api_key=api_key)


def read_place(place_id, api_key=None):
    assertions.datatype_str('place_id', place_id)
    url = '/places/{}'.format(place_id)
    return utils.request('GET', url, api_key=api_key)


def update_place(place_id, name=None, position=None, address=None,
                 description=None, icon=None, tags=None, customFields=None,
                 api_key=None):
    kwargs = locals()
    place_id = kwargs.pop('place_id')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/places/{}'.format(place_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


def delete_place(place_id, api_key=None):
    assertions.datatype_str('place_id', place_id)
    url = '/places/{}'.format(place_id)
    return utils.request('DELETE', url, api_key=api_key)


def list_places(api_key=None, **request_kwargs):
    return utils.request('GET', '/places', api_key=api_key, **request_kwargs)
