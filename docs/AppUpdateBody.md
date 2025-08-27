# AppUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The friendly name of the app. | [optional] 
**settings** | [**AppSettings**](AppSettings.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_update_body import AppUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of AppUpdateBody from a JSON string
app_update_body_instance = AppUpdateBody.from_json(json)
# print the JSON string representation of the object
print(AppUpdateBody.to_json())

# convert the object into a dict
app_update_body_dict = app_update_body_instance.to_dict()
# create an instance of AppUpdateBody from a dict
app_update_body_from_dict = AppUpdateBody.from_dict(app_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


