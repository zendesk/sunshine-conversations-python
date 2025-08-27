# Participant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the participant. | [optional] 
**user_id** | **str** | The id of the associated user. | [optional] 
**unread_count** | **int** | Number of messages the user has not yet read. | [optional] 
**client_associations** | [**List[ClientAssociation]**](ClientAssociation.md) | Represents the clients that are active in the conversation for a particular user. A participant can have multiple clientAssociations in the case of channel transfer, business initiated conversations, or identified users. The order of the array indicates how recently a client has interacted with the conversation, with the most recent client first. The first item in the array is considered to be the user&#39;s primary client for that conversation, and will be selected first for message delivery.  | [optional] 
**user_external_id** | **str** | The externalId of the associated user. | [optional] 
**last_read** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the latest message the user has read. | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant import Participant

# TODO update the JSON string below
json = "{}"
# create an instance of Participant from a JSON string
participant_instance = Participant.from_json(json)
# print the JSON string representation of the object
print(Participant.to_json())

# convert the object into a dict
participant_dict = participant_instance.to_dict()
# create an instance of Participant from a dict
participant_from_dict = Participant.from_dict(participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


