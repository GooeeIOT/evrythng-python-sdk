"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/products
"""
from evrythng import assertions, utils


field_specs = {
    'datatypes': {
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
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt', 'activatedAt'),
    'writable': ('description', 'brand', 'categories', 'photos', 'url',
                 'identifiers', 'properties', 'tags', 'customFields'),
}


def create_product(name, description=None, brand=None, categories=None,
                   photos=None, url=None, identifiers=None, properties=None,
                   tags=None, customFields=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/products', data=kwargs, api_key=api_key)


def list_products(api_key=None, **request_kwargs):
    return utils.request('GET', '/products', api_key=api_key, **request_kwargs)


def read_product(product_id, api_key=None):
    assertions.datatype_str('product_id', product_id)
    url = '/products/{}'.format(product_id)
    return utils.request('GET', url, api_key=api_key)


def update_product(product_id, name=None, description=None, brand=None,
                   categories=None, photos=None, url=None, identifiers=None,
                   properties=None, tags=None, customFields=None, api_key=None):
    kwargs = locals()
    product_id = kwargs.pop('product_id')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/products/{}'.format(product_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


def delete_product(product_id, api_key=None):
    assertions.datatype_str('product_id', product_id)
    url = '/products/{}'.format(product_id)
    return utils.request('DELETE', url, api_key=api_key)
