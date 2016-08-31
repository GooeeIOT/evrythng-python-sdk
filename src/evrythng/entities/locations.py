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


def update_location(thng_id, position=None, timestamp=None, api_key=None):
    data = {'position': position, 'timestamp': timestamp}
    assertions.validate_field_specs(data, field_specs)
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('PUT', url, data=data, api_key=api_key)


def list_locations(thng_id, api_key=None, **request_kwargs):
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('GET', url, api_key=api_key, **request_kwargs)


def delete_location(thng_id, api_key=None):
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)
