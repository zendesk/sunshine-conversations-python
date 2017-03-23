# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The webhook ID, generated automatically. | 
**target** | **str** | URL to be called when the webhook is triggered. | 
**triggers** | **list[str]** | An array of triggers you wish to have the webhook listen to. If unspecified the default trigger is *message*. | 
**secret** | **str** | Secret which will be transmitted with each webhook invocation and can be used to verify the authenticity of the caller. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


