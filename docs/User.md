# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the user. | [optional] 
**authenticated** | **bool** | Whether or not the user has authenticated, either via JWT or via the Help Center | [optional] [readonly] 
**external_id** | **str** | An optional ID that can also be used to retrieve the user.  | [optional] 
**zendesk_id** | **str** | The ID that links a messaging user to its core Zendesk user counterpart. This ID can be used to fetch the core user record via the Zendesk Support API.  | [optional] 
**signed_up_at** | **str** | The date at which the user signed up. Must be ISO 8601 time format &#x60;YYYY-MM-DDThh:mm:ss.sssZ&#x60;. | [optional] 
**to_be_retained** | **bool** | Flag indicating whether a user should be retained after they have passed their inactive expiry. See [creating deletion schedules for bot-only conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154) for more information. | [optional] 
**profile** | [**Profile**](Profile.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**identities** | [**List[Identity]**](Identity.md) | The user&#39;s connected identities. | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


