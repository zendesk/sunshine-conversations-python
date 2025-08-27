# MessageOverrideLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | [**MessageOverridePayload**](MessageOverridePayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_override_line import MessageOverrideLine

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOverrideLine from a JSON string
message_override_line_instance = MessageOverrideLine.from_json(json)
# print the JSON string representation of the object
print(MessageOverrideLine.to_json())

# convert the object into a dict
message_override_line_dict = message_override_line_instance.to_dict()
# create an instance of MessageOverrideLine from a dict
message_override_line_from_dict = MessageOverrideLine.from_dict(message_override_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


