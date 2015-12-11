from evrythng.exceptions import InvalidDatatypeException
from evrythng import assertions, utils


datatype_specs = {
    'description': 'str',
    'customFields': 'dict',
    'collections': 'list_of_ref',
    'tags': 'list_of_str',
}
required_fields = ('name',)
readonly_fields = ('id', 'createdAt', 'updatedAt')
writable_fields = ('description', 'customFields', 'collections', 'tags')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_collection(name, description=None, customFields=None,
                      collections=None, tags=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request('POST', '/collections', data=kwargs, api_key=api_key)


def list_collections(api_key=None):
    return utils.request('GET', '/collections', api_key=api_key)


def read_collection(collection_id, api_key=None):
    url = '/collections/{}'.format(collection_id)
    return utils.request('GET', url, api_key=api_key)


def update_collection(collection_id, name=None, description=None,
                      customFields=None, collections=None, tags=None,
                      api_key=None):
    kwargs = locals()
    collection_id = kwargs.pop('collection_id')
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    url = '/collections/{}'.format(collection_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key)


def delete_collection(collection_id, api_key=None):
    url = '/collections/{}'.format(collection_id)
    return utils.request('DELETE', url, api_key=api_key)


def list_collection_thngs(collection_id, api_key=None):
    url = '/collections/{}/thngs'.format(collection_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def _assert_collection_id_is_str(collection_id):
    try:
        assert isinstance(collection_id, str)
    except AssertionError:
        raise InvalidDatatypeException(
            'collection_id', str, type(collection_id))


def add_collection_thngs(collection_id, thng_ids, api_key=None):
    if not hasattr(thng_ids, '__iter__'):
        raise InvalidDatatypeException(
            'thng_ids', type(thng_ids), (list, tuple))
    for i, item in enumerate(thng_ids):
        try:
            assert isinstance(item, str)
        except AssertionError:
            InvalidDatatypeException('thng_ids[{}]'.format(i), str, type(item))
    url = '/collections/{}/thngs'.format(collection_id)
    return utils.request('PUT', url, data=thng_ids, api_key=api_key)


def delete_collection_thng(collection_id, thng_id, api_key=None):
    _assert_collection_id_is_str(collection_id)
    url = '/collections/{}/thngs/{}'.format(collection_id, thng_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def delete_all_collection_things(collection_id, api_key=None):
    _assert_collection_id_is_str(collection_id)
    url = '/collections/{}/collections'.format(collection_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def add_collections_to_collection(collection_id, collection_ids, api_key=None):
    _assert_collection_id_is_str(collection_id)
    if not hasattr(collection_ids, '__iter__'):
        raise InvalidDatatypeException(
            'thng_ids', type(collection_ids), (list, tuple))

    for i, item in enumerate(collection_ids):
        try:
            assert isinstance(item, str)
        except AssertionError:
            InvalidDatatypeException(
                'collection_ids[{}]'.format(i), str, type(item))

    url = '/collections/{}/collections'.format(collection_id)
    return utils.request('POST', url, data=collection_ids, api_key=api_key)


def delete_collection_from_collection(collection_id, child_collection_id,
                                      api_key=None):
    _assert_collection_id_is_str(collection_id)

    try:
        assert isinstance(child_collection_id, str)
    except AssertionError:
        raise InvalidDatatypeException(
            'child_collection_id', str, type(child_collection_id))

    url = '/collections/{}/collections/{}'.format(
        collection_id, child_collection_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def delete_all_collections_from_collection(collection_id, api_key=None):
    _assert_collection_id_is_str(collection_id)
    url = '/collections/{}/collections'.format(collection_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
