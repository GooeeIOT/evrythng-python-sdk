"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/collections
"""
from evrythng import assertions, utils
from evrythng.entities.actions import field_specs as action_field_specs


field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'customFields': 'dict',
        'collections': 'list_of_ref',
        'tags': 'list_of_str',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('description', 'customFields', 'collections', 'tags'),
}


def create_collection_action(type_, collection, timestamp=None, identifiers=None,
                             location=None, locationSource=None, context=None, customFields=None,
                             api_key=None):
    """Create an Action for a Collection"""
    kwargs = locals()
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, action_field_specs)

    url = '/collections/{}/actions/{}'.format(collection, type_)

    return utils.request('POST', url, data=kwargs, api_key=api_key)


def create_collection(name, description=None, customFields=None,
                      collections=None, tags=None, api_key=None):
    """
    Create a new Collection.

    :param name: The Name of the Collection.
    :type description: str
    :param description: The Description of the Collection.
    :type description: str
    :param customFields: The Custom Fields of Collection.
    :type customFields: dict
    :param collections: The Collections of the Collection.
    :type collections: list of str
    :param tags: The Tags of the Collection.
    :type tags: list of str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/collections', data=kwargs, api_key=api_key)


def list_collections(api_key=None, **request_kwargs):
    """
    List Collections.

    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    return utils.request('GET', '/collections', api_key=api_key, **request_kwargs)


def read_collection(collection_id, api_key=None):
    """
    Read a Collection.

    :param collection_id: The Collection to read.
    :type collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}'.format(collection_id)
    return utils.request('GET', url, api_key=api_key)


def update_collection(collection_id, name=None, description=None,
                      customFields=None, collections=None, tags=None,
                      api_key=None):
    """
    Update an existing Collection.

    :param collection_id: The Collection to update.
    :type collection_id: str
    :param name: The Name of the Collection.
    :type description: str
    :param description: The Description of the Collection.
    :type description: str
    :param customFields: The Custom Fields of Collection.
    :type customFields: dict
    :param collections: The Collections of the Collection.
    :type collections: list of str
    :param tags: The Tags of the Collection.
    :type tags: list of str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    kwargs = locals()
    collection_id = kwargs.pop('collection_id')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/collections/{}'.format(collection_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key)


def delete_collection(collection_id, api_key=None):
    """
    Delete an existing Collection.

    :param collection_id: The Collection to delete.
    :type collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}'.format(collection_id)
    return utils.request('DELETE', url, api_key=api_key)


def list_collection_thngs(collection_id, api_key=None):
    """
    List a Collection's Thngs.

    :param collection_id: The Collection to list Thngs for.
    :type collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}/thngs'.format(collection_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def add_collection_thngs(collection_id, thng_ids, api_key=None):
    """
    Add Thngs to a Collection.

    :param collection_id: The Collection to add Thngs to.
    :type collection_id: str
    :param thng_ids: The Thngs to add to the Collection.
    :type thng_ids: list of str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    assertions.datatype_list_of_str('thng_ids', thng_ids)
    url = '/collections/{}/thngs'.format(collection_id)
    return utils.request('PUT', url, data=thng_ids, api_key=api_key)


def delete_collection_thng(collection_id, thng_id, api_key=None):
    """
    Delete a Thng from a Collection.

    :param collection_id: The Collection to remove Thngs from.
    :type collection_id: str
    :param thng_id: The Thng to remove from the Collection.
    :type thng_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}/thngs/{}'.format(collection_id, thng_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def delete_all_collection_thngs(collection_id, api_key=None):
    """
    Delete *ALL* Thngs from a Collection.

    :param collection_id: The Collection to remove *all* Thngs from.
    :type collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}/thngs'.format(collection_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def add_collections_to_collection(collection_id, collection_ids, api_key=None):
    """
    Add Collection to a Collection.

    :param collection_id: The Collection to add Collections to.
    :type collection_id: str
    :param collection_ids: The Collections to add.
    :type collection_ids: list of str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    assertions.datatype_list_of_str('collection_ids', collection_ids)
    url = '/collections/{}/collections'.format(collection_id)
    return utils.request('POST', url, data=collection_ids, api_key=api_key)


def delete_collection_from_collection(collection_id, child_collection_id,
                                      api_key=None):
    """
    Delete a Collection from a Collection.

    :param collection_id: The Collection to remove a Collection from.
    :type collection_id: str
    :param child_collection_id: The child Collection to remove.
    :type child_collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    assertions.datatype_str('child_collection_id', collection_id)
    url = '/collections/{}/collections/{}'.format(
        collection_id, child_collection_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def delete_all_collections_from_collection(collection_id, api_key=None):
    """
    Delete *ALL* Collections from a Collection.

    :param collection_id: The Collection to remove *all* Collections from.
    :type collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}/collections'.format(collection_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)


def read_collections_from_collection(collection_id, api_key=None):
    """
    Read the Collections of a Collection.

    :param collection_id: The Collection to read the Collections of.
    :type collection_id: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection_id', collection_id)
    url = '/collections/{}/collections'.format(collection_id)
    return utils.request('GET', url, api_key=api_key, accept=True)
