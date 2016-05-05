"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/reactor
"""
from evrythng import assertions, utils


reactor_field_specs = {
    'datatypes': {
        'type': 'str',
        'script': 'str',
        'files': 'dict',
        'manifest': 'ref',
    },
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('type', 'script', 'files', 'manifest'),
    'required': (),
}

reactor_log_field_specs = {
    'datatypes': {
        'logLevel': 'str',
        'message': 'str',
        'app': 'ref',
        'timestamp': 'time',
    },
    'readonly': ('id', 'createdAt'),
    'writable': ('logLevel', 'message', 'app', 'timestamp'),
    'required': ('logLevel', 'message', 'app'),
}


def update_reactor(project_id, application_id, script=None, bundle=None, manifest=None,
                   api_key=None):
    """
    Update a Reactor Script.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to update the Reactor script for.
    :type application_id: str
    :param script: The reactor script.
    :type script: str
    :param bundle: The reactor script bundle.
    :type bundle: dict
    :param manifest: The reactor script manifest.
    :type manifest: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    application_id = kwargs.pop('application_id')
    bundle = kwargs.pop('bundle', None)

    assertions.validate_field_specs(kwargs, reactor_field_specs)
    url = '/projects/{}/applications/{}/reactorScript'.format(project_id, application_id)

    return utils.request('PUT', url, data=None if bundle else kwargs, api_key=api_key, files=bundle)


def get_reactor(project_id, application_id, api_key=None):
    """
    Get the Reactor script of the Project Application.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to get the script for.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}/reactorScript'.format(project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def create_reactor_logs(project_id, application_id, logs, api_key=None):
    """
    Create one or more Reactor script logs.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to create the logs for.
    :type application_id: str
    :param logs: Reactor logs to create.
    :type logs: list of LogEntryDocuments
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    for log in logs:
        assertions.validate_field_specs(log, reactor_log_field_specs)

    url = '/projects/{}/applications/{}/reactorLogs/bulk'.format(project_id, application_id)
    return utils.request('POST', url, api_key=api_key, accept=True, data=logs)


def get_reactor_logs(project_id, application_id, api_key=None):
    """
    Get the logs of a Reactor script.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to get the script logs for.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}/reactorLogs'.format(project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def delete_reactor_logs(project_id, application_id, api_key=None):
    """
    Delete the logs of a Reactor script.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to delete the logs for.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}/reactorLogs'.format(project_id, application_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
