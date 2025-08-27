# QuotedMessageMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of quotedMessage - a complete Sunshine Conversations message is provided. | [default to 'message']
**message** | [**Message**](Message.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.quoted_message_message import QuotedMessageMessage

# TODO update the JSON string below
json = "{}"
# create an instance of QuotedMessageMessage from a JSON string
quoted_message_message_instance = QuotedMessageMessage.from_json(json)
# print the JSON string representation of the object
print(QuotedMessageMessage.to_json())

# convert the object into a dict
quoted_message_message_dict = quoted_message_message_instance.to_dict()
# create an instance of QuotedMessageMessage from a dict
quoted_message_message_from_dict = QuotedMessageMessage.from_dict(quoted_message_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


