# ConversationPostbackEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postback** | [**PostbackWebhook**](PostbackWebhook.md) | The postback associated with the event. | [optional] 
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation linked to the postback. | [optional] 
**user** | [**User**](User.md) | The user that triggered the postback. | [optional] 
**source** | [**SourceWithCampaignWebhook**](SourceWithCampaignWebhook.md) | The source of the postback. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_postback_event_all_of_payload import ConversationPostbackEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationPostbackEventAllOfPayload from a JSON string
conversation_postback_event_all_of_payload_instance = ConversationPostbackEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationPostbackEventAllOfPayload.to_json())

# convert the object into a dict
conversation_postback_event_all_of_payload_dict = conversation_postback_event_all_of_payload_instance.to_dict()
# create an instance of ConversationPostbackEventAllOfPayload from a dict
conversation_postback_event_all_of_payload_from_dict = ConversationPostbackEventAllOfPayload.from_dict(conversation_postback_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


