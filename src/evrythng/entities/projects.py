from evrythng import assertions, utils


datatype_specs = {
    'name': 'str',
    'description': 'str',
    'startsAt': 'time',
    'endsAt': 'time',
    'tags': 'list_of_str',
    'shortDomains': 'list_of_str',
    'customFields': 'dict',
}
required_fields = ('name',)
readonly_fields = ('id', 'createdAt', 'updatedAt')
writable_fields = ('description', 'startsAt', 'endsAt', 'tags', 'shortDomains')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_project(name=None, description=None, startsAt=None, endsAt=None,
                   tags=None, shortDomains=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request(
        'POST', '/projects', data=kwargs, api_key=api_key)


def update_project(project_id, name=None, description=None, startsAt=None,
                   endsAt=None, tags=None, shortDomains=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    _validate_data(kwargs)
    url = '/projects/{}'.format(project_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key, accept=True)


def list_projects(api_key=None):
    return utils.request('GET', '/projects', api_key=api_key, accept=True)


def read_project(project_id, api_key=None):
    url = '/projects/{}'.format(project_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def delete_project(project_id, api_key=None):
    url = '/projects/{}'.format(project_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
