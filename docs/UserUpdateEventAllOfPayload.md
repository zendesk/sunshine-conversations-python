# UserUpdateEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) | The updated user. | [optional] 
**reason** | **str** | The reason why the user was updated, if applicable. * &#x60;authentication&#x60; - An unauthenticated user became an [authenticated](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/intro-to-users/) user. * &#x60;localeDetection&#x60; - A user was updated as a result of automated locale detection on messages sent.  | [optional] 
**source** | [**SourceWebhook**](SourceWebhook.md) | The source of the creation. | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_update_event_all_of_payload import UserUpdateEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateEventAllOfPayload from a JSON string
user_update_event_all_of_payload_instance = UserUpdateEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(UserUpdateEventAllOfPayload.to_json())

# convert the object into a dict
user_update_event_all_of_payload_dict = user_update_event_all_of_payload_instance.to_dict()
# create an instance of UserUpdateEventAllOfPayload from a dict
user_update_event_all_of_payload_from_dict = UserUpdateEventAllOfPayload.from_dict(user_update_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


