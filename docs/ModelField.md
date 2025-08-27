# ModelField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The field type. | 
**name** | **str** | The name of the field. Must be unique per form or formResponse. | 
**label** | **str** | The label of the field. What the field is displayed as on Web Messenger. | 
**text** | **str** | Specifies the response for a text field. | [optional] 
**email** | **str** | Specifies the response for a email field. | [optional] 
**select** | **List[object]** | Array of objects representing the response for a field of type select. Form and formResponse messages only. | [optional] 

## Example

```python
from sunshine_conversations_client.model.model_field import ModelField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelField from a JSON string
model_field_instance = ModelField.from_json(json)
# print the JSON string representation of the object
print(ModelField.to_json())

# convert the object into a dict
model_field_dict = model_field_instance.to_dict()
# create an instance of ModelField from a dict
model_field_from_dict = ModelField.from_dict(model_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


