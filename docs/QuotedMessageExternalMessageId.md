# QuotedMessageExternalMessageId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of quotedMessage - &#x60;externalMessageId&#x60; if no Sunshine Conversations message matched the quoted message. | [default to 'externalMessageId']
**external_message_id** | **str** | The external message Id of the quoted message. | [optional] 

## Example

```python
from sunshine_conversations_client.model.quoted_message_external_message_id import QuotedMessageExternalMessageId

# TODO update the JSON string below
json = "{}"
# create an instance of QuotedMessageExternalMessageId from a JSON string
quoted_message_external_message_id_instance = QuotedMessageExternalMessageId.from_json(json)
# print the JSON string representation of the object
print(QuotedMessageExternalMessageId.to_json())

# convert the object into a dict
quoted_message_external_message_id_dict = quoted_message_external_message_id_instance.to_dict()
# create an instance of QuotedMessageExternalMessageId from a dict
quoted_message_external_message_id_from_dict = QuotedMessageExternalMessageId.from_dict(quoted_message_external_message_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


