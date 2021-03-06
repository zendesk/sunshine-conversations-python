# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the client. | [optional] 
**type** | [**ClientType**](ClientType.md) |  | [optional] 
**status** | **str** | The client status. Indicates if the client is able to receive messages or not. Can be pending, inactive, active, or blocked. | [optional] 
**integration_id** | **str** | The ID of the integration that the client was created for. Unused for clients of type sdk, as they incorporate multiple integrations. | [optional] 
**external_id** | **str** | The ID of the user on an external channel. For example, the user’s phone number for Twilio, or their page-scoped user ID for Facebook Messenger. Applies only to non-SDK clients. | [optional] 
**last_seen** | **str** | A datetime string with the format &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60; representing the last time the user interacted with this client. | [optional] 
**linked_at** | **str** | A timestamp signifying when the client was added to the user. Formatted as &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60;. | [optional] 
**display_name** | **str** | The user&#39;s display name on the channel. | [optional] 
**avatar_url** | **str** | The URL for the user&#39;s avatar on the channel. | [optional] 
**info** | [**object**](.md) | A flat curated object with properties that vary for each client platform. All keys are optional and not guaranteed to be available. | [optional] 
**raw** | [**object**](.md) | An object with raw properties that vary for each client platform. All keys are optional and not guaranteed to be available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


