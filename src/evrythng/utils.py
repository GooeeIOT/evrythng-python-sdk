import os

import requests


def request(request_type, resource_url, data=None, api_key=None,
            base_url='https://api.evrythng.com',
            return_raw_request=False, accept=False):
    request_type = request_type.lower()

    if api_key is None:
        os.getenv('EVRYTHNG_API_TOKEN')

    request_func = getattr(requests, request_type)
    url = '{}{}'.format(base_url, resource_url)
    kwargs = {
        'headers': {'Content-Type': 'application/json'},
    }

    if accept:
        kwargs['headers']['Accept'] = 'application/json'

    if api_key:
        kwargs['headers']['Authorization'] = 'Token {}'.format(api_key)

    if data:
        kwargs['json'] = data

    response = request_func(url, **kwargs)

    if return_raw_request:
        return response

    return response.json()
