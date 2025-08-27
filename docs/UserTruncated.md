# UserTruncated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the user. | [optional] 
**authenticated** | **bool** | Whether or not the user has authenticated, either via JWT or via the Help Center | [optional] [readonly] 
**external_id** | **str** | An optional ID that can also be used to retrieve the user.  | [optional] 
**zendesk_id** | **str** | The ID that links a messaging user to its core Zendesk user counterpart. This ID can be used to fetch the core user record via the Zendesk Support API.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.user_truncated import UserTruncated

# TODO update the JSON string below
json = "{}"
# create an instance of UserTruncated from a JSON string
user_truncated_instance = UserTruncated.from_json(json)
# print the JSON string representation of the object
print(UserTruncated.to_json())

# convert the object into a dict
user_truncated_dict = user_truncated_instance.to_dict()
# create an instance of UserTruncated from a dict
user_truncated_from_dict = UserTruncated.from_dict(user_truncated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


