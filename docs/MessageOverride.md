# MessageOverride

A raw payload containing a message that is sent directly to a channel. See [message overrides](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/message-overrides/) for more information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple** | [**AppleMessageOverridePayload**](AppleMessageOverridePayload.md) |  | [optional] 
**line** | [**MessageOverridePayload**](MessageOverridePayload.md) |  | [optional] 
**messenger** | [**MessageOverridePayload**](MessageOverridePayload.md) |  | [optional] 
**whatsapp** | [**MessageOverridePayload**](MessageOverridePayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_override import MessageOverride

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOverride from a JSON string
message_override_instance = MessageOverride.from_json(json)
# print the JSON string representation of the object
print(MessageOverride.to_json())

# convert the object into a dict
message_override_dict = message_override_instance.to_dict()
# create an instance of MessageOverride from a dict
message_override_from_dict = MessageOverride.from_dict(message_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


