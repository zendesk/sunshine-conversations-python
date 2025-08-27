# ParticipantListResponse

List of returned participants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participants** | [**List[Participant]**](Participant.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_list_response import ParticipantListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantListResponse from a JSON string
participant_list_response_instance = ParticipantListResponse.from_json(json)
# print the JSON string representation of the object
print(ParticipantListResponse.to_json())

# convert the object into a dict
participant_list_response_dict = participant_list_response_instance.to_dict()
# create an instance of ParticipantListResponse from a dict
participant_list_response_from_dict = ParticipantListResponse.from_dict(participant_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


