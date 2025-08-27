# CustomUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 

## Example

```python
from sunshine_conversations_client.model.custom_update import CustomUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomUpdate from a JSON string
custom_update_instance = CustomUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomUpdate.to_json())

# convert the object into a dict
custom_update_dict = custom_update_instance.to_dict()
# create an instance of CustomUpdate from a dict
custom_update_from_dict = CustomUpdate.from_dict(custom_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


