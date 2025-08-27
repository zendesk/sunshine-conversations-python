# IntegrationUpdateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration_update_base import IntegrationUpdateBase

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationUpdateBase from a JSON string
integration_update_base_instance = IntegrationUpdateBase.from_json(json)
# print the JSON string representation of the object
print(IntegrationUpdateBase.to_json())

# convert the object into a dict
integration_update_base_dict = integration_update_base_instance.to_dict()
# create an instance of IntegrationUpdateBase from a dict
integration_update_base_from_dict = IntegrationUpdateBase.from_dict(integration_update_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


