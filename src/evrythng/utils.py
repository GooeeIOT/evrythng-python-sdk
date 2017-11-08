import logging
import os
import sys

from evrythng.exceptions import MissingAPIKeyException

try:
    # Python 3.x
    from urllib.parse import urlencode
except:
    # Python 2.x
    from urlparse import urlparse

import requests


logging.getLogger('requests').setLevel(logging.WARNING)
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
LOG.addHandler(ch)


def request(request_type, resource_url, data=None, api_key=None, files=None,
            base_url=None, accept=False, debug=None,
            query_params=None, pageNumber=None, perPage=None, timeout=30):
    """Send a request to the Evrythng API."""
    if debug is None:
        debug = os.getenv('PYEVT_DEBUG', '0') == '1'

    if base_url is None:
        base_url = os.getenv('PYEVT_BASE_URL', 'https://api.evrythng.com')

    if query_params:
        if type(query_params) != dict:
            raise ValueError('query_params must be a dict mapping keys to values.')
    else:
        query_params = {}

    if not api_key:
        try:
            api_key = os.getenv('EVRYTHNG_API_TOKEN')
        except KeyError:
            raise MissingAPIKeyException

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
        LOG.debug('|'.join((
            'EVTDEBUG',
            request_type.upper(),
            str(response.status_code),
            url,
            str(requests_kwargs),
            response.text,
        )))

    return response
