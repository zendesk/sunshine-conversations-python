# Confirmation

The confirmation options of the link request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of confirmation. | 
**message** | [**MessagePost**](MessagePost.md) | The message used to reach out to the user, if desired. Messages sent via this method can only be of type text and image. If actions are included they can only be of type link. The confirmation message will not be added to the user’s conversation. | [optional] 

## Example

```python
from sunshine_conversations_client.model.confirmation import Confirmation

# TODO update the JSON string below
json = "{}"
# create an instance of Confirmation from a JSON string
confirmation_instance = Confirmation.from_json(json)
# print the JSON string representation of the object
print(Confirmation.to_json())

# convert the object into a dict
confirmation_dict = confirmation_instance.to_dict()
# create an instance of Confirmation from a dict
confirmation_from_dict = Confirmation.from_dict(confirmation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


