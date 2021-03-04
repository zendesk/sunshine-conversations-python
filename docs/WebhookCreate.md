# WebhookCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | URL to be called when the webhook is triggered. | 
**triggers** | **list[str]** | An array of triggers you wish to have the webhook listen to. See [**WebhookTriggersEnum**](Enums.md#WebhookTriggersEnum) for available values. | [optional] 
**include_client** | **bool** | Specifies whether webhook payloads should include the client information associated with a conversation in webhook events. | [optional] 
**include_full_app_user** | **bool** | Specifies whether webhook payloads should include the complete appUser schema for appUser events. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


