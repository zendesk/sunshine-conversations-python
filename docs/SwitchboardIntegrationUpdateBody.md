# SwitchboardIntegrationUpdateBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identifier for use in control transfer protocols. Restricted to alphanumeric characters, &#x60;-&#x60; and &#x60;_&#x60;. | [optional] 
**integration_id** | **str** | The id of the integration to link to the switchboard integration. Must be used when linking a custom integration. Can&#39;t provide both &#x60;integrationId&#x60; and &#x60;integrationType&#x60;. | [optional] 
**integration_type** | **str** | The type of the integration to link to the switchboard integration. Must be used when linking an OAuth integration. Can&#39;t provide both &#x60;integrationId&#x60; and &#x60;integrationType&#x60;. | [optional] 
**deliver_standby_events** | **bool** | Setting to determine if webhooks should be sent when the switchboard integration is not in control of a conversation (standby status) | [optional] 
**next_switchboard_integration_id** | **str** | The switchboard integration id to which control of a conversation is passed / offered by default. | [optional] 
**message_history_count** | **int** | Number of messages to include in the message history context. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


