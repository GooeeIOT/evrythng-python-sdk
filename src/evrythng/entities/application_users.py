"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/appusers
"""
from evrythng import assertions, utils

field_specs = {
    'datatypes': {
        'email': 'str',
        'firstName': 'str',
        'lastName': 'str',
        'password': 'str',
        'birthday': 'birthday',
        'gender': 'gender',
        'timezone': 'str',
        'locale': 'str',
        'photo': 'base64',
        'customFields': 'dict',
        'tags': 'list_of_str',
    },
    'required': ('email',),
    'readonly': tuple(),
    'writable': ('firstName', 'lastName', 'password', 'birthday', 'gender',
                 'timezone', 'locale', 'photo', 'customFields', 'tags'),
}


def create_user(email, firstName=None, lastName=None, password=None,
                birthday=None, gender=None, timezone=None, locale=None,
                photo=None, customFields=None, tags=None, api_key=None,
                request_kwargs=None):
    """Create an Application User."""
    kwargs = locals()
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request(
        'POST', '/auth/evrythng/users', data=kwargs, api_key=api_key,
        **(request_kwargs or {}))


def activate_user(user, activationCode, api_key=None, request_kwargs=None):
    """Activate an Application User."""
    assertions.datatype_str('user', user)
    assertions.datatype_str('activationCode', activationCode)
    url = '/auth/evrythng/users/{}/validate'.format(user)
    data = {'activationCode': activationCode}
    return utils.request('POST', url, data=data, api_key=api_key,
                         **(request_kwargs or {}))


def create_anonymous_user(api_key=None, request_kwargs=None):
    """Create an Anonymous Application User."""
    return utils.request(
        'POST', '/auth/evrythng/users?anonymous=true', api_key=api_key,
        **(request_kwargs or {}))


def authenticate_user(email, password, api_key=None, request_kwargs=None):
    """
    Bad HTTP response status meaning:
        401 = Wrong password.
        403 = User status is not 'active'.
        404 = User not found.
    """
    assertions.datatype_str('email', email)
    assertions.datatype_str('password', password)
    data = {'email': email, 'password': password}
    return utils.request('POST', '/auth/evrythng', data=data, api_key=api_key,
                         **(request_kwargs or {}))


def authenticate_facebook_user(expires, token, api_key=None,
                               request_kwargs=None):
    """Authenticate a Facebook User."""
    assertions.datatype_str('token', token)
    data = {
        'access': {
            'expires': expires,
            'token': token,
        }
    }
    return utils.request('POST', '/auth/facebook', data=data, api_key=api_key,
                         **(request_kwargs or {}))


def delete_user(user, api_key=None, request_kwargs=None):
    """Delete a User."""
    assertions.datatype_str('user', user)
    url = '/users/{}'.format(user)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))


def logout_user(api_key=None, request_kwargs=None):
    """Logout an Application User."""
    return utils.request('POST', '/auth/all/logout', api_key=api_key,
                         **(request_kwargs or {}))


def login_user(email, password, app_api_key, request_kwargs=None):
    """Login an Application User."""
    kwargs = locals()
    del kwargs['request_kwargs']
    app_api_key = kwargs.pop('app_api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/auth/evrythng', data=kwargs,
                         api_key=app_api_key, **(request_kwargs or {}))


def list_users(project_id, api_key=None, request_kwargs=None):
    """List Application Users."""
    assertions.datatype_str('project_id', project_id)
    return utils.request('GET', '/users', api_key=api_key,
                         **(request_kwargs or {}))


def read_user(user, api_key=None, request_kwargs=None):
    """Read an Application User."""
    assertions.datatype_str('user', user)
    url = '/users/{}'.format(user)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def update_user(user, email=None, firstName=None, lastName=None,
                password=None, birthday=None, gender=None, timezone=None,
                locale=None, photo=None, customFields=None, tags=None,
                api_key=None, request_kwargs=None):
    """Update an Application User."""
    kwargs = locals()
    del kwargs['request_kwargs']
    user = kwargs.pop('user')
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/users/{}'.format(user)
    return utils.request('PUT', url, data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))
