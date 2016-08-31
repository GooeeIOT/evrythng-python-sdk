"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/properties
"""
from evrythng import assertions, utils


field_specs = {
    'datatypes': {
        'key': 'str',
        'value': 'json',
        'timestamp': 'time'
    },
    'required': ('key', 'value'),
    'readonly': tuple(),
    'writable': ('timestamp',),
}


# Update a single Property


def upsert_product_property(product_id, key, values, **request_kwargs):
    """Create/Update a single Property on a Product.

    POST /products/{$product_id}/properties/{$key}
    {"value": {$value}}
    """
    assertions.datatype_str('product_id', product_id)
    return _upsert_property('products', product_id, key, values, **request_kwargs)


def upsert_thng_property(thng_id, key, values, **request_kwargs):
    """Create/Update a single Property on a Thng.

    POST /thngs/{$thng_id}/properties/{$key}
    {"value": {$value}}
    """
    assertions.datatype_str('thng_id', thng_id)
    return _upsert_property('thngs', thng_id, key, values, **request_kwargs)


def _upsert_property(entity_type, entity_id, key, values, **request_kwargs):
    """A helper to wrap common property update functionality."""
    assertions.datatype_str('key', key)
    url = '/{}/{}/properties/{}'.format(entity_type, entity_id, key)
    return utils.request('PUT', url, data=values, **request_kwargs)


# Convenience functions.
create_product_property = upsert_product_property
update_product_property = upsert_product_property


# Update multiple Properties


def upsert_product_properties(product_id, key_values, **request_kwargs):
    """Create/Update multiple Properties on a Product.

    POST /products/{$product_id}/properties
    [{"key": "max_wattage", "value": 40}, {"key": "sku", "value": "abc123"}]
    """
    for key_value in key_values:
        assertions.validate_field_specs(key_value, field_specs)
    return _upsert_properties('products', product_id, key_values, **request_kwargs)


def upsert_thng_properties(thng_id, key_values, **request_kwargs):
    """Create/Update multiple Properties on a Thng.

    POST /thngs/{$thng_id}/properties
    [{"key": "motion", "value": 20}, {"key": "temperature", "value": 98}]
    """
    for key_value in key_values:
        assertions.validate_field_specs(key_value, field_specs)
    return _upsert_properties('thngs', thng_id, key_values, **request_kwargs)


def _upsert_properties(entity_type, entity_id, key_values, api_key=None):
    """A helper to wrap common property update functionality."""
    url = '/{}/{}/properties'.format(entity_type, entity_id)
    return utils.request('POST', url, data=key_values, api_key=api_key)


# Convenience functions.
create_thng_properties = upsert_thng_properties
update_thng_properties = upsert_thng_properties


# List All Properties


def list_product_properties(product_id, from_date=None, to_date=None, **request_kwargs):
    """List all Properties on a Product."""
    assertions.datatype_str('product_id', product_id)
    url = '/products/{}/properties'.format(product_id)
    return utils.request('GET', url, **request_kwargs)


def list_thng_properties(thng_id, from_date=None, to_date=None, **request_kwargs):
    """List all Properties on a thng."""
    assertions.datatype_str('thng_id', thng_id)
    url = '/thngs/{}/properties'.format(thng_id)
    return utils.request('GET', url, **request_kwargs)


# Read a Property


def _read_property(evrythng_id, evrythng_type, property_name, timestamp_to=None,
                   timestamp_from=None, **request_kwargs):
    """Helper for reading properties."""
    assertions.datatype_str('property_name', property_name)
    url = '/{}/{}/properties/{}'.format(evrythng_type, evrythng_id, property_name)
    query_params = request_kwargs.get('query_params', {})

    if timestamp_from:
        assertions.datatype_time('timestamp', timestamp_from)
        query_params['from'] = timestamp_from
    if timestamp_to:
        assertions.datatype_time('timestamp', timestamp_to)
        query_params['to'] = timestamp_to

    request_kwargs.update(query_params=query_params)

    return utils.request('GET', url, **request_kwargs)


def read_product_property(product_id, property_name, timestamp_from=None, timestamp_to=None,
                          **request_kwargs):
    """Read a Product Property."""
    assertions.datatype_str('product_id', product_id)
    return _read_property(product_id, 'products', property_name, timestamp_from=timestamp_from,
                          timestamp_to=timestamp_to, **request_kwargs)


def read_thng_property(thng_id, property_name, timestamp_from=None, timestamp_to=None,
                       **request_kwargs):
    """Read a Thng Property."""
    assertions.datatype_str('thng_id', thng_id)
    return _read_property(thng_id, 'thngs', property_name, timestamp_from=timestamp_from,
                          timestamp_to=timestamp_to, **request_kwargs)


# Delete Properties
#
# The only way to delete data points is to append the ?to=Timestamp URL query
# parameter to specify a point in time before which all the data points will
# be removed.
#
# ATTENTION: If the ?to= parameter is not specified, ALL updates of this
# property will be deleted!


def _delete_property(evrythng_id, evrythng_type, property_name, timestamp_from=None,
                     timestamp_to=None, **request_kwargs):
    """Helper for deleting properties."""
    assertions.datatype_str('property_name', property_name)
    query_params = {}
    if timestamp_from:
        assertions.datatype_time('timestamp', timestamp_from)
        query_params['from'] = timestamp_from
    if timestamp_to:
        assertions.datatype_time('timestamp', timestamp_to)
        query_params['to'] = timestamp_to
    url = '/{}/{}/properties/{}'.format(evrythng_type, evrythng_id, property_name)
    return utils.request('DELETE', url, query_params=query_params, **request_kwargs)


def delete_product_property(product_id, property_name, timestamp_from=None, timestamp_to=None,
                            **request_kwargs):
    """Delete a Property on a Product."""
    assertions.datatype_str('product_id', product_id)
    _delete_property(product_id, 'products', property_name, timestamp_from=timestamp_from,
                     timestamp_to=timestamp_to, **request_kwargs)


def delete_thng_property(thng_id, property_name, timestamp_from=None,
                         timestamp_to=None, **request_kwargs):
    """Delete a Property on a Thng."""
    assertions.datatype_str('thng_id', thng_id)
    _delete_property(thng_id, 'thngs', property_name, timestamp_from=timestamp_from,
                     timestamp_to=timestamp_to, **request_kwargs)
