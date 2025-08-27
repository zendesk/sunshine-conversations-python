# MessageListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) | List of returned messages. | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_list_response import MessageListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageListResponse from a JSON string
message_list_response_instance = MessageListResponse.from_json(json)
# print the JSON string representation of the object
print(MessageListResponse.to_json())

# convert the object into a dict
message_list_response_dict = message_list_response_instance.to_dict()
# create an instance of MessageListResponse from a dict
message_list_response_from_dict = MessageListResponse.from_dict(message_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


