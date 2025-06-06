# Viber

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | To configure a Viber integration, acquire the Viber Public Account token from the user and call the Create Integration endpoint.  | [optional] [default to 'viber']
**token** | **str** | Viber Public Account token. | 
**uri** | **str** | Unique URI of the Viber account. | [optional] [readonly] 
**account_id** | **str** | Unique ID of the Viber account. | [optional] [readonly] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


