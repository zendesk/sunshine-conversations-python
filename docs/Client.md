# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier for the client. Must be globally unique. | 
**active** | **bool** | Flag indicating if the client is active. | [optional] 
**last_seen** | **str** | The date time the client was last seen. | [optional] 
**platform** | **str** |  | 
**push_notification_token** | **str** | The GCM or APN token to be used for sending push notifications to the device. Applies to only *android* and *ios* clients.  | [optional] 
**app_version** | **str** | A reserved string field for reporting the app version running on the device. | [optional] 
**info** | [**ClientInfo**](ClientInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


