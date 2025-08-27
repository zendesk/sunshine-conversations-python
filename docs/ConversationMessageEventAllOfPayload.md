# ConversationMessageEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation in which the message was sent. | [optional] 
**message** | [**MessageWebhook**](MessageWebhook.md) | The message that was sent. | [optional] 
**recent_notifications** | [**List[MessageWebhook]**](MessageWebhook.md) | Messages sent with the Notification API since the last user message. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_message_event_all_of_payload import ConversationMessageEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageEventAllOfPayload from a JSON string
conversation_message_event_all_of_payload_instance = ConversationMessageEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageEventAllOfPayload.to_json())

# convert the object into a dict
conversation_message_event_all_of_payload_dict = conversation_message_event_all_of_payload_instance.to_dict()
# create an instance of ConversationMessageEventAllOfPayload from a dict
conversation_message_event_all_of_payload_from_dict = ConversationMessageEventAllOfPayload.from_dict(conversation_message_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


