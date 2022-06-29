# ConversationTruncated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the conversation. | [optional] 
**type** | [**ConversationType**](ConversationType.md) |  | [optional] 
**metadata** | [**object**](.md) | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**active_switchboard_integration** | [**SwitchboardIntegrationWebhook**](SwitchboardIntegrationWebhook.md) | The current switchboard integration that is in control of the conversation. This field is omitted if no &#x60;activeSwitchboardIntegration&#x60; exists for the conversation. | [optional] 
**pending_switchboard_integration** | [**SwitchboardIntegrationWebhook**](SwitchboardIntegrationWebhook.md) | The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


