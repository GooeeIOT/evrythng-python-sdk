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
                 icon=None, tags=None, customFields=None, api_key=None,
                 request_kwargs=None):
    kwargs = locals()
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/places', data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def read_place(place, api_key=None, request_kwargs=None):
    assertions.datatype_str('place', place)
    url = '/places/{}'.format(place)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def update_place(place, name=None, position=None, address=None,
                 description=None, icon=None, tags=None, customFields=None,
                 api_key=None, request_kwargs=None):
    kwargs = locals()
    del kwargs['request_kwargs']
    place = kwargs.pop('place')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/places/{}'.format(place)
    return utils.request('PUT', url, data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def delete_place(place, api_key=None, request_kwargs=None):
    assertions.datatype_str('place', place)
    url = '/places/{}'.format(place)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))


def list_places(api_key=None, request_kwargs=None):
    return utils.request('GET', '/places', api_key=api_key,
                         **(request_kwargs or {}))
