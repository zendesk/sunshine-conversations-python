# IntegrationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_type** | **str** | The type of the integration to deliver the message to. Can be set to &#x60;none&#x60; if sending a [silent message](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/sending-messages/#silent-messages). Will return an error if the user does not have a client of that type attached to the conversation.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration_type import IntegrationType

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationType from a JSON string
integration_type_instance = IntegrationType.from_json(json)
# print the JSON string representation of the object
print(IntegrationType.to_json())

# convert the object into a dict
integration_type_dict = integration_type_instance.to_dict()
# create an instance of IntegrationType from a dict
integration_type_from_dict = IntegrationType.from_dict(integration_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


