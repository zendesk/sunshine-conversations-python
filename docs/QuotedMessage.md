# QuotedMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of quotedMessage - &#x60;externalMessageId&#x60; if no Sunshine Conversations message matched the quoted message. | [default to 'externalMessageId']
**message** | [**Message**](Message.md) |  | [optional] 
**external_message_id** | **str** | The external message Id of the quoted message. | [optional] 

## Example

```python
from sunshine_conversations_client.model.quoted_message import QuotedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of QuotedMessage from a JSON string
quoted_message_instance = QuotedMessage.from_json(json)
# print the JSON string representation of the object
print(QuotedMessage.to_json())

# convert the object into a dict
quoted_message_dict = quoted_message_instance.to_dict()
# create an instance of QuotedMessage from a dict
quoted_message_from_dict = QuotedMessage.from_dict(quoted_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


