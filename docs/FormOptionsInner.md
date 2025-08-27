# FormOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the option. What the option is displayed as on Web Messenger. | [optional] 
**name** | **str** | The name of the field. Must be unique per field. | [optional] 

## Example

```python
from sunshine_conversations_client.model.form_options_inner import FormOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormOptionsInner from a JSON string
form_options_inner_instance = FormOptionsInner.from_json(json)
# print the JSON string representation of the object
print(FormOptionsInner.to_json())

# convert the object into a dict
form_options_inner_dict = form_options_inner_instance.to_dict()
# create an instance of FormOptionsInner from a dict
form_options_inner_from_dict = FormOptionsInner.from_dict(form_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


