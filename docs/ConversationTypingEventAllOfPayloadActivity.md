# ConversationTypingEventAllOfPayloadActivity

The activity that was sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of activity. | [optional] 
**source** | [**SourceWebhook**](SourceWebhook.md) | The source of the activity. | [optional] 
**author** | [**AuthorWebhook**](AuthorWebhook.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_typing_event_all_of_payload_activity import ConversationTypingEventAllOfPayloadActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationTypingEventAllOfPayloadActivity from a JSON string
conversation_typing_event_all_of_payload_activity_instance = ConversationTypingEventAllOfPayloadActivity.from_json(json)
# print the JSON string representation of the object
print(ConversationTypingEventAllOfPayloadActivity.to_json())

# convert the object into a dict
conversation_typing_event_all_of_payload_activity_dict = conversation_typing_event_all_of_payload_activity_instance.to_dict()
# create an instance of ConversationTypingEventAllOfPayloadActivity from a dict
conversation_typing_event_all_of_payload_activity_from_dict = ConversationTypingEventAllOfPayloadActivity.from_dict(conversation_typing_event_all_of_payload_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


