from evrythng import utils
from . import validate_field_specs


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
    validate_field_specs(data, field_specs)
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('PUT', url, data=data, api_key=api_key)


def list_locations(thng_id, api_key=None):
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('GET', url, api_key=api_key)


def delete_location(thng_id, api_key=None):
    url = '/thngs/{}/location'.format(thng_id)
    return utils.request('DELETE', url, api_key=api_key)
