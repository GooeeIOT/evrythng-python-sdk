# python-evrythng

A comprehensive pythonic wrapper around the Evrythng REST API.

This project is currently in heavy development. We are creating a rough basic
entity API first. Then we will iterate off of that and refactor commonalities
into something worth using.

Though mostly usable, it hasn't reached a production build. Also, things are
pretty naive at the moment... much refactoring needs to take place.

NOTE: Filters are generally unsupported at the moment. It's an ASAP.

### ToDo

probably need to define all entitiy arguments as kwarguments?

- complete datatype_list_of_social_networks
- add filtering where possible (ie, list pages)
- refactor repeated repetative things out to keep things DRY
- implement Service APIs
- Alias endpoints
    - /products/:productId/actions/:actionType
    - /thngs/:thngId/actions/:actionType
    - /collections/:collectionId/actions/:actionType
- 'to' parameter in delete_location
- config options singleton (so you don't have to pass api_key everywhere)
- add more examples
- Sphinx generated documentation
- create a (locally installable) pip package
