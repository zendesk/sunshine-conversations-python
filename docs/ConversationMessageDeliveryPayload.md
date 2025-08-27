# ConversationMessageDeliveryPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) | The user associated with the conversation. | [optional] 
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation in which the message was sent. | [optional] 
**message** | [**ConversationMessageDeliveryPayloadMessage**](ConversationMessageDeliveryPayloadMessage.md) |  | [optional] 
**destination** | [**ConversationMessageDeliveryPayloadDestination**](ConversationMessageDeliveryPayloadDestination.md) |  | [optional] 
**external_messages** | [**List[ConversationMessageDeliveryPayloadExternalMessagesInner]**](ConversationMessageDeliveryPayloadExternalMessagesInner.md) | An array of objects representing the third-party messages associated with the event. The order of the external messages is not guaranteed to be the same across the different triggers. Note that some channels don’t expose message IDs, in which case this field will be unset. | [optional] 
**is_final_event** | **bool** | A boolean indicating whether the webhook is the final one for the &#x60;message.id&#x60; and &#x60;destination.type&#x60; pair. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_message_delivery_payload import ConversationMessageDeliveryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageDeliveryPayload from a JSON string
conversation_message_delivery_payload_instance = ConversationMessageDeliveryPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageDeliveryPayload.to_json())

# convert the object into a dict
conversation_message_delivery_payload_dict = conversation_message_delivery_payload_instance.to_dict()
# create an instance of ConversationMessageDeliveryPayload from a dict
conversation_message_delivery_payload_from_dict = ConversationMessageDeliveryPayload.from_dict(conversation_message_delivery_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


