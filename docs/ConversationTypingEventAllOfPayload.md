# ConversationTypingEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation in which the activity was sent. | [optional] 
**activity** | [**ConversationTypingEventAllOfPayloadActivity**](ConversationTypingEventAllOfPayloadActivity.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_typing_event_all_of_payload import ConversationTypingEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationTypingEventAllOfPayload from a JSON string
conversation_typing_event_all_of_payload_instance = ConversationTypingEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationTypingEventAllOfPayload.to_json())

# convert the object into a dict
conversation_typing_event_all_of_payload_dict = conversation_typing_event_all_of_payload_instance.to_dict()
# create an instance of ConversationTypingEventAllOfPayload from a dict
conversation_typing_event_all_of_payload_from_dict = ConversationTypingEventAllOfPayload.from_dict(conversation_typing_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


