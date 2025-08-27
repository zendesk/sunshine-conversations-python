# ParticipantLeaveBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The id of the user that will be removed from the conversation. It will return 404 if the user can’t be found.  | [optional] 
**user_external_id** | **str** | The externalId of the user that will be removed from the conversation. It will return 404 if the user can’t be found.  | [optional] 
**participant_id** | **str** | The participantId of the user that will be removed from the conversation. It will return 404 if the user can’t be found.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_leave_body import ParticipantLeaveBody

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantLeaveBody from a JSON string
participant_leave_body_instance = ParticipantLeaveBody.from_json(json)
# print the JSON string representation of the object
print(ParticipantLeaveBody.to_json())

# convert the object into a dict
participant_leave_body_dict = participant_leave_body_instance.to_dict()
# create an instance of ParticipantLeaveBody from a dict
participant_leave_body_from_dict = ParticipantLeaveBody.from_dict(participant_leave_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


