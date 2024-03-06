# ConversationMessageDeliveryPayload

The payload of the event. The contents of this object depend on the type of event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User2**](User2.md) | The user associated with the conversation. | [optional] 
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation in which the message was sent. | [optional] 
**message** | [**ConversationMessageDeliveryPayloadMessage**](ConversationMessageDeliveryPayloadMessage.md) |  | [optional] 
**destination** | [**ConversationMessageDeliveryPayloadDestination**](ConversationMessageDeliveryPayloadDestination.md) |  | [optional] 
**external_messages** | [**list[ConversationMessageDeliveryPayloadExternalMessages]**](ConversationMessageDeliveryPayloadExternalMessages.md) | An array of objects representing the third-party messages associated with the event. The order of the external messages is not guaranteed to be the same across the different triggers. Note that some channels don’t expose message IDs, in which case this field will be unset. | [optional] 
**is_final_event** | **bool** | A boolean indicating whether the webhook is the final one for the &#x60;message.id&#x60; and &#x60;destination.type&#x60; pair. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


