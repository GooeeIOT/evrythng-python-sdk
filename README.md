# python-evrythng

A comprehensive pythonic wrapper around the Evrythng REST API.

This project is currently in heavy development. We are creating a rough basic
entity API first. Then we will iterate off of that and refactor commonalities
into something worth using.

Though mostly usable, it hasn't reached a production build. Also, things are
pretty naive at the moment... much refactoring needs to take place.

### Supported Entities

- Projects
- Applications
- Application Users
- Products
- Thngs
- Properties
- Actions
- Action Types
- Locations
- Collections
- Places

(Filters are coming soon, but not currently supported)

### ToDo

- Probably need to define all Entity arguments as kwarguments?
- Complete datatype_list_of_social_networks
- Add filtering where possible (ie, list pages)
- Re-factor repeated repetative things out to keep things DRY
- Implement Service APIs
- Alias endpoints
    - /products/:productId/actions/:actionType
    - /thngs/:thngId/actions/:actionType
    - /collections/:collectionId/actions/:actionType
- 'to' parameter in delete_location
- Config options singleton (so you don't have to pass api_key everywhere)
- Add more examples
- Sphinx generated documentation
- Create a (locally installable) pip package
