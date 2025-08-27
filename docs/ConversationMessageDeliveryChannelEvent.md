# ConversationMessageDeliveryChannelEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the event. May be used to ensure that an event is not processed twice in the case of a webhook that is re-tried due to an error or timeout. | [optional] 
**type** | **str** | The type of the event. Will match one of the subscribed triggers for your [webhook](#operation/CreateWebhook). | [optional] 
**created_at** | **str** | A timestamp signifying when the event was generated. Formatted as &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60;. | [optional] 
**payload** | [**ConversationMessageDeliveryPayload**](ConversationMessageDeliveryPayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_message_delivery_channel_event import ConversationMessageDeliveryChannelEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageDeliveryChannelEvent from a JSON string
conversation_message_delivery_channel_event_instance = ConversationMessageDeliveryChannelEvent.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageDeliveryChannelEvent.to_json())

# convert the object into a dict
conversation_message_delivery_channel_event_dict = conversation_message_delivery_channel_event_instance.to_dict()
# create an instance of ConversationMessageDeliveryChannelEvent from a dict
conversation_message_delivery_channel_event_from_dict = ConversationMessageDeliveryChannelEvent.from_dict(conversation_message_delivery_channel_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


