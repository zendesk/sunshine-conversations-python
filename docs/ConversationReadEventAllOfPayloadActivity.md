# ConversationReadEventAllOfPayloadActivity

The activity that was sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of activity. | [optional] [default to 'conversation:read']
**source** | [**SourceWebhook**](SourceWebhook.md) | The source of the activity. | [optional] 
**author** | [**AuthorWebhook**](AuthorWebhook.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_read_event_all_of_payload_activity import ConversationReadEventAllOfPayloadActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationReadEventAllOfPayloadActivity from a JSON string
conversation_read_event_all_of_payload_activity_instance = ConversationReadEventAllOfPayloadActivity.from_json(json)
# print the JSON string representation of the object
print(ConversationReadEventAllOfPayloadActivity.to_json())

# convert the object into a dict
conversation_read_event_all_of_payload_activity_dict = conversation_read_event_all_of_payload_activity_instance.to_dict()
# create an instance of ConversationReadEventAllOfPayloadActivity from a dict
conversation_read_event_all_of_payload_activity_from_dict = ConversationReadEventAllOfPayloadActivity.from_dict(conversation_read_event_all_of_payload_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


