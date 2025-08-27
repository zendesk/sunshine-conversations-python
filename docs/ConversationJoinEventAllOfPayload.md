# ConversationJoinEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation in which the user was added. | [optional] 
**user** | [**UserTruncated**](UserTruncated.md) | The user that joined the conversation. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_join_event_all_of_payload import ConversationJoinEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationJoinEventAllOfPayload from a JSON string
conversation_join_event_all_of_payload_instance = ConversationJoinEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationJoinEventAllOfPayload.to_json())

# convert the object into a dict
conversation_join_event_all_of_payload_dict = conversation_join_event_all_of_payload_instance.to_dict()
# create an instance of ConversationJoinEventAllOfPayload from a dict
conversation_join_event_all_of_payload_from_dict = ConversationJoinEventAllOfPayload.from_dict(conversation_join_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


