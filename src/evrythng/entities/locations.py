"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/locations
"""
from evrythng import assertions, utils

field_specs = {
    'datatypes': {
        'position': 'geojson',
        'timestamp': 'time',
    },
    'required': ('position',),
    'readonly': tuple(),
    'writable': ('timestamp',),
}


def update_location(thng, position=None, timestamp=None, api_key=None,
                    request_kwargs=None):
    data = {'position': position, 'timestamp': timestamp}
    assertions.validate_field_specs(data, field_specs)
    url = '/thngs/{}/location'.format(thng)
    return utils.request('PUT', url, data=data, api_key=api_key,
                         **(request_kwargs or {}))


def list_locations(thng, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    url = '/thngs/{}/location'.format(thng)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def delete_location(thng, api_key=None, request_kwargs=None):
    assertions.datatype_str('thng', thng)
    url = '/thngs/{}/location'.format(thng)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))
