# WebhookBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | URL to be called when the webhook is triggered. | [optional] 
**triggers** | **list[str]** | An array of triggers the integration is subscribed to. This property is case sensitive. Current supported triggers in v2 are &#x60;conversation:create&#x60;, &#x60;conversation:message:delivery:channel&#x60;, &#x60;conversation:message:delivery:failure&#x60;, &#x60;conversation:message:delivery:user&#x60;, &#x60;conversation:message&#x60;, &#x60;conversation:read&#x60;, &#x60;conversation:typing&#x60;, &#x60;conversation:postback&#x60;, and &#x60;user:merge&#x60; | [optional] 
**include_full_user** | **bool** | A boolean specifying whether webhook payloads should include the complete user schema for events involving a specific user. | [optional] [default to False]
**include_full_source** | **bool** | A boolean specifying whether webhook payloads should include the client and device object (when applicable). | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


