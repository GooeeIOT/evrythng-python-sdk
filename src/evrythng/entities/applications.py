"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/applications
"""
from evrythng import assertions, utils


field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'project': 'ref',
        'defaultUrl': 'str',
        'socialNetworks': 'list_of_social_networks',
        'tags': 'list_of_str',
        'customFields': 'dict',
        'appApiKey': 'str',
    },
    'required': ('name', 'socialNetworks'),
    'readonly': ('id', 'createdAt', 'updatedAt', 'project', 'appApiKey'),
    'writable': ('description', 'defaultUrl', 'tags', 'customFields'),
}


def create_application(project_id, name, description=None, defaultUrl=None,
                       socialNetworks=None, tags=None, customFields=None,
                       api_key=None):
    """
    Create an Application.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param name: The Name of the Application.
    :type name: str
    :param description: The Description of the Application.
    :type description: str
    :param defaultUrl: The Default URL of the Application.
    :type defaultUrl: str
    :param socialNetworks: Social Networks that the Application supports.
    :type socialNetworks: dict of dicts
    :param tags: The Tags of the Application
    :type tags: list of str
    :param customFields: The Custom Fields of Application.
    :type customFields: dict
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    if socialNetworks is None:
        socialNetworks = {}
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/projects/{}/applications'.format(project_id)
    return utils.request('POST', url, data=kwargs, api_key=api_key)


def update_application(project_id, application_id, name=None, description=None,
                       defaultUrl=None, socialNetworks=None, tags=None,
                       customFields=None, api_key=None):
    """
    Update an Application.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to update the details for.
    :type application_id: str
    :param name: The Name of the Application.
    :type name: str
    :param description: The Description of the Application.
    :type description: str
    :param defaultUrl: The Default URL of the Application.
    :type defaultUrl: str
    :param socialNetworks: Social Networks that the Application supports.
    :type socialNetworks: dict of dicts
    :param tags: The Tags of the Application.
    :type tags: list of str
    :param customFields: The Custom Fields of Application.
    :type customFields: dict
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    application_id = kwargs.pop('application_id')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key, accept=True)


def list_applications(project_id, api_key=None, **request_kwargs):
    """
    List Applications.

    :param project_id: The Project to list the Applications for.
    :type project_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications'.format(project_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def read_application(project_id, application_id, api_key=None):
    """
    Read an Application.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to get the details of.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def read_trusted_application_key(project_id, application_id, api_key=None):
    """
    Read a Trusted Application Key.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to get the Trusted Key for.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}/secretKey'\
        .format(project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def delete_application(project_id, application_id, api_key=None):
    """
    Delete an Application.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to delete.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
