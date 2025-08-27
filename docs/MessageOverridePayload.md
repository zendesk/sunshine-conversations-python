# MessageOverridePayload

The exact payload to send to the channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **object** |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_override_payload import MessageOverridePayload

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOverridePayload from a JSON string
message_override_payload_instance = MessageOverridePayload.from_json(json)
# print the JSON string representation of the object
print(MessageOverridePayload.to_json())

# convert the object into a dict
message_override_payload_dict = message_override_payload_instance.to_dict()
# create an instance of MessageOverridePayload from a dict
message_override_payload_from_dict = MessageOverridePayload.from_dict(message_override_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


