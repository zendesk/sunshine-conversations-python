# MessageOverrideMessenger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messenger** | [**MessageOverridePayload**](MessageOverridePayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_override_messenger import MessageOverrideMessenger

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOverrideMessenger from a JSON string
message_override_messenger_instance = MessageOverrideMessenger.from_json(json)
# print the JSON string representation of the object
print(MessageOverrideMessenger.to_json())

# convert the object into a dict
message_override_messenger_dict = message_override_messenger_instance.to_dict()
# create an instance of MessageOverrideMessenger from a dict
message_override_messenger_from_dict = MessageOverrideMessenger.from_dict(message_override_messenger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


