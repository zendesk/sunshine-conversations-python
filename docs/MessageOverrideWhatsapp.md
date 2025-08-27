# MessageOverrideWhatsapp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whatsapp** | [**MessageOverridePayload**](MessageOverridePayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_override_whatsapp import MessageOverrideWhatsapp

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOverrideWhatsapp from a JSON string
message_override_whatsapp_instance = MessageOverrideWhatsapp.from_json(json)
# print the JSON string representation of the object
print(MessageOverrideWhatsapp.to_json())

# convert the object into a dict
message_override_whatsapp_dict = message_override_whatsapp_instance.to_dict()
# create an instance of MessageOverrideWhatsapp from a dict
message_override_whatsapp_from_dict = MessageOverrideWhatsapp.from_dict(message_override_whatsapp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


