# ParticipantLeaveBodyUserExternalId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_external_id** | **str** | The externalId of the user that will be removed from the conversation. It will return 404 if the user can’t be found.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_leave_body_user_external_id import ParticipantLeaveBodyUserExternalId

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantLeaveBodyUserExternalId from a JSON string
participant_leave_body_user_external_id_instance = ParticipantLeaveBodyUserExternalId.from_json(json)
# print the JSON string representation of the object
print(ParticipantLeaveBodyUserExternalId.to_json())

# convert the object into a dict
participant_leave_body_user_external_id_dict = participant_leave_body_user_external_id_instance.to_dict()
# create an instance of ParticipantLeaveBodyUserExternalId from a dict
participant_leave_body_user_external_id_from_dict = ParticipantLeaveBodyUserExternalId.from_dict(participant_leave_body_user_external_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


