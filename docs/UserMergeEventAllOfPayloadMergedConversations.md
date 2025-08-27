# UserMergeEventAllOfPayloadMergedConversations

Contains information about the conversations that were merged together as a result of the operation, if applicable. If no conversations were merged, this property is omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surviving** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation that now represents the merged conversation object. | [optional] 
**discarded** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation that was unified into the surviving conversation object. | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_merge_event_all_of_payload_merged_conversations import UserMergeEventAllOfPayloadMergedConversations

# TODO update the JSON string below
json = "{}"
# create an instance of UserMergeEventAllOfPayloadMergedConversations from a JSON string
user_merge_event_all_of_payload_merged_conversations_instance = UserMergeEventAllOfPayloadMergedConversations.from_json(json)
# print the JSON string representation of the object
print(UserMergeEventAllOfPayloadMergedConversations.to_json())

# convert the object into a dict
user_merge_event_all_of_payload_merged_conversations_dict = user_merge_event_all_of_payload_merged_conversations_instance.to_dict()
# create an instance of UserMergeEventAllOfPayloadMergedConversations from a dict
user_merge_event_all_of_payload_merged_conversations_from_dict = UserMergeEventAllOfPayloadMergedConversations.from_dict(user_merge_event_all_of_payload_merged_conversations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


