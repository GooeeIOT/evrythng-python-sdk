Python Evrythng
===============

A comprehensive pythonic wrapper around the Evrythng REST API.

.. image:: https://img.shields.io/pypi/v/python-evrythng.svg
    :target: https://pypi.python.org/pypi/python-evrythng

For more information about Evrythng and the API that this module wraps, see the
`Evrythng Documentation Portal <https://dashboard.evrythng.com/documentation/api>`_.

Installation
------------

`python-evrythng` is available on PyPI and can be installed via pip.

.. code-block:: bash

    $ pip install python-evrythng

Example Usage
-------------

.. code-block:: python

    import os
    from evrythng import entities

    EVT_OPERATOR_KEY = 'your operator key from the Accounts page'
    os.environ['EVRYTHNG_API_TOKEN'] = EVT_OPERATOR_KEY
    os.environ['PYEVT_DEBUG'] = '1'

    print('Creating a  Project...')
    response = entities.create_project('python-evrythng Project')
    assert response.status_code == 201
    project_id = response.json()['id']

    print('Creating an Application under Project={}...'.format(
        project_id))
    response = entities.create_application(project_id,
                                           'python-evrythng Application')
    assert response.status_code == 201
    response_json = response.json()

    print('You can get the Trusted API key of the Application...')
    application_id = response_json['id']
    trusted_app_key = entities.read_trusted_application_key(
        project_id, application_id)
    app_key = response_json['appApiKey']
    print('Trusted App Key = {} for Application={}'.format(
        trusted_app_key, application_id))

Found a bug, wanna help?
------------------------

Awesome, let us know! Create a pull request.

.. image:: https://raw.githubusercontent.com/GooeeIOT/python-evrythng/master/docs/gooee.png
    :width: 50%

.. image:: https://raw.githubusercontent.com/LyleScott/python-evrythng/master/docs/evrythng.png
    :width: 50%

