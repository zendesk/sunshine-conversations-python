# AppListFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_id** | **str** | When specified, lists only the apps that the service account has access to. | [optional] 

## Example

```python
from sunshine_conversations_client.model.app_list_filter import AppListFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppListFilter from a JSON string
app_list_filter_instance = AppListFilter.from_json(json)
# print the JSON string representation of the object
print(AppListFilter.to_json())

# convert the object into a dict
app_list_filter_dict = app_list_filter_instance.to_dict()
# create an instance of AppListFilter from a dict
app_list_filter_from_dict = AppListFilter.from_dict(app_list_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


