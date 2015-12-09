from evrythng import utils


def create_project(name=None, description=None, startsAt=None, endsAt=None,
                   tags=None, shortDomains=None, api_key=None):
    datatype_specs = {
        'name': 'str',
        'description': 'str',
        'startsAt': 'time',
        'endsAt': 'time',
        'tags': 'list|str',
        'shortDomains': 'list|str',
        'customFields': 'dict',
    }
    required_fields = ('name',)
    readonly_fields = ('id', 'createdAt', 'updatedAt')
    writable_fields = ('description', 'startsAt', 'endsAt', 'tags')

    kwargs = locals()
    api_key = kwargs.pop('api_key')

    utils.assert_required(kwargs, required_fields)
    utils.assert_readonly(kwargs, readonly_fields)
    utils.assert_no_extras(kwargs, required_fields + writable_fields)
    utils.assert_datatypes(kwargs, datatype_specs)

    # utils.request('POST', '/projects', data, api_key=api_key)
