# Target

The target conversation to attach the client to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | The conversation ID of the target conversation. | 

## Example

```python
from sunshine_conversations_client.model.target import Target

# TODO update the JSON string below
json = "{}"
# create an instance of Target from a JSON string
target_instance = Target.from_json(json)
# print the JSON string representation of the object
print(Target.to_json())

# convert the object into a dict
target_dict = target_instance.to_dict()
# create an instance of Target from a dict
target_from_dict = Target.from_dict(target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


