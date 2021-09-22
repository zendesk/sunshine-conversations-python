# ClientUpdateEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation which triggered a change in the client. | [optional] 
**user** | [**UserTruncated**](UserTruncated.md) | The user associated with the client. | [optional] 
**client** | [**Client**](Client.md) | The updated client. | [optional] 
**reason** | **str** | The reason for which the client was updated. * &#x60;confirmed&#x60; - The client is now active and ready to use. * &#x60;blocked&#x60; - The user has unsubscribed from the conversation. * &#x60;matched&#x60; - The channel found a user that matches the information provided.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


