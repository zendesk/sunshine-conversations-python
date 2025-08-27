# FormResponseMessageField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The field type. | 
**name** | **str** | The name of the field. Must be unique per form or formResponse. | 
**label** | **str** | The label of the field. What the field is displayed as on Web Messenger. | 
**text** | **str** | Specifies the response for a text field. | [optional] 
**email** | **str** | Specifies the response for a email field. | [optional] 
**select** | **List[object]** | Array of objects representing the response for a field of type select. Form and formResponse messages only. | [optional] 
**quoted_message_id** | **str** | The messageId for the form that this response belongs to. | [optional] 

## Example

```python
from sunshine_conversations_client.model.form_response_message_field import FormResponseMessageField

# TODO update the JSON string below
json = "{}"
# create an instance of FormResponseMessageField from a JSON string
form_response_message_field_instance = FormResponseMessageField.from_json(json)
# print the JSON string representation of the object
print(FormResponseMessageField.to_json())

# convert the object into a dict
form_response_message_field_dict = form_response_message_field_instance.to_dict()
# create an instance of FormResponseMessageField from a dict
form_response_message_field_from_dict = FormResponseMessageField.from_dict(form_response_message_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


