# AppKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the API key, used when signing JWTs or accessing the API using Basic Authentication. | [optional] 
**display_name** | **str** | The name of the API key. | [optional] 
**secret** | **str** | The secret of the API key, used when signing JWTs or accessing the API using Basic Authentication | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_key import AppKey

# TODO update the JSON string below
json = "{}"
# create an instance of AppKey from a JSON string
app_key_instance = AppKey.from_json(json)
# print the JSON string representation of the object
print(AppKey.to_json())

# convert the object into a dict
app_key_dict = app_key_instance.to_dict()
# create an instance of AppKey from a dict
app_key_from_dict = AppKey.from_dict(app_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


