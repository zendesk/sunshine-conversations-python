# ParticipantResponse

The created participant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant** | [**Participant**](Participant.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_response import ParticipantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantResponse from a JSON string
participant_response_instance = ParticipantResponse.from_json(json)
# print the JSON string representation of the object
print(ParticipantResponse.to_json())

# convert the object into a dict
participant_response_dict = participant_response_instance.to_dict()
# create an instance of ParticipantResponse from a dict
participant_response_from_dict = ParticipantResponse.from_dict(participant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


