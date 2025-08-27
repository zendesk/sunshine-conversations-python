# AppKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**AppKey**](AppKey.md) | The created key object. | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_key_response import AppKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppKeyResponse from a JSON string
app_key_response_instance = AppKeyResponse.from_json(json)
# print the JSON string representation of the object
print(AppKeyResponse.to_json())

# convert the object into a dict
app_key_response_dict = app_key_response_instance.to_dict()
# create an instance of AppKeyResponse from a dict
app_key_response_from_dict = AppKeyResponse.from_dict(app_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


