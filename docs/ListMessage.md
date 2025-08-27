# ListMessage

List messages are a vertically scrollable set of items that may each contain text, an image, and message actions. Not all messaging channels fully support list messages. * Facebook Messenger and WeChat have native support. * For LINE and our Android, iOS and Web SDK, Sunshine Conversations converts list messages to carousel. * On WhatsApp, Telegram and Twitter, Sunshine Conversations converts list messages to multiple rich messages. * On all other platforms, Sunshine Conversations converts list messages to raw text. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'list']
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**items** | [**List[Item]**](Item.md) | An array of objects representing the items associated with the message. Only present in carousel and list type messages. | 
**actions** | [**List[ActionSubset]**](ActionSubset.md) | An array of objects representing the actions associated with the message. The array length is limited by the third party channel. | [optional] 

## Example

```python
from sunshine_conversations_client.model.list_message import ListMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ListMessage from a JSON string
list_message_instance = ListMessage.from_json(json)
# print the JSON string representation of the object
print(ListMessage.to_json())

# convert the object into a dict
list_message_dict = list_message_instance.to_dict()
# create an instance of ListMessage from a dict
list_message_from_dict = ListMessage.from_dict(list_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


