# AppResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**App**](App.md) | The app. | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_response import AppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppResponse from a JSON string
app_response_instance = AppResponse.from_json(json)
# print the JSON string representation of the object
print(AppResponse.to_json())

# convert the object into a dict
app_response_dict = app_response_instance.to_dict()
# create an instance of AppResponse from a dict
app_response_from_dict = AppResponse.from_dict(app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


