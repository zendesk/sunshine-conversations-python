# DefaultResponderDefaultResponder

The default responder for the integration. This is the responder that will be used to send messages to the user. For more information, refer to the <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the switchboard integration. | [optional] 
**integration_id** | **str** | The unique ID of the integration. | [optional] 
**integration_type** | **str** | The type of the integration. | [optional] 
**deliver_standby_events** | **bool** | Indicates whether the switchboard should deliver standby events. | [optional] 
**next_switchboard_integration_id** | **str** | The unique ID of the next switchboard integration. | [optional] 
**message_history_count** | **float** | The number of messages to keep in the message history. | [optional] 
**inherited** | **bool** | Indicates whether the default responder is inherited from the switchboard&#39;s global config or not. Returns &#x60;false&#x60; if a per-channel responder override has been set for this integration, and &#x60;true&#x60; otherwise. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


