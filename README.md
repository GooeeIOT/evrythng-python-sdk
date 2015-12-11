# python-evrythng

A comprehensive pythonic wrapper around the Evrythng REST API.

This project is currently in development.

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
- Alias endpoints
    /products/:productId/actions/:actionType
    /thngs/:thngId/actions/:actionType
    /collections/:collectionId/actions/:actionType
- 'to' parameter in delete_location
- fill out datatype_list_of_social_networks
- config options singleton
- add examples
- create a (locally installable) pip package
