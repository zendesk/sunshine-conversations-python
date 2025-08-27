# TemplateMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'template']
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**template** | **object** | The whatsapp template message to send. For more information, consult the [guide](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/message-overrides/#template-messages). &#x60;schema&#x60; must be set to &#x60;whatsapp&#x60;. | 

## Example

```python
from sunshine_conversations_client.model.template_message import TemplateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateMessage from a JSON string
template_message_instance = TemplateMessage.from_json(json)
# print the JSON string representation of the object
print(TemplateMessage.to_json())

# convert the object into a dict
template_message_dict = template_message_instance.to_dict()
# create an instance of TemplateMessage from a dict
template_message_from_dict = TemplateMessage.from_dict(template_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


