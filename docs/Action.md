# Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | 
**text** | **str** | The button text. | 
**amount** | **int** | The amount being charged. It needs to be specified in cents and is an integer (9.99$ -&gt; 999). | 
**currency** | **str** | An ISO 4217 standard currency code in lowercase. Used for actions of type buy. | [optional] 
**metadata** | [**object**](.md) | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**uri** | **str** | The webview URI. This is the URI that will open in the webview when clicking the button. | 
**default** | **bool** | Boolean value indicating whether the action is the default action for a message item in Facebook Messenger. | [optional] 
**extra_channel_options** | [**ExtraChannelOptions**](ExtraChannelOptions.md) |  | [optional] 
**payload** | **str** | A string payload to help you identify the action context. Used when posting the reply. You can also use metadata for more complex needs. | 
**icon_url** | **str** | An icon to render next to the reply option. | [optional] 
**size** | **str** | The size to display a webview. Used for actions of type webview. | [optional] 
**fallback** | **str** | The fallback uri for channels that don’t support webviews. Used for actions of type webview. | 
**open_on_receive** | **bool** | Boolean value indicating if the webview should open automatically. Only one action per message can be set to true. Currently only supported on the Web Messenger. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


