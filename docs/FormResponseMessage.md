# FormResponseMessage

A formResponse type message is a response to a form type message. formResponse type messages are only supported as responses to form messages on Web Messenger and cannot be sent via the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'formResponse']
**fields** | [**List[FormResponseMessageField]**](FormResponseMessageField.md) | Array of field objects that contain the submitted fields. | 
**text_fallback** | **str** | A string containing the &#x60;label: value&#x60; of all fields, each separated by a newline character. | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.form_response_message import FormResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FormResponseMessage from a JSON string
form_response_message_instance = FormResponseMessage.from_json(json)
# print the JSON string representation of the object
print(FormResponseMessage.to_json())

# convert the object into a dict
form_response_message_dict = form_response_message_instance.to_dict()
# create an instance of FormResponseMessage from a dict
form_response_message_from_dict = FormResponseMessage.from_dict(form_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


