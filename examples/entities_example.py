import os
import random
import string
from datetime import datetime

from evrythng import entities

# Set this to your Operator Key located at:
# https://dashboard.evrythng.com/settings/account
EVT_OPERATOR_KEY = '2qdmVjDDFk9VQif7FEyHS1kdUyYXEP4C6C2Pfm2J9fRg42YpyFiTeqZY29XlE278rHsHlKrY7riIxpxM'
os.environ['EVRYTHNG_API_TOKEN'] = EVT_OPERATOR_KEY
os.environ['PYEVT_DEBUG'] = '1'


def assert_status_code(response, expected_status):
    try:
        assert response.status_code == expected_status
    except AssertionError:
        raise AssertionError('Response status of {} when expecting {}: {}'.format(
            response.status_code, expected_status, response.text))


def debug(s):
    print('\nEXAMPLE: {}'.format(s))

debug('Creating a  Project...')
response = entities.create_project('python-evrythng Project')
assert_status_code(response, 201)
project_id = response.json()['id']

debug('Creating an Application under Project={}...'.format(
    project_id))
response = entities.create_application(project_id, 'python-evrythng Application')
assert_status_code(response, 201)
response_json = response.json()

debug('You can get the Trusted API key of the Application...')
application_id = response_json['id']
trusted_app_key = entities.read_trusted_application_key(project_id, application_id)
app_key = response_json['appApiKey']

debug('Creating a Thng...')
response = entities.create_thng('python-evrythng Thng',
                                customFields={'meta': {'room': '209b'}})
assert_status_code(response, 201)
thng_id = response.json()['id']

debug('Removing a Thng as an "Application User" should result in a 403 Forbidden.')
response = entities.delete_thng(thng_id, api_key=app_key)
assert_status_code(response, 403)

property_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])

debug('Create a Property on the Thng={} with name={}...'.format(
    thng_id, property_name))
response = entities.create_thng_properties(thng_id, [
    {'key': property_name, 'value': 123}
])
assert_status_code(response, 200)

datetime_to_milliseconds = lambda x: int(x.strftime('%s') + '000')

debug('Create multiple values for Property on the Thng={} with name={}...'.format(
    thng_id, property_name))
response = entities.create_thng_properties(thng_id, [
    {'key': property_name,
     'value': 8.3,
     'timestamp': datetime_to_milliseconds(datetime(2016, 10, 24))},
    {'key': property_name,
     'value': 1.3,
     'timestamp': datetime_to_milliseconds(datetime(2016, 10, 25))},
    {'key': property_name,
     'value': 5.2,
     'timestamp': datetime_to_milliseconds(datetime(2016, 10, 26))},
])
assert_status_code(response, 200)
