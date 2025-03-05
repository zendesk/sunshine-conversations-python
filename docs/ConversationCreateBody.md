# ConversationCreateBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConversationType**](ConversationType.md) |  | 
**participants** | [**list[ParticipantSubSchema]**](ParticipantSubSchema.md) | The users participating in the conversation. For &#x60;personal&#x60; conversations, this field is required with a length of exactly 1. For &#x60;sdkGroup&#x60; conversations, must have a length less than or equal to 10. Can be omitted to have a conversation with no participants if the type is &#x60;sdkGroup&#x60;.  | [optional] 
**display_name** | **str** | A friendly name for the conversation, may be displayed to the business or the user.  | [optional] 
**description** | **str** | A short text describing the conversation. | [optional] 
**icon_url** | **str** | A custom conversation icon url. The image must be in either JPG, PNG, or GIF format | [optional] 
**metadata** | **dict(str, object)** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


