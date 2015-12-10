from evrythng import assertions, utils


datatype_specs = {
    'name': 'str',
    'description': 'str',
    'brand': 'str',
    'categories': 'list_of_str',
    'photos': 'list_of_str',
    'url': 'str',
    'identifiers': 'dict_of_dict',
    'properties': 'dict',
    'tags': 'list_of_str',
    'customFields': 'dict',
}
required_fields = ('name',)
readonly_fields = ('id', 'createdAt', 'updatedAt', 'activatedAt')
writable_fields = ('description', 'brand', 'categories', 'photos', 'url',
                   'identifiers', 'properties', 'tags', 'customFields')


def _validate_data(kwargs):
    """Sanity checking of data that is submitted to evrythng."""
    assertions.required(kwargs, required_fields)
    assertions.readonly(kwargs, readonly_fields)
    assertions.no_extras(
        kwargs, required_fields + writable_fields + readonly_fields)
    assertions.datatypes(kwargs, datatype_specs)


def create_product(name, description=None, brand=None, categories=None,
                   photos=None, url=None, identifiers=None, properties=None,
                   tags=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    _validate_data(kwargs)
    return utils.request('POST', '/products', data=kwargs, api_key=api_key)


def list_products(api_key=None):
    return utils.request('GET', '/products', api_key=api_key)


def read_product(product_id, api_key=None):
    url = '/products/{}'.format(product_id)
    return utils.request('GET', url, api_key=api_key)


def update_product(product_id, name, description=None, brand=None,
                   categories=None, photos=None, url=None, identifiers=None,
                   properties=None, tags=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    product_id = kwargs.pop('product_id')
    _validate_data(kwargs)
    url = '/products/{}'.format(product_id)
    return utils.request(
        'PUT', url, data=kwargs, api_key=api_key)


def delete_product(product_id, api_key=None):
    url = '/products/{}'.format(product_id)
    return utils.request('DELETE', url, api_key=api_key)
