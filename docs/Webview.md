# Webview

When a webview actions is clicked/tapped, the provided URI will be loaded in a webview. Channels that do not support webviews will open the fallback URI instead.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | 
**uri** | **str** | The webview URI. This is the URI that will open in the webview when clicking the button. | 
**text** | **str** | The button text. | 
**default** | **bool** | Boolean value indicating whether the action is the default action for a message item in Facebook Messenger. | [optional] 
**metadata** | **dict(str, object)** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**extra_channel_options** | [**ExtraChannelOptions**](ExtraChannelOptions.md) |  | [optional] 
**size** | **str** | The size to display a webview. Used for actions of type webview. | [optional] 
**fallback** | **str** | The fallback uri for channels that don’t support webviews. Used for actions of type webview. | 
**open_on_receive** | **bool** | Boolean value indicating if the webview should open automatically. Only one action per message can be set to true. Currently only supported on the Web Messenger. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


