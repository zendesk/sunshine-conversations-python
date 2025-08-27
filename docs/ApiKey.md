# ApiKey

The integration key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the API key, used when signing JWTs or accessing the API using Basic Authentication. | [optional] 
**display_name** | **str** | The name of the API key. | [optional] 
**secret** | **str** | The secret of the API key, used when signing JWTs or accessing the API using Basic Authentication | [optional] 

## Example

```python
from sunshine_conversations_client.model.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_from_dict = ApiKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


