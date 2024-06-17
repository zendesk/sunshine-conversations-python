# DefaultResponderDefaultResponder

The default responder object. <aside class=\"notice\">This property will only be returned in response for <code>get integration</code> and <code>list integration</code> and must not be used in the request body.</aside> <aside class=\"notice\">Response will contain only one of the following: <code>defaultResponder</code> or <code>defaultResponderId</code> but never both.</aside> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboard_id** | **str** | The unique ID of the switchboard. | [optional] 
**app_id** | **str** | Identifies the app. | [optional] 
**integration_id** | **str** | The unique ID of the integration. | [optional] 
**integration_type** | **str** | The type of the integration. | [optional] 
**name** | **str** | The name of the switchboard. | [optional] 
**deliver_standby_events** | **bool** | Indicates whether the switchboard should deliver standby events. | [optional] 
**next_switchboard_integration_id** | **str** | The unique ID of the next switchboard integration. | [optional] 
**message_history_count** | **float** | The number of messages to keep in the message history. | [optional] 
**inherited** | **bool** | Indicates whether the switchboard is inherited. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


