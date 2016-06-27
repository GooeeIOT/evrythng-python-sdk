import os
import requests
try:
    # Python 3.x
    from urllib.parse import urlencode
except:
    # Python 2.x
    from urlparse import urlparse


# TODO: Since so much dev is going on, we've made debug=True the default. This
# needs to change, probably soon.
def request(request_type, resource_url, data=None, api_key=None, files=None,
            base_url='https://api.evrythng.com', accept=False, debug=True, custom_query_params=None,
            pageNumber=None, perPage=None, timeout=30):
    """Send a request to the Evrythng API."""
    if custom_query_params:
        if type(custom_query_params) != dict:
            raise ValueError('custom_query_params must be a dict mapping keys to values.')
    else:
        custom_query_params = {}

    if api_key is None:
        try:
            api_key = os.getenv('EVRYTHNG_API_TOKEN')
        except KeyError:
            print('Configure your EVRYTHNG_API_TOKEN environment variable.')

    request_func = getattr(requests, request_type.lower())
    url = '{}{}'.format(base_url, resource_url)
    requests_kwargs = {
        'headers': {},
        'timeout': timeout,
    }

    if data:
        requests_kwargs['json'] = data
        requests_kwargs['headers'] = {'Content-Type': 'application/json'}

    if files:
        requests_kwargs['files'] = files

    if accept:
        requests_kwargs['headers']['Accept'] = 'application/json'

    if api_key:
        requests_kwargs['headers']['Authorization'] = 'Token {}'.format(api_key)

    if data:
        requests_kwargs['json'] = data

    # Add in custom URL parameters.
    if perPage:
        custom_query_params['perPage'] = perPage
    if pageNumber:
        custom_query_params['page'] = pageNumber
    if custom_query_params:
        url += '?{}'.format(urlencode(custom_query_params))

    if debug:
        print('---')
        print(request_type.upper(), url)
        if data:
            print('DATA', data)
        print('REQKWARGS', requests_kwargs)

    response = request_func(url, **requests_kwargs)

    if debug:
        print('RESPONSE', response.status_code, response.text)

    return response
