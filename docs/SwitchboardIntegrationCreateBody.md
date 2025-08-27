# SwitchboardIntegrationCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identifier for use in control transfer protocols. Restricted to alphanumeric characters, &#x60;-&#x60; and &#x60;_&#x60;. | 
**integration_id** | **str** | The id of the integration to link to the switchboard integration. Must be used when linking a custom integration. One of &#x60;integrationId&#x60; or &#x60;integrationType&#x60; must be provided. | [optional] 
**integration_type** | **str** | The type of the integration to link to the switchboard integration. Must be used when linking an OAuth integration. One of &#x60;integrationId&#x60; or &#x60;integrationType&#x60; must be provided. | [optional] 
**deliver_standby_events** | **bool** | Setting to determine if webhooks should be sent when the switchboard integration is not in control of a conversation (standby status) | [optional] 
**next_switchboard_integration_id** | **str** | The switchboard integration id to which control of a conversation is passed / offered by default. | [optional] 
**message_history_count** | **int** | Number of messages to include in the message history context. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_integration_create_body import SwitchboardIntegrationCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardIntegrationCreateBody from a JSON string
switchboard_integration_create_body_instance = SwitchboardIntegrationCreateBody.from_json(json)
# print the JSON string representation of the object
print(SwitchboardIntegrationCreateBody.to_json())

# convert the object into a dict
switchboard_integration_create_body_dict = switchboard_integration_create_body_instance.to_dict()
# create an instance of SwitchboardIntegrationCreateBody from a dict
switchboard_integration_create_body_from_dict = SwitchboardIntegrationCreateBody.from_dict(switchboard_integration_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


