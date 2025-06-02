# UserUpdateEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) | The updated user. | [optional] 
**reason** | **str** | The reason why the user was updated, if applicable. * &#x60;authentication&#x60; - An unauthenticated user became an [authenticated](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/intro-to-users/) user. * &#x60;localeDetection&#x60; - A user was updated as a result of automated locale detection on messages sent.  | [optional] 
**source** | [**SourceWebhook**](SourceWebhook.md) | The source of the creation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


