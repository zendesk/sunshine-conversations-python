# Link

A link action will open the provided URI when tapped.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | [default to 'link']
**uri** | **str** | The action URI. This is the link that will be used in the clients when clicking the button. | 
**text** | **str** | The button text. | 
**default** | **bool** | Boolean value indicating whether the action is the default action for a message item in Facebook Messenger. | [optional] 
**metadata** | [**object**](.md) | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**extra_channel_options** | [**ExtraChannelOptions**](ExtraChannelOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


