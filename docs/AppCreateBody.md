# AppCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The friendly name of the app. | 
**settings** | [**AppSettings**](AppSettings.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_create_body import AppCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of AppCreateBody from a JSON string
app_create_body_instance = AppCreateBody.from_json(json)
# print the JSON string representation of the object
print(AppCreateBody.to_json())

# convert the object into a dict
app_create_body_dict = app_create_body_instance.to_dict()
# create an instance of AppCreateBody from a dict
app_create_body_from_dict = AppCreateBody.from_dict(app_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


