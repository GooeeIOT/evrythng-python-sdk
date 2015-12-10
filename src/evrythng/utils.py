import os

import requests


def request(request_type, resource_url, data=None, api_key=None,
            base_url='https://api.evrythng.com', accept=False, debug=True):
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

    if debug:
        print('---')
        print(request_type.upper(), url)
        if data:
            print('DATA', data)

    response = request_func(url, **kwargs)

    if debug:
        print('RESPONSE', response.text)

    return response
