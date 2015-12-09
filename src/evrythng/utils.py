import os

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json
import requests


def request(self, request_type, resource_url, data=None,
            api_key=None, return_raw_request=False, accept=False):
    request_type = request_type.lower()

    if api_key is None:
        os.getenv('EVRYTHNG_API_TOKEN')

    request_func = getattr(requests, request_type)
    url = '{}{}'.format(self.base_url, resource_url)
    kwargs = {
        'headers': {'Content-Type': 'application/json'},
    }

    if accept:
        kwargs['headers']['Accept'] = 'application/json'

    if api_key:
        kwargs['Authorization'] = 'Token {}'.format(api_key)

    if data:
        kwargs['json'] = json.dumps(data)

    response = request_func(url, **kwargs)

    if return_raw_request:
        return response

    return response.json()
