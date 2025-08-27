# MessagePostResponse

The created messages. A single request may produce multiple messages when the shorthand syntax is used to send a template message with leading text.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_post_response import MessagePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePostResponse from a JSON string
message_post_response_instance = MessagePostResponse.from_json(json)
# print the JSON string representation of the object
print(MessagePostResponse.to_json())

# convert the object into a dict
message_post_response_dict = message_post_response_instance.to_dict()
# create an instance of MessagePostResponse from a dict
message_post_response_from_dict = MessagePostResponse.from_dict(message_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


