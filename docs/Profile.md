# Profile

Object hosting user profile information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**given_name** | **str** | The user&#39;s given name (first name). | [optional] 
**surname** | **str** | The user&#39;s surname (last name). | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] 
**avatar_url** | **str** | The user&#39;s avatar. | [optional] 
**locale** | **str** | End-user&#39;s locale information in BCP 47 format. | [optional] 

## Example

```python
from sunshine_conversations_client.model.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


