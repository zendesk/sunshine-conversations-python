# UserRemoveEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserTruncated**](UserTruncated.md) | The user that was removed. | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_remove_event_all_of_payload import UserRemoveEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserRemoveEventAllOfPayload from a JSON string
user_remove_event_all_of_payload_instance = UserRemoveEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(UserRemoveEventAllOfPayload.to_json())

# convert the object into a dict
user_remove_event_all_of_payload_dict = user_remove_event_all_of_payload_instance.to_dict()
# create an instance of UserRemoveEventAllOfPayload from a dict
user_remove_event_all_of_payload_from_dict = UserRemoveEventAllOfPayload.from_dict(user_remove_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


