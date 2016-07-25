from evrythng.extended import reactor

project_id = ''
application_id = ''
api_key = ''

script = """
function onThngPropertiesChanged(event) {
    logger.debug('CHANGE!' + JSON.stringify(event));
    done();
}
"""

manifest = """
{
    "name": "tester",
    "version": "0.0.1"
}
"""

response = reactor.update_reactor_script(
    project_id, application_id, script, manifest,
    api_key=api_key)
print(response)
print(response.text)
