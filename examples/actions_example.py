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


ACTION_NAME = '_testactiontype'


# Make sure ActionType exists.

response = entities.list_action_types(EVT_OPERATOR_KEY)
for item in response.json():
    if item['name'] == ACTION_NAME:
        break
else:
    response = entities.create_action_type(ACTION_NAME)
    assert_status_code(response, 201)


# Thng Actions.

debug('Creating a Thng...')
response = entities.create_thng('python-evrythng Thng')
assert_status_code(response, 201)
thng_id = response.json()['id']

response = entities.create_thng_action(ACTION_NAME, thng_id)
assert_status_code(response, 201)

response = entities.read_thng_actions(thng_id, ACTION_NAME)
assert len(response.json()) == 1


# Collection actions.

debug('Creating a Collection...')
response = entities.create_collection('python-evrythng collection')
assert_status_code(response, 201)
collection_id = response.json()['id']
response = entities.add_collection_thngs(collection_id, [thng_id])

response = entities.create_collection_action(ACTION_NAME, collection_id)
assert_status_code(response, 201)

response = entities.read_collection_actions(collection_id, ACTION_NAME)
assert len(response.json()) == 1


# Product actions.

debug('Creating a Thng...')
response = entities.create_product('python-evrythng product')
assert_status_code(response, 201)
product_id = response.json()['id']

response = entities.create_product_action(ACTION_NAME, product_id)
assert_status_code(response, 201)

response = entities.read_product_actions(product_id, ACTION_NAME)
assert len(response.json()) == 1
