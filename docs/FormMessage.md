# FormMessage

A form type message without text or actions. Only supported in the Web SDK.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'form']
**submitted** | **bool** | Flag which states whether the form is submitted. | [optional] [readonly] 
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation.. | [optional] 
**fields** | [**List[FormMessageField]**](FormMessageField.md) | An array of objects representing fields associated with the message. Only present in form and formResponse messages. | 

## Example

```python
from sunshine_conversations_client.model.form_message import FormMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FormMessage from a JSON string
form_message_instance = FormMessage.from_json(json)
# print the JSON string representation of the object
print(FormMessage.to_json())

# convert the object into a dict
form_message_dict = form_message_instance.to_dict()
# create an instance of FormMessage from a dict
form_message_from_dict = FormMessage.from_dict(form_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


