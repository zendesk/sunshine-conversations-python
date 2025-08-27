# SyncUserBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surviving_zendesk_id** | **str** | Only used for synchronizing messaging users when their Support user counterparts have been merged. The user.id of the surviving Support user is specified here.   | [optional] 

## Example

```python
from sunshine_conversations_client.model.sync_user_body import SyncUserBody

# TODO update the JSON string below
json = "{}"
# create an instance of SyncUserBody from a JSON string
sync_user_body_instance = SyncUserBody.from_json(json)
# print the JSON string representation of the object
print(SyncUserBody.to_json())

# convert the object into a dict
sync_user_body_dict = sync_user_body_instance.to_dict()
# create an instance of SyncUserBody from a dict
sync_user_body_from_dict = SyncUserBody.from_dict(sync_user_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


