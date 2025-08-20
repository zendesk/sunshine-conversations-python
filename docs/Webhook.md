# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the webhook. | [optional] [readonly] 
**version** | **str** | Schema version of the payload delivered to this webhook. Can be &#x60;v1&#x60;, &#x60;v1.1&#x60; or &#x60;v2&#x60;. | [optional] [readonly] 
**target** | **str** | URL to be called when the webhook is triggered. | 
**triggers** | **list[str]** | An array of triggers the integration is subscribed to. This property is case sensitive. [More details](https://developer.zendesk.com/api-reference/conversations/#section/Webhook-Triggers). | 
**secret** | **str** | Webhook secret, used to verify the origin of incoming requests. | [optional] 
**include_full_user** | **bool** | A boolean specifying whether webhook payloads should include the complete user schema for events involving a specific user. | [optional] [default to False]
**include_full_source** | **bool** | A boolean specifying whether webhook payloads should include the client and device object (when applicable). | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


