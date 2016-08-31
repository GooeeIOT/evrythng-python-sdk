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
                photo=None, customFields=None, tags=None, api_key=None):
    """Create an Application User."""
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request(
        'POST', '/auth/evrythng/users', data=kwargs, api_key=api_key)


def activate_user(user_id, activationCode, api_key=None):
    """Activate an Application User."""
    assertions.datatype_str('user_id', user_id)
    assertions.datatype_str('activationCode', activationCode)
    url = '/auth/evrythng/users/{}/validate'.format(user_id)
    data = {'activationCode': activationCode}
    return utils.request('POST', url, data=data, api_key=api_key)


def create_anonymous_user(api_key=None):
    """Create an Anonymous Application User."""
    return utils.request(
        'POST', '/auth/evrythng/users?anonymous=true', api_key=api_key)


def authenticate_user(email, password, api_key=None):
    """
    Bad HTTP response status meaning:
        401 = Wrong password.
        403 = User status is not 'active'.
        404 = User not found.
    """
    assertions.datatype_str('email', email)
    assertions.datatype_str('password', password)
    data = {'email': email, 'password': password}
    return utils.request('POST', '/auth/evrythng', data=data, api_key=api_key)


def authenticate_facebook_user(expires, token, api_key=None):
    """Authenticate a Facebook User."""
    assertions.datatype_str('token', token)
    data = {
        'access': {
            'expires': expires,
            'token': token,
        }
    }
    return utils.request('POST', '/auth/facebook', data=data, api_key=api_key)


def delete_user(user_id, api_key=None):
    """Delete a User."""
    assertions.datatype_str('user_id', user_id)
    url = '/users/{}'.format(user_id)
    return utils.request('DELETE', url, api_key=api_key)


def logout_user(api_key=None):
    """Logout an Application User."""
    return utils.request('POST', '/auth/all/logout', api_key=api_key)


def login_user(email, password, app_api_key):
    """Login an Application User."""
    kwargs = locals()
    app_api_key = kwargs.pop('app_api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/auth/evrythng', data=kwargs, api_key=app_api_key)


def list_users(project_id, api_key=None, **request_kwargs):
    """List Application Users."""
    assertions.datatype_str('project_id', project_id)
    return utils.request('GET', '/users', api_key=api_key, **request_kwargs)


def read_user(user_id, api_key=None):
    """Read an Application User."""
    assertions.datatype_str('user_id', user_id)
    url = '/users/{}'.format(user_id)
    return utils.request('GET', url, api_key=api_key)


def update_user(user_id, email=None, firstName=None, lastName=None,
                password=None, birthday=None, gender=None, timezone=None,
                locale=None, photo=None, customFields=None, tags=None,
                api_key=None):
    """Update an Application User."""
    kwargs = locals()
    user_id = kwargs.pop('user_id')
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/users/{}'.format(user_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)
