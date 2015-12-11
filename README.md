# python-evrythng

A comprehensive pythonic wrapper around the Evrythng REST API.

This project is currently in development. It hasn't quite reached a usable
alpha, though that will happen soon. This status will be updated accordingly.

### Supported Entities

- Projects  
- Applications  
- Application Users  
- Products  
- Thngs  
- ~~Properties~~ (started, need to finish)  
- Actions
- ~~Action Types~~ (mostly done. waiting on proper documentation)
- Locations
- ~~Collections~~  
- ~~Places~~  

### ToDo

- refactor repeated repetative things out. DRY
- add query param support for GET /actions/:actionType
- add query param support for GET /places
- Alias endpoints
    - /products/:productId/actions/:actionType
    - /thngs/:thngId/actions/:actionType
    - /collections/:collectionId/actions/:actionType
- 'to' parameter in delete_location
- fill out datatype_list_of_social_networks
- config options singleton
- add examples
- create a (locally installable) pip package
