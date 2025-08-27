# UserMergeEventAllOfPayloadMergedUsers

Contains information about the users that were merged together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surviving** | [**User**](User.md) | The user that now represents the merged user object. | [optional] 
**discarded** | [**User**](User.md) | The user that was unified into the surviving user object. | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_merge_event_all_of_payload_merged_users import UserMergeEventAllOfPayloadMergedUsers

# TODO update the JSON string below
json = "{}"
# create an instance of UserMergeEventAllOfPayloadMergedUsers from a JSON string
user_merge_event_all_of_payload_merged_users_instance = UserMergeEventAllOfPayloadMergedUsers.from_json(json)
# print the JSON string representation of the object
print(UserMergeEventAllOfPayloadMergedUsers.to_json())

# convert the object into a dict
user_merge_event_all_of_payload_merged_users_dict = user_merge_event_all_of_payload_merged_users_instance.to_dict()
# create an instance of UserMergeEventAllOfPayloadMergedUsers from a dict
user_merge_event_all_of_payload_merged_users_from_dict = UserMergeEventAllOfPayloadMergedUsers.from_dict(user_merge_event_all_of_payload_merged_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


