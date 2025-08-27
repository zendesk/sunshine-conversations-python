# Integration

The integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the integration. | [optional] [readonly] 
**type** | **str** |  | 
**status** | [**Status**](Status.md) |  | [optional] 
**display_name** | **str** | A human-friendly name used to identify the integration. | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration import Integration

# TODO update the JSON string below
json = "{}"
# create an instance of Integration from a JSON string
integration_instance = Integration.from_json(json)
# print the JSON string representation of the object
print(Integration.to_json())

# convert the object into a dict
integration_dict = integration_instance.to_dict()
# create an instance of Integration from a dict
integration_from_dict = Integration.from_dict(integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


