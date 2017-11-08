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


def create_collection_action(type_, collection, timestamp=None,
                             identifiers=None,
                             location=None, locationSource=None, context=None,
                             customFields=None, api_key=None,
                             request_kwargs=None):
    """Create an Action for a Collection."""
    kwargs = locals()
    del kwargs['request_kwargs']
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    assertions.validate_field_specs(kwargs, action_field_specs)

    url = '/collections/{}/actions/{}'.format(collection, type_)

    return utils.request('POST', url, data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def read_collection_actions(collection, type_, api_key=None,
                            request_kwargs=None):
    """Read Actions for a Collection."""
    assertions.datatype_str('collection', collection)
    assertions.datatype_str('type_', type_)
    url = '/collections/{}/actions/{}'.format(collection, type_)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def create_collection(name, description=None, customFields=None,
                      collections=None, tags=None, api_key=None,
                      request_kwargs=None):
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
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/collections', data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def list_collections(api_key=None, request_kwargs=None):
    """
    List Collections.

    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    return utils.request('GET', '/collections', api_key=api_key,
                         **(request_kwargs or {}))


def read_collection(collection, api_key=None, request_kwargs=None):
    """
    Read a Collection.

    :param collection: The Collection to read.
    :type collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}'.format(collection)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def update_collection(collection, name=None, description=None,
                      customFields=None, collections=None, tags=None,
                      api_key=None, request_kwargs=None):
    """
    Update an existing Collection.

    :param collection: The Collection to update.
    :type collection: str
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
    del kwargs['request_kwargs']
    collection = kwargs.pop('collection')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/collections/{}'.format(collection)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key, **(request_kwargs or {}))


def delete_collection(collection, api_key=None, request_kwargs=None):
    """
    Delete an existing Collection.

    :param collection: The Collection to delete.
    :type collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}'.format(collection)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))


def list_collection_thngs(collection, api_key=None, request_kwargs=None):
    """
    List a Collection's Thngs.

    :param collection: The Collection to list Thngs for.
    :type collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}/thngs'.format(collection)
    return utils.request('GET', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def add_collection_thngs(collection, thngs, api_key=None, request_kwargs=None):
    """
    Add Thngs to a Collection.

    :param collection: The Collection to add Thngs to.
    :type collection: str
    :param thngs: The Thngs to add to the Collection.
    :type thngs: list of str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    assertions.datatype_list_of_str('thngs', thngs)
    url = '/collections/{}/thngs'.format(collection)
    return utils.request('PUT', url, data=thngs, api_key=api_key,
                         **(request_kwargs or {}))


def delete_collection_thng(collection, thng, api_key=None, request_kwargs=None):
    """
    Delete a Thng from a Collection.

    :param collection: The Collection to remove Thngs from.
    :type collection: str
    :param thng: The Thng to remove from the Collection.
    :type thng: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}/thngs/{}'.format(collection, thng)
    return utils.request('DELETE', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def delete_all_collection_thngs(collection, api_key=None, request_kwargs=None):
    """
    Delete *ALL* Thngs from a Collection.

    :param collection: The Collection to remove *all* Thngs from.
    :type collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}/thngs'.format(collection)
    return utils.request('DELETE', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def add_collections_to_collection(collection, collections, api_key=None,
                                  request_kwargs=None):
    """
    Add Collection to a Collection.

    :param collection: The Collection to add Collections to.
    :type collection: str
    :param collections: The Collections to add.
    :type collections: list of str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    assertions.datatype_list_of_str('collections', collections)
    url = '/collections/{}/collections'.format(collection)
    return utils.request('POST', url, data=collections, api_key=api_key,
                         **(request_kwargs or {}))


def delete_collection_from_collection(collection, child_collection,
                                      api_key=None, request_kwargs=None):
    """
    Delete a Collection from a Collection.

    :param collection: The Collection to remove a Collection from.
    :type collection: str
    :param child_collection: The child Collection to remove.
    :type child_collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    assertions.datatype_str('child_collection', collection)
    url = '/collections/{}/collections/{}'.format(
        collection, child_collection)
    return utils.request('DELETE', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def delete_all_collections_from_collection(collection, api_key=None,
                                           request_kwargs=None):
    """
    Delete *ALL* Collections from a Collection.

    :param collection: The Collection to remove *all* Collections from.
    :type collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}/collections'.format(collection)
    return utils.request('DELETE', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))


def read_collections_from_collection(collection, api_key=None,
                                     request_kwargs=None):
    """
    Read the Collections of a Collection.

    :param collection: The Collection to read the Collections of.
    :type collection: str
    :param api_key: The API key to authorize request against.
    :type api_key: str
    :return
    :rtype
    """
    assertions.datatype_str('collection', collection)
    url = '/collections/{}/collections'.format(collection)
    return utils.request('GET', url, api_key=api_key, accept=True,
                         **(request_kwargs or {}))
