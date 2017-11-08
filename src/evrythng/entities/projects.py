"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/projects
"""
import logging

from evrythng import assertions, utils

field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'startsAt': 'time',
        'endsAt': 'time',
        'tags': 'list_of_str',
        'shortDomains': 'list_of_str',
        'customFields': 'dict',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('description', 'startsAt', 'endsAt', 'tags', 'shortDomains',
                 'customFields'),
}

logger = logging.getLogger(__name__)


def create_project(name, description=None, startsAt=None, endsAt=None,
                   tags=None, shortDomains=None, customFields=None,
                   api_key=None, request_kwargs=None):
    """
    Create a new Project.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param startsAt:
    :type startsAt: int
    :param endsAt:
    :type endsAt: int
    :param tags:
    :type tags: list of str
    :param shortDomains:
    :type shortDomains: list of str
    :param api_key:
    :type api_key: str
    :return A Project document.
    :rtype Response
    """
    kwargs = locals()
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    logger.debug('Creating Project...')
    return utils.request('POST', '/projects', data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def update_project(project, name=None, description=None, startsAt=None,
                   endsAt=None, tags=None, shortDomains=None,
                   customFields=None, api_key=None, request_kwargs=None):
    """
    Update an existing Project.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param startsAt:
    :type startsAt: int
    :param endsAt:
    :type endsAt: int
    :param tags:
    :type tags: list of str
    :param shortDomains:
    :type shortDomains: list of str
    :param api_key:
    :type api_key: str
    :return A Project document.
    :rtype Response
    """
    kwargs = locals()
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    project = kwargs.pop('project')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/projects/{}'.format(project)
    logger.debug('Updating Project {}...'.format(project))
    return utils.request('PUT', url, data=kwargs, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def list_projects(api_key=None, request_kwargs=None):
    """
    List Projects.

    :param api_key: The API key to authorize the request against.
    :type api_key: str
    :return A list of Project documents.
    :rtype Response
    """
    logger.debug('Listing Projects...')
    return utils.request('GET', '/projects', api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def read_project(project, api_key=None, request_kwargs=None):
    """
    Read a Project.

    :param project: The ID of the Project entity.
    :type project: str
    :param api_key: The API key to authorize the request against.
    :type api_key: str
    :return A Project document.
    :rtype Response
    """
    assertions.datatype_str('project', project)
    url = '/projects/{}'.format(project)
    logger.debug('Reading Project {}'.format(project))
    return utils.request('GET', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def delete_project(project, api_key=None, request_kwargs=None):
    """
    Delete a Project.

    :param project: The ID of the Project entity.
    :type project: str
    :param api_key: The API key to authorize the request against.
    :type api_key: str
    :return Blank string.
    :rtype Response
    """
    assertions.datatype_str('project', project)
    url = '/projects/{}'.format(project)
    logger.debug('Deleting Project {}'.format(project))
    return utils.request('DELETE', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def delete_all_projects(api_key=None, request_kwargs=None):
    """
    Delete all Projects.

    WARNING: This will recursively delete most underlying relationships.

    :param api_key: The API key to authorize the request against.
    :type api_key: str
    """
    for project in list_projects(api_key=api_key).json():
        delete_project(project['id'], api_key=api_key, **(request_kwargs or {}))
