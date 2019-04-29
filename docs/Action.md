# Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action type. See [**ActionTypeEnum**](Enums.md#ActionTypeEnum) for available values. | 
**text** | **str** | The button text. | 
**payload** | **str** | The payload to be sent with the resulting webhook. Required for *postback* and *reply* actions.  | [optional] 
**metadata** | **object** | Flat JSON object containing any custom properties associated with the action. | [optional] 
**amount** | **int** | The amount being charged. It needs to be specified in cents and is an integer. Required for *buy* actions.  | [optional] 
**currency** | **str** | The currency of the amount being charged (USD, CAD, etc.). | [optional] 
**default** | **bool** | Flag indicating if the message action is the default for a message item in Facebook Messenger. | [optional] 
**icon_url** | **str** | An icon to render next to the reply option (Facebook Messenger and Web Messenger only). | [optional] 
**uri** | **str** | The action URI. This is the link that will be used in the clients when clicking the button. Required for *link* and *webview* actions.  | [optional] 
**fallback** | **str** | The webview action fallback uri. This is the link that will be used in clients that do not support webviews. Required for *webview* actions.  | [optional] 
**size** | **str** | The size used to display the webview. Allowed values are [\&quot;compact\&quot;, \&quot;tall\&quot;, \&quot;full\&quot;]. (Optional) Used for *webview* actions. See [**ActionSizeEnum**](Enums.md#ActionSizeEnum) for available values.  | [optional] 
**extra_channel_options** | **object** | Extra options to pass directly to the channel API. See [Extra Channel Options](https://docs.smooch.io/rest#extra-channel-options-schema) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


