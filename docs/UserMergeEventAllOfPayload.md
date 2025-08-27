# UserMergeEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merged_users** | [**UserMergeEventAllOfPayloadMergedUsers**](UserMergeEventAllOfPayloadMergedUsers.md) |  | [optional] 
**merged_conversations** | [**UserMergeEventAllOfPayloadMergedConversations**](UserMergeEventAllOfPayloadMergedConversations.md) |  | [optional] 
**merged_clients** | [**UserMergeEventAllOfPayloadMergedClients**](UserMergeEventAllOfPayloadMergedClients.md) |  | [optional] 
**discarded_metadata** | **Dict[str, object]** | A flat object with the set of metadata properties that were discarded when merging the two users. This should contain values only if the combined metadata fields exceed the 4KB limit. | [optional] 
**reason** | **str** | The reason for which the users merged. * &#x60;api&#x60; - The users were merged using the API. * &#x60;channelLinking&#x60; - The users were merged as a result of initiating a channel link. * &#x60;sdkLogin&#x60; - The users were merged as a result of logging into an SDK device.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_merge_event_all_of_payload import UserMergeEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserMergeEventAllOfPayload from a JSON string
user_merge_event_all_of_payload_instance = UserMergeEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(UserMergeEventAllOfPayload.to_json())

# convert the object into a dict
user_merge_event_all_of_payload_dict = user_merge_event_all_of_payload_instance.to_dict()
# create an instance of UserMergeEventAllOfPayload from a dict
user_merge_event_all_of_payload_from_dict = UserMergeEventAllOfPayload.from_dict(user_merge_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


