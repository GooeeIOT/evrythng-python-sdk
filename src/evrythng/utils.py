import os
import requests
try:
    # Python 3.x
    from urllib.parse import urlencode
except:
    # Python 2.x
    from urlparse import urlparse


def request(request_type, resource_url, data=None, api_key=None, files=None,
            base_url='https://api.evrythng.com', accept=False, debug=None,
            query_params=None, pageNumber=None, perPage=None, timeout=30):
    """Send a request to the Evrythng API."""
    if debug is None:
        debug = os.getenv('PYEVT_DEBUG', '0') == '1'

    if query_params:
        if type(query_params) != dict:
            raise ValueError('query_params must be a dict mapping keys to values.')
    else:
        query_params = {}

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
        query_params['perPage'] = perPage
    if pageNumber:
        query_params['page'] = pageNumber

    if query_params:
        url += '?{}'.format(urlencode(query_params))

    response = request_func(url, **requests_kwargs)

    if debug:
        print('|'.join((
            'EVTDEBUG',
            request_type.upper(),
            str(response.status_code),
            url,
            str(requests_kwargs),
            response.text,
        )))

    return response
