# FormMessageField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The field type. | 
**name** | **str** | The name of the field. Must be unique per form or formResponse. | 
**label** | **str** | The label of the field. What the field is displayed as on Web Messenger. | 
**text** | **str** | Specifies the response for a text field. | [optional] 
**email** | **str** | Specifies the response for a email field. | [optional] 
**select** | **List[object]** | Array of objects representing the response for a field of type select. Form and formResponse messages only. | [optional] 
**placeholder** | **str** | Placeholder text for the field. Form message only. | [optional] 
**min_size** | **int** | The minimum allowed length for the response for a field of type text. Form message only. | [optional] [default to 1]
**max_size** | **int** | The maximum allowed length for the response for a field of type text. Form message only. | [optional] [default to 128]
**options** | [**List[FormOptionsInner]**](FormOptionsInner.md) | Array of objects representing options for a field of type select. | [optional] 

## Example

```python
from sunshine_conversations_client.model.form_message_field import FormMessageField

# TODO update the JSON string below
json = "{}"
# create an instance of FormMessageField from a JSON string
form_message_field_instance = FormMessageField.from_json(json)
# print the JSON string representation of the object
print(FormMessageField.to_json())

# convert the object into a dict
form_message_field_dict = form_message_field_instance.to_dict()
# create an instance of FormMessageField from a dict
form_message_field_from_dict = FormMessageField.from_dict(form_message_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


