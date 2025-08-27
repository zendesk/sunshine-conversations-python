# SwitchboardIntegrationWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the switchboard integration. | [optional] 
**name** | **str** | Identifier for use in control transfer protocols. Restricted to alphanumeric characters, &#x60;-&#x60; and &#x60;_&#x60;. | [optional] 
**integration_id** | **str** | Id of the integration that should deliver events routed by the switchboard. | [optional] 
**integration_type** | **str** | Type of integration that should deliver events routed by the switchboard. If referencing an OAuth integration, the clientId issued by Sunshine Conversations during the OAuth partnership process will be the value of integrationType. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_integration_webhook import SwitchboardIntegrationWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardIntegrationWebhook from a JSON string
switchboard_integration_webhook_instance = SwitchboardIntegrationWebhook.from_json(json)
# print the JSON string representation of the object
print(SwitchboardIntegrationWebhook.to_json())

# convert the object into a dict
switchboard_integration_webhook_dict = switchboard_integration_webhook_instance.to_dict()
# create an instance of SwitchboardIntegrationWebhook from a dict
switchboard_integration_webhook_from_dict = SwitchboardIntegrationWebhook.from_dict(switchboard_integration_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


