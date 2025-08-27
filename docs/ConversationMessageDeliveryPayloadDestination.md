# ConversationMessageDeliveryPayloadDestination

A nested object representing the destination of the message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An identifier for the channel to which a message was sent to. May include one of \&quot;web\&quot;, \&quot;ios\&quot;, \&quot;android\&quot;, \&quot;messenger\&quot;, \&quot;viber\&quot;, \&quot;telegram\&quot;, \&quot;wechat\&quot;, \&quot;line\&quot;, \&quot;twilio\&quot;, \&quot;api\&quot;, \&quot;notification\&quot;, or any other channel. | [optional] 
**integration_id** | **str** | Identifier indicating which integration the message was sent to. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_message_delivery_payload_destination import ConversationMessageDeliveryPayloadDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageDeliveryPayloadDestination from a JSON string
conversation_message_delivery_payload_destination_instance = ConversationMessageDeliveryPayloadDestination.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageDeliveryPayloadDestination.to_json())

# convert the object into a dict
conversation_message_delivery_payload_destination_dict = conversation_message_delivery_payload_destination_instance.to_dict()
# create an instance of ConversationMessageDeliveryPayloadDestination from a dict
conversation_message_delivery_payload_destination_from_dict = ConversationMessageDeliveryPayloadDestination.from_dict(conversation_message_delivery_payload_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


