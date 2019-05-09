# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier for the client. Must be globally unique. | 
**status** | **str** | The client status. Indicates if the client is able to receive messages or not. See [**ClientStatusEnum**](Enums.md#ClientStatusEnum) for available values. | [optional] 
**external_id** | **str** | The ID of the user on an external channel. For example, the user&#39;s phone number for Twilio, or their page-scoped user ID for Facebook Messenger. Applies only to non-SDK clients. | [optional] 
**active** | **bool** | Deprecated - use the status property instead. | [optional] 
**last_seen** | **str** | The date time the client was last seen. | [optional] 
**platform** | **str** | The client&#39;s platform. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values. | 
**integration_id** | **str** | The ID of the integration that the client was created for. | [optional] 
**push_notification_token** | **str** | The GCM or APN token to be used for sending push notifications to the device. Applies to only *android* and *ios* clients.  | [optional] 
**app_version** | **str** | A reserved string field for reporting the app version running on the device. | [optional] 
**display_name** | **str** | The client&#39;s display name. | [optional] 
**info** | [**ClientInfo**](ClientInfo.md) |  | [optional] 
**raw** | **object** | An Object with raw properties that vary for each client platform. All keys are optional and not guaranteed to be available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


