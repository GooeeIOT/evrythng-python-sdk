"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/reactor
"""
from evrythng import assertions, utils


reactor_bundle_field_specs = {
    'datatypes': {
        'bundle_bytes': 'not_implemented',
    },
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('bundle_bytes',),
    'required': (),
}

reactor_script_field_specs = {
    'datatypes': {
        'type': 'enum|simple,bundle',
        'script': 'str',
        'manifest': 'str',
    },
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('type', 'script', 'manifest'),
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


def update_reactor_bundle(project_id, application_id, bundle_bytes,
                          api_key=None):
    """
    Update a Reactor via a bundle of files; A zip file containing main.js,
    package.json, etc.

    :param project_id: The ID of the Project.
    :type project_id: str
    :param application_id: The ID for the Application that is a child of the
                           Project for which the reactor script will be scoped
                           to.
    :type application_id: str
    :param bundle_bytes: The bytes that make up the Zip file containing the
                         bundle of files.
    :type bundle_bytes: bytes
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    assertions.datatype_str('project_id', project_id)
    application_id = kwargs.pop('application_id')
    assertions.datatype_str('application_id', application_id)
    assertions.validate_field_specs(kwargs, reactor_bundle_field_specs)
    url = '/projects/{}/applications/{}/reactorScript'.format(
        project_id, application_id)
    files = {'file': bundle_bytes}
    return utils.request('PUT', url, files=files, api_key=api_key)


def update_reactor_script(project_id, application_id, script, manifest='',
                          type_='simple', api_key=None):
    """
    Update the Reactor with a single script text file and an optional manifest.

    :param project_id: The ID of the Project.
    :type project_id: str
    :param application_id: The ID for the Application that is a child of the
                           Project for which the reactor script will be scoped
                           to.
    :type application_id: str
    :param script: The reactor script body.
    :type script: str
    :param manifest: The manifest file for running the script. A packages.json
                     file, basically.
    :type manifest: str
    :param type_: The reactor script type. Possible values are simple, bundle.
                  Default is simple
    :type type_: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    kwargs = locals()
    kwargs['type'] = kwargs.pop('type_')
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    assertions.datatype_str('project_id', project_id)
    application_id = kwargs.pop('application_id')
    assertions.datatype_str('application_id', application_id)
    assertions.validate_field_specs(kwargs, reactor_script_field_specs)
    url = '/projects/{}/applications/{}/reactorScript'.format(
        project_id, application_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


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
    url = '/projects/{}/applications/{}/reactorScript'.format(
        project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def get_reactor_status(project_id, application_id, api_key=None):
    """
    Read the reactor script status.

    :param project_id: The Project of the Application.
    :type project_id: str
    :param application_id: The Application to get the script for.
    :type application_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return:
    """
    url = '/projects/{}/applications/{}/reactorScript/status'.format(
        project_id, application_id)
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

    url = '/projects/{}/applications/{}/reactorLogs/bulk'.format(
        project_id, application_id)
    return utils.request('POST', url, api_key=api_key, accept=True, data=logs)


def get_reactor_logs(project_id, application_id, api_key=None, **request_kwargs):
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
    url = '/projects/{}/applications/{}/reactorLogs'.format(
        project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True, **request_kwargs)


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
    url = '/projects/{}/applications/{}/reactorLogs'.format(
        project_id, application_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
