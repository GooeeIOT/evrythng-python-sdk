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


def upsert_product_property(product, key, values, api_key=None,
                            request_kwargs=None):
    """Create/Update a single Property on a Product.

    POST /products/{$product}/properties/{$key}
    {"value": {$value}}
    """
    assertions.datatype_str('product', product)
    return _upsert_property('products', product, key, values, api_key=api_key,
                            **(request_kwargs or {}))


def upsert_thng_property(thng, key, values, api_key=None, request_kwargs=None):
    """Create/Update a single Property on a Thng.

    POST /thngs/{$thng}/properties/{$key}
    {"value": {$value}}
    """
    assertions.datatype_str('thng', thng)
    return _upsert_property('thngs', thng, key, values, api_key=api_key,
                            **(request_kwargs or {}))


def _upsert_property(entity_type, entity_id, key, values, api_key=None,
                     request_kwargs=None):
    """A helper to wrap common property update functionality."""
    assertions.datatype_str('key', key)
    url = '/{}/{}/properties/{}'.format(entity_type, entity_id, key)
    return utils.request('PUT', url, data=values, api_key=api_key,
                         **(request_kwargs or {}))


# Convenience functions.
create_product_property = upsert_product_property
update_product_property = upsert_product_property


# Update multiple Properties


def upsert_product_properties(product, key_values, api_key=None,
                              request_kwargs=None):
    """Create/Update multiple Properties on a Product.

    POST /products/{$product}/properties
    [{"key": "max_wattage", "value": 40}, {"key": "sku", "value": "abc123"}]
    """
    for key_value in key_values:
        assertions.validate_field_specs(key_value, field_specs)
    return _upsert_properties('products', product, key_values, api_key=api_key,
                              **(request_kwargs or {}))


def upsert_thng_properties(thng, key_values, api_key=None, request_kwargs=None):
    """Create/Update multiple Properties on a Thng.

    POST /thngs/{$thng}/properties
    [{"key": "motion", "value": 20}, {"key": "temperature", "value": 98}]
    """
    for key_value in key_values:
        assertions.validate_field_specs(key_value, field_specs)
    return _upsert_properties('thngs', thng, key_values, api_key=api_key,
                              **(request_kwargs or {}))


def _upsert_properties(entity_type, entity_id, key_values, api_key=None,
                       request_kwargs=None):
    """A helper to wrap common property update functionality."""
    url = '/{}/{}/properties'.format(entity_type, entity_id)
    return utils.request('POST', url, data=key_values, api_key=api_key,
                         **(request_kwargs or {}))


# Convenience functions.
create_thng_properties = upsert_thng_properties
update_thng_properties = upsert_thng_properties


# List All Properties


def list_product_properties(product, from_date=None, to_date=None, api_key=None,
                            request_kwargs=None):
    """List all Properties on a Product."""
    assertions.datatype_str('product', product)
    url = '/products/{}/properties'.format(product)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def list_thng_properties(thng, from_date=None, to_date=None, api_key=None,
                         request_kwargs=None):
    """List all Properties on a thng."""
    assertions.datatype_str('thng', thng)
    url = '/thngs/{}/properties'.format(thng)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


# Read a Property


def _read_property(evrythng, evrythng_type, property_name, timestamp_to=None,
                   timestamp_from=None, api_key=None, request_kwargs=None):
    """Helper for reading properties."""
    assertions.datatype_str('property_name', property_name)
    url = '/{}/{}/properties/{}'.format(evrythng_type, evrythng, property_name)
    query_params = (request_kwargs or {}).get('query_params', {})

    if timestamp_from:
        assertions.datatype_time('timestamp', timestamp_from)
        query_params['from'] = timestamp_from
    if timestamp_to:
        assertions.datatype_time('timestamp', timestamp_to)
        query_params['to'] = timestamp_to

    request_kwargs.update(query_params=query_params)

    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def read_product_property(product, property_name, timestamp_from=None,
                          timestamp_to=None, api_key=None, request_kwargs=None):
    """Read a Product Property."""
    assertions.datatype_str('product', product)
    return _read_property(product, 'products', property_name,
                          timestamp_from=timestamp_from,
                          timestamp_to=timestamp_to, api_key=api_key,
                          **(request_kwargs or {}))


def read_thng_property(thng, property_name, timestamp_from=None,
                       timestamp_to=None, api_key=None, request_kwargs=None):
    """Read a Thng Property."""
    assertions.datatype_str('thng', thng)
    return _read_property(thng, 'thngs', property_name,
                          timestamp_from=timestamp_from,
                          timestamp_to=timestamp_to, api_key=api_key,
                          **(request_kwargs or {}))


# Delete Properties
#
# The only way to delete data points is to append the ?to=Timestamp URL query
# parameter to specify a point in time before which all the data points will
# be removed.
#
# ATTENTION: If the ?to= parameter is not specified, ALL updates of this
# property will be deleted!


def _delete_property(evrythng, evrythng_type, property_name,
                     timestamp_from=None, timestamp_to=None, api_key=None,
                     request_kwargs=None):
    """Helper for deleting properties."""
    assertions.datatype_str('property_name', property_name)
    query_params = {}
    if timestamp_from:
        assertions.datatype_time('timestamp', timestamp_from)
        query_params['from'] = timestamp_from
    if timestamp_to:
        assertions.datatype_time('timestamp', timestamp_to)
        query_params['to'] = timestamp_to
    url = '/{}/{}/properties/{}'.format(evrythng_type, evrythng, property_name)
    return utils.request('DELETE', url, query_params=query_params,
                         api_key=api_key, **(request_kwargs or {}))


def delete_product_property(product, property_name, timestamp_from=None,
                            timestamp_to=None, api_key=None,
                            request_kwargs=None):
    """Delete a Property on a Product."""
    assertions.datatype_str('product', product)
    return _delete_property(product, 'products', property_name,
                            timestamp_from=timestamp_from,
                            timestamp_to=timestamp_to, api_key=api_key,
                            **(request_kwargs or {}))


def delete_thng_property(thng, property_name, timestamp_from=None,
                         timestamp_to=None, api_key=None,
                         request_kwargs=None):
    """Delete a Property on a Thng."""
    assertions.datatype_str('thng', thng)
    return _delete_property(thng, 'thngs', property_name,
                            timestamp_from=timestamp_from,
                            timestamp_to=timestamp_to, api_key=api_key,
                            **(request_kwargs or {}))
