# AppKeyCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the API key. | 

## Example

```python
from sunshine_conversations_client.model.app_key_create_body import AppKeyCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of AppKeyCreateBody from a JSON string
app_key_create_body_instance = AppKeyCreateBody.from_json(json)
# print the JSON string representation of the object
print(AppKeyCreateBody.to_json())

# convert the object into a dict
app_key_create_body_dict = app_key_create_body_instance.to_dict()
# create an instance of AppKeyCreateBody from a dict
app_key_create_body_from_dict = AppKeyCreateBody.from_dict(app_key_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


