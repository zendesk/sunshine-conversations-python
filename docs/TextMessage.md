# TextMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'text']
**text** | **str** | The text content of the message. Required unless &#x60;actions&#x60;, &#x60;htmlText&#x60; or &#x60;markdownText&#x60; is provided. | [optional] 
**html_text** | **str** | HTML text content of the message. Can be provided in place of &#x60;text&#x60;. Cannot be used with &#x60;markdownText&#x60;. If no &#x60;text&#x60; is provided, will be converted to &#x60;text&#x60; upon reception to be displayed on channels that do not support rich text. See [rich text](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/structured-messages/#rich-text) documentation for more information. | [optional] 
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**markdown_text** | **str** | Markdown text content of the message. Can be provided in place of &#x60;text&#x60;. Cannot be used with &#x60;htmlText&#x60;. Will be converted to &#x60;htmlText&#x60; upon reception. If converted &#x60;htmlText&#x60; exceeds 4096 characters, the message will be rejected. If no &#x60;text&#x60; is provided, will be converted to &#x60;text&#x60; upon reception to be displayed on channels that do not support rich text. See [rich text](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/structured-messages/#rich-text) documentation for more information. | [optional] 
**actions** | [**List[Action]**](Action.md) | Array of message actions. | [optional] 
**payload** | **str** | The payload of a [reply button](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/structured-messages/#reply-buttons) response message. | [optional] 

## Example

```python
from sunshine_conversations_client.model.text_message import TextMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessage from a JSON string
text_message_instance = TextMessage.from_json(json)
# print the JSON string representation of the object
print(TextMessage.to_json())

# convert the object into a dict
text_message_dict = text_message_instance.to_dict()
# create an instance of TextMessage from a dict
text_message_from_dict = TextMessage.from_dict(text_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


