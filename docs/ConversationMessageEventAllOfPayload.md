# ConversationMessageEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation in which the message was sent. | [optional] 
**message** | [**MessageWebhook**](MessageWebhook.md) | The message that was sent. | [optional] 
**recent_notifications** | [**list[MessageWebhook]**](MessageWebhook.md) | Messages sent with the Notification API since the last user message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


