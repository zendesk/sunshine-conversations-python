# UserMergeEventAllOfPayloadMergedClients

Contains information about the clients that were merged together as a result of the operation, if applicable. If no clients were merged, this property is omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surviving** | [**Client**](Client.md) | The client that already existed before the merge started. | [optional] 
**discarded** | [**Client**](Client.md) | The pending client that was discarded during the merge event. | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_merge_event_all_of_payload_merged_clients import UserMergeEventAllOfPayloadMergedClients

# TODO update the JSON string below
json = "{}"
# create an instance of UserMergeEventAllOfPayloadMergedClients from a JSON string
user_merge_event_all_of_payload_merged_clients_instance = UserMergeEventAllOfPayloadMergedClients.from_json(json)
# print the JSON string representation of the object
print(UserMergeEventAllOfPayloadMergedClients.to_json())

# convert the object into a dict
user_merge_event_all_of_payload_merged_clients_dict = user_merge_event_all_of_payload_merged_clients_instance.to_dict()
# create an instance of UserMergeEventAllOfPayloadMergedClients from a dict
user_merge_event_all_of_payload_merged_clients_from_dict = UserMergeEventAllOfPayloadMergedClients.from_dict(user_merge_event_all_of_payload_merged_clients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


