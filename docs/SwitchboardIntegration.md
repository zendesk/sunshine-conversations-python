# SwitchboardIntegration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the switchboard integration. | 
**name** | **str** | Identifier for use in control transfer protocols. Restricted to alphanumeric characters, &#x60;-&#x60; and &#x60;_&#x60;. | 
**integration_id** | **str** | Id of the integration that should deliver events routed by the switchboard. | 
**integration_type** | **str** | Type of integration that should deliver events routed by the switchboard. If referencing an OAuth integration, the clientId issued by Sunshine Conversations during the OAuth partnership process will be the value of integrationType. | 
**deliver_standby_events** | **bool** | Setting to determine if webhooks should be sent when the switchboard integration is not in control of a conversation (standby status) | 
**next_switchboard_integration_id** | **str** | The switchboard integration id to which control of a conversation is passed / offered by default. | [optional] 
**message_history_count** | **int** | Number of messages to include in the message history context. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


