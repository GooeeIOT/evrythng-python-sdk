from evrythng import assertions, utils


datatype_specs = {
    'name': 'str',
    'description': 'str',
    'project': 'ref',
    'defaultUrl': 'str',
    'socialNetworks': 'list|social_networks',
    'tags': 'list|str',
    'customFields': 'dict',
    'appApiKey': 'str',
}
required_fields = ('name', 'socialNetworks')
readonly_fields = ('id', 'createdAt', 'updatedAt', 'project', 'appApiKey')
writable_fields = ('description', 'defaultUrl', 'tags', 'customFields')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_application(project_id, name=None, description=None,
                       defaultUrl=None, socialNetworks=None, tags=None,
                       customFields=None, appApiKey=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    _validate_data(kwargs)
    url = '/projects/{}/applications'.format(project_id)
    return utils.request('POST', url, data=kwargs, api_key=api_key)


def update_application(project_id, application_id, name=None, description=None,
                       defaultUrl=None, socialNetworks=None, tags=None,
                       customFields=None, appApiKey=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    application_id = kwargs.pop('application_id')
    _validate_data(kwargs)
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key, accept=True)


def list_applications(project_id, api_key=None):
    url = '/projects/{}/applications'.format(project_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def read_application(project_id, application_id, api_key=None):
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def delete_application(project_id, application_id, api_key=None):
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
