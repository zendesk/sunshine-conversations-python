# ActivityTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | If the author type is &#x60;user&#x60;, only &#x60;conversation:read&#x60; is supported. | [optional] 

## Example

```python
from sunshine_conversations_client.model.activity_types import ActivityTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTypes from a JSON string
activity_types_instance = ActivityTypes.from_json(json)
# print the JSON string representation of the object
print(ActivityTypes.to_json())

# convert the object into a dict
activity_types_dict = activity_types_instance.to_dict()
# create an instance of ActivityTypes from a dict
activity_types_from_dict = ActivityTypes.from_dict(activity_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


