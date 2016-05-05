Python Everythng
================
A comprehensive pythonic wrapper around the Evrythng REST API.

.. image:: https://img.shields.io/pypi/v/python-evrythng.svg
    :target: https://pypi.python.org/pypi/python-evrythng

.. image:: https://img.shields.io/pypi/dm/python-evrythng.svg
        :target: https://pypi.python.org/pypi/python-evrythng
        
.. image:: https://img.shields.io/twitter/url/https/pypi.python.org/pypi/python-evrythng.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D

More information about Evrythng may be found in its
`Documentation <https://dashboard.evrythng.com/documentation/api>`_.

python_evrythng is available on PyPI and can be installed via pip.

.. code-block:: bash

    $ pip install python_evrythng

License
===============================================================================
.. image:: https://raw.githubusercontent.com/GooeeIOT/python-evrythng/master/docs/gooee.png

Copyright (c) 2016, Gooee™ LLC.All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

Notice
=============================================================================

This project is currently in heavy development. We are creating a rough basic
entity API first. Then we will iterate off of that and refactor commonalities
into something worth using.

Though mostly usable, it hasn't reached a production build. Also, things are
pretty naive at the moment... much refactoring needs to take place.

**Supported Entities:**

* Projects
* Applications
* Application Users
* Products
* Thngs
* Properties
* Actions
* Action Types
* Locations
* Collections
* Places


**TODO:**

* Probably need to define all Entity arguments as kwarguments?
* Complete datatype_list_of_social_networks
* Add filtering where possible (ie, list pages)
* Re-factor repeated repetative things out to keep things DRY
* Implement Service APIs
* Alias endpoints
    * */products/:productId/actions/:actionType*
    * */thngs/:thngId/actions/:actionType*
    * */collections/:collectionId/actions/:actionType*
* 'to' parameter in delete_location
* Config options singleton (so you don't have to pass api_key everywhere)
* Add usage examples
* Sphinx generated documentation
* Add pagination limit support

Found a bug, wanna help?
==============================================================================
Awesome, let us know! Send a pull request or a patch. Ask! We are here to help 
and will respond to all filed issues.
