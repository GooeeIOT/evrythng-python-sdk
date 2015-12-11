from evrythng import assertions, utils


__all__ = [
    'create_property',
    'create_property_on_thng',
    'create_property_on_product',
    'update_property_on_thng',
    'update_property_on_product',
    'list_properties_on_thng',
    'list_properties_on_product',
]

field_specs = {
    'datatypes': {
        'key': 'str',
        'value': 'str',
    },
    'required': ('key', 'value'),
    'readonly': tuple(),
    'writable': ('timestamp',),
}


def create_property(key, value, timestamp=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/properties', data=kwargs, api_key=api_key)


def create_property_on_thng(thngId, key, value, timestamp=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/thngs/{}/properties'.format(thngId)
    return utils.request('POST', url, data=kwargs, api_key=api_key)


def create_property_on_product(product_id, key, value, timestamp=None,
                               api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/products/{}/properties'.format(product_id)
    return utils.request('POST', url, data=kwargs, api_key=api_key)


def update_property_on_thng(thngId, key, value, timestamp=None, api_key=None):
    kwargs = locals()
    thngId = kwargs.pop('thngId')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/thngs/{}/properties'.format(thngId)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


def update_property_on_product(product_id, key, value, timestamp=None,
                               api_key=None):
    kwargs = locals()
    product_id = kwargs.pop('product_id')
    api_key = kwargs.pop('api_key')
    url = '/products/{}/properties'.format(product_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


def list_properties_on_thng(thngId, api_key=None):
    assertions.datatype_str('thngId', thngId)
    url = '/thngs/{}/properties'.format(thngId)
    return utils.request('PUT', url, api_key=api_key)


def list_properties_on_product(product_id, api_key=None):
    assertions.datatype_str('product_id', product_id)
    url = '/products/{}/properties'.format(product_id)
    return utils.request('GET', url, api_key=api_key)
