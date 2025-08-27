# ParticipantLeaveBodyUserId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The id of the user that will be removed from the conversation. It will return 404 if the user can’t be found.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_leave_body_user_id import ParticipantLeaveBodyUserId

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantLeaveBodyUserId from a JSON string
participant_leave_body_user_id_instance = ParticipantLeaveBodyUserId.from_json(json)
# print the JSON string representation of the object
print(ParticipantLeaveBodyUserId.to_json())

# convert the object into a dict
participant_leave_body_user_id_dict = participant_leave_body_user_id_instance.to_dict()
# create an instance of ParticipantLeaveBodyUserId from a dict
participant_leave_body_user_id_from_dict = ParticipantLeaveBodyUserId.from_dict(participant_leave_body_user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


