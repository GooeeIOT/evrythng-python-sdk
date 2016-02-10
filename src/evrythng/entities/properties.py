"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/properties
"""
from evrythng import assertions, utils


field_specs = {
    'datatypes': {
        'key': 'str',
        'value': 'str_num_bool',
        'timestamp': 'time'
    },
    'required': ('key', 'value'),
    'readonly': tuple(),
    'writable': ('timestamp',),
}


# Update a single Property


def upsert_product_property(product_id, key, value, timestamp=None,
                            api_key=None):
    """Create/Update a single Property on a Product.

    POST /products/{$product_id}/properties/{$key}
    {"value": {$value}}
    """
    key_values = {'key': key, 'value': value}
    if timestamp is not None:
        key_values['timestamp'] = timestamp
    return _upsert_properties('products', product_id, key_values,
                              api_key=api_key)


def upsert_thng_property(thng_id, key, value, timestamp=None, api_key=None):
    """Create/Update a single Property on a Thng.

    POST /thngs/{$thng_id}/properties/{$key}
    {"value": {$value}}
    """
    key_values = {'key': key, 'value': value}
    if timestamp is not None:
        key_values['timestamp'] = timestamp
    return _upsert_property('thngs', thng_id, key_values, api_key=api_key)


def _upsert_property(entity_type, entity_id, key_values, api_key=None):
    """A helper to wrap common property update functionality."""
    assertions.validate_field_specs(key_values, field_specs)
    key = key_values.pop('key')
    url = '/{}/{}/properties/{}'.format(entity_type, entity_id, key)
    return utils.request('PUT', url, data=[key_values], api_key=api_key)


# Convenience functions.
create_product_property = upsert_product_property
update_product_property = upsert_product_property


# Update multiple Properties


def upsert_product_properties(product_id, key_values, api_key=None):
    """Create/Update multiple Properties on a Product.

    POST /products/{$product_id}/properties
    [{"key": "max_wattage", "value": 40}, {"key": "sku", "value": "abc123"}]
    """
    for key_value in key_values:
        assertions.validate_field_specs(key_value, field_specs)
    return _upsert_properties('products', product_id, key_values,
                              api_key=api_key)


def upsert_thng_properties(thng_id, key_values, api_key=None):
    """Create/Update multiple Properties on a Thng.

    POST /thngs/{$thng_id}/properties
    [{"key": "motion", "value": 20}, {"key": "temperature", "value": 98}]
    """
    for key_value in key_values:
        assertions.validate_field_specs(key_value, field_specs)
    return _upsert_properties('thngs', thng_id, key_values, api_key=api_key)


def _upsert_properties(entity_type, entity_id, key_values, api_key=None):
    """A helper to wrap common property update functionality."""
    url = '/{}/{}/properties'.format(entity_type, entity_id)
    return utils.request('POST', url, data=key_values, api_key=api_key)


# Convenience functions.
create_thng_properties = upsert_thng_properties
update_thng_properties = upsert_thng_properties


# List Properties


def list_product_properties(product_id, api_key=None):
    """List all Properties on a Product.

    TODO: add filtering capability.
    """
    assertions.datatype_str('product_id', product_id)
    url = '/products/{}/properties'.format(product_id)
    return utils.request('GET', url, api_key=api_key)


def list_thng_properties(thng_id, api_key=None):
    """List all Properties on a thng.

    TODO: add filtering capability.
    """
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}/properties'.format(thng_id)
    return utils.request('GET', url, api_key=api_key)
