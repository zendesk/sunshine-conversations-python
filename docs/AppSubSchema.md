# AppSubSchema

The app that triggered the events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the app. | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_sub_schema import AppSubSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubSchema from a JSON string
app_sub_schema_instance = AppSubSchema.from_json(json)
# print the JSON string representation of the object
print(AppSubSchema.to_json())

# convert the object into a dict
app_sub_schema_dict = app_sub_schema_instance.to_dict()
# create an instance of AppSubSchema from a dict
app_sub_schema_from_dict = AppSubSchema.from_dict(app_sub_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


