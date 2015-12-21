"""
:Example:

>>> api_key = 'your-api-key'
>>> response = create_project(
...     name='Project 1',
...     description='My Project',
...     api_key=api_key
... )
>>> print(response)
<Response [201]>
>>> print(response.json())
{"id":"UgDHtdm2se5RpbXRfnfC9a9h",
 "createdAt":1449849752918,
 "updatedAt":1449849752918,
 "name":"Project 1",
 "description":"My Project",
 "shortDomains":["tn.gg"]}
>>> project_id = response.json()['id']
>>> response = list_projects(api_key=api_key)
>>> print(response)
<Response [200]>
>>> print(response.json())
[
    {"id":"UgDHtdm2se5RpbXRfnfC9a9h",
     "name": "Project 1",
     "createdAt":1449849752918,
     "updatedAt":1449849752918,
     "name":"Project 1",
     "description":"My Project",
     "shortDomains":["tn.gg"]},
 ]
>>> response = read_project(project_id, api_key=api_key)
>>> print(response)
<Response [200]>
>>> print(response.json())
{"id":"UgDHtdm2se5RpbXRfnfC9a9h",
 "createdAt":1449849752918,
 "updatedAt":1449849752918,
 "name":"Project 1",
 "description":"My Project",
 "shortDomains":["tn.gg"]}
>>> response = update_project(project_id, name='Project 1 EDIT',
...     api_key=api_key)
>>> print(response)
<Response [200]>
>>> print(response.json())
{"id":"UgDHtdm2se5RpbXRfnfC9a9h",
 "createdAt":1449849752918,
 "updatedAt":1449849752918,
 "name":"Project 1 EDIT",
 "description":"My Project",
 "shortDomains":["tn.gg"]}
>>> response = delete_project(project_id, api_key=api_key)
>>> print(response)
<Response [200]>
"""

from evrythng import assertions, utils


__all__ = [
    'create_project',
    'update_project',
    'list_projects',
    'read_project',
    'delete_project',
]

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


def create_project(name, description=None, startsAt=None, endsAt=None,
                   tags=None, shortDomains=None, customFields=None,
                   api_key=None):
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
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/projects', data=kwargs, api_key=api_key)


def update_project(project_id, name=None, description=None, startsAt=None,
                   endsAt=None, tags=None, shortDomains=None,
                   customFields=None, api_key=None):
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
    api_key = kwargs.pop('api_key')
    project_id = kwargs.pop('project_id')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/projects/{}'.format(project_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key, accept=True)


def list_projects(api_key=None):
    """
    List Projects.

    :param api_key: The API key to authorize the request against.
    :type api_key: str
    :return A list of Project documents.
    :rtype Response
    """
    return utils.request('GET', '/projects', api_key=api_key, accept=True)


def read_project(project_id, api_key=None):
    """
    Read a Project.

    :param project_id: The ID of the Project entity.
    :type project_id: str
    :param api_key: The API key to authorize the request against.
    :type api_key: str
    :return A Project document.
    :rtype Response
    """
    assertions.datatype_str('project_id', project_id)
    url = '/projects/{}'.format(project_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def delete_project(project_id, api_key=None):
    """
    Delete a Project.

    :param project_id: The ID of the Project entity.
    :type project_id: str
    :param api_key: The API key to authorize the request against.
    :type api_key: str
    :return Blank string.
    :rtype Response
    """
    assertions.datatype_str('project_id', project_id)
    url = '/projects/{}'.format(project_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def delete_all_projects(api_key=None):
    """
    Delete all projects.

    :param api_key: The API key to authorize the request against.
    :type api_key: str
    """
    for project in list_projects(api_key=api_key).json():
        response = delete_project(project['id'], api_key=api_key)
        print(project['id'], project['name'], response)
