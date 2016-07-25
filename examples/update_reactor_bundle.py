from evrythng.extended import reactor

project_id = ''
application_id = ''
api_key = ''
path = '/path/to/bundle.zip'

response = reactor.update_reactor_bundle(
    project_id,
    application_id,
    open(path, 'rb'),
    api_key=api_key
)
print(response)
print(response.text)
