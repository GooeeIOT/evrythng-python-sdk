from evrythng import assertions, utils


datatype_specs = {
    'email': 'str',
    'firstName': 'str',
    'lastName': 'str',
    'password': 'str',
    'birthday': 'birthday',
    'gender': 'str|male,female',  # male|female
    'timezone': 'str',
    'locale': 'str',
    'photo': 'base64',
    'customFields': 'dict',
    'tags': 'list_of_str',
}
required_fields = ('email',)
readonly_fields = tuple()
writable_fields = ('firstName', 'lastName', 'password', 'birthday', 'gender',
                   'timezone', 'locale', 'photo', 'customFields', 'tags')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_user(email, firstName=None, lastName=None, password=None,
                birthday=None, gender=None, timezone=None, locale=None,
                photo=None, customFields=None, tags=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request(
        'POST', '/auth/evrythng/users', data=kwargs, api_key=api_key)


def activate_user(user_id, activationCode, api_key=None):
    url = '/auth/evrythng/users/{}/validate'.format(user_id)
    data = {'activationCode': activationCode}
    return utils.request('POST', url, data=data, api_key=api_key)


def create_anonymous_user(api_key=None):
    return utils.request(
        'POST', '/auth/evrythng/users?anonymous=true', api_key=api_key)


def authenticate_user(email, password, api_key=None):
    """
    Bad HTTP response status meaning:
        401 = Wrong password.
        403 = User status is not 'active'.
        404 = User not found.
    """
    data = {'email': email, 'password': password}
    return utils.request('POST', '/auth/evrythng', data=data, api_key=api_key)


def authenticate_facebook_user(expires, token, api_key=None):
    data = {
        'access': {
            'expires': expires,
            'token': token,
        }
    }
    return utils.request('POST', '/auth/facebook', data=data, api_key=api_key)


def logout_user(api_key=None):
    return utils.request('POST', '/auth/all/logout', api_key=api_key)


def list_users(project_id, api_key=None):
    return utils.request('GET', '/users', api_key=api_key)


def read_user(user_id, api_key=None):
    url = '/users/{}'.format(user_id)
    return utils.request('GET', url, api_key=api_key)


def update_user(user_id, email=None, firstName=None, lastName=None,
                password=None, birthday=None, gender=None, timezone=None,
                localte=None, photo=None, customFields=None, tags=None,
                api_key=None):
    kwargs = locals()
    user_id = kwargs.pop('user_id')
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    url = '/users/{}'.format(user_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)
