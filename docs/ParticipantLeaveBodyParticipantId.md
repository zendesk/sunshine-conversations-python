# ParticipantLeaveBodyParticipantId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_id** | **str** | The participantId of the user that will be removed from the conversation. It will return 404 if the user can’t be found.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_leave_body_participant_id import ParticipantLeaveBodyParticipantId

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantLeaveBodyParticipantId from a JSON string
participant_leave_body_participant_id_instance = ParticipantLeaveBodyParticipantId.from_json(json)
# print the JSON string representation of the object
print(ParticipantLeaveBodyParticipantId.to_json())

# convert the object into a dict
participant_leave_body_participant_id_dict = participant_leave_body_participant_id_instance.to_dict()
# create an instance of ParticipantLeaveBodyParticipantId from a dict
participant_leave_body_participant_id_from_dict = ParticipantLeaveBodyParticipantId.from_dict(participant_leave_body_participant_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


