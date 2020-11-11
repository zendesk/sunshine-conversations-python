# SwitchboardIntegrationCreateBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identifier for use in control transfer protocols. Restricted to alphanumeric characters, &#x60;-&#x60; and &#x60;_&#x60;. | 
**integration_id** | **str** | The id of the integration to link to the switchboard integration. Must be used when linking a custom integration. One of &#x60;integrationId&#x60; or &#x60;integrationType&#x60; must be provided. | [optional] 
**integration_type** | **str** | The type of the integration to link to the switchboard integration. Must be used when linking an OAuth integration. One of &#x60;integrationId&#x60; or &#x60;integrationType&#x60; must be provided. | [optional] 
**deliver_standby_events** | **bool** |  | [optional] 
**next_switchboard_integration_id** | **str** |  | [optional] 
**message_history_count** | **int** | Number of messages to include in the message history context. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


