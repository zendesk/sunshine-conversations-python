# ConversationMessageDeliveryPayloadMessage

The message that was sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A string representing the ID of the message. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_message_delivery_payload_message import ConversationMessageDeliveryPayloadMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageDeliveryPayloadMessage from a JSON string
conversation_message_delivery_payload_message_instance = ConversationMessageDeliveryPayloadMessage.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageDeliveryPayloadMessage.to_json())

# convert the object into a dict
conversation_message_delivery_payload_message_dict = conversation_message_delivery_payload_message_instance.to_dict()
# create an instance of ConversationMessageDeliveryPayloadMessage from a dict
conversation_message_delivery_payload_message_from_dict = ConversationMessageDeliveryPayloadMessage.from_dict(conversation_message_delivery_payload_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


