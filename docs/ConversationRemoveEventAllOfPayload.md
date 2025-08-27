# ConversationRemoveEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation that was deleted. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_remove_event_all_of_payload import ConversationRemoveEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationRemoveEventAllOfPayload from a JSON string
conversation_remove_event_all_of_payload_instance = ConversationRemoveEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationRemoveEventAllOfPayload.to_json())

# convert the object into a dict
conversation_remove_event_all_of_payload_dict = conversation_remove_event_all_of_payload_instance.to_dict()
# create an instance of ConversationRemoveEventAllOfPayload from a dict
conversation_remove_event_all_of_payload_from_dict = ConversationRemoveEventAllOfPayload.from_dict(conversation_remove_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


