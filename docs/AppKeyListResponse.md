# AppKeyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[AppKey]**](AppKey.md) | List of returned keys. | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_key_list_response import AppKeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppKeyListResponse from a JSON string
app_key_list_response_instance = AppKeyListResponse.from_json(json)
# print the JSON string representation of the object
print(AppKeyListResponse.to_json())

# convert the object into a dict
app_key_list_response_dict = app_key_list_response_instance.to_dict()
# create an instance of AppKeyListResponse from a dict
app_key_list_response_from_dict = AppKeyListResponse.from_dict(app_key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


