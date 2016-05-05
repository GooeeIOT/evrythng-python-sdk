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
def request(request_type, resource_url, data=None, api_key=None,
            base_url='https://api.evrythng.com', accept=False, debug=True, query=None, files=None):
    """Send a request to the API"""
    request_type = request_type.lower()

    if api_key is None:
        try:
            api_key = os.getenv('EVRYTHNG_API_TOKEN')
        except KeyError:
            print("Configure your EVRYTHNG_API_TOKEN environment variable")

    request_func = getattr(requests, request_type)
    url = '{}{}'.format(base_url, resource_url)
    kwargs = {'headers': {}}

    if data:
        kwargs['json'] = data
        kwargs['headers'] = {'Content-Type': 'application/json'}

    if files:
        kwargs['files'] = files

    if accept:
        kwargs['headers']['Accept'] = 'application/json'

    if api_key:
        kwargs['headers']['Authorization'] = 'Token {}'.format(api_key)

    if query:
        url += '?{}'.format(urlencode(query))

    if debug:
        print('---')
        print(request_type.upper(), url)
        if data:
            print('DATA', data)

    response = request_func(url, **kwargs)

    if debug:
        print('RESPONSE', response.status_code, response.text)

    return response
