# IntegrationListFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **str** | Comma-separated list of types to return. If omitted, all types are returned. | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration_list_filter import IntegrationListFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationListFilter from a JSON string
integration_list_filter_instance = IntegrationListFilter.from_json(json)
# print the JSON string representation of the object
print(IntegrationListFilter.to_json())

# convert the object into a dict
integration_list_filter_dict = integration_list_filter_instance.to_dict()
# create an instance of IntegrationListFilter from a dict
integration_list_filter_from_dict = IntegrationListFilter.from_dict(integration_list_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


