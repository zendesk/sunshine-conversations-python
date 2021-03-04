# MessagePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of the individual posting the message. See [**RoleEnum**](Enums.md#RoleEnum) for available values. | 
**type** | **str** | The message type. See [**MessageTypeEnum**](Enums.md#MessageTypeEnum) for available values. | 
**name** | **str** | The display name of the message author. | [optional] 
**email** | **str** | The email address of the message author. | [optional] 
**avatar_url** | **str** | The URL of the desired message avatar image. | [optional] 
**metadata** | **object** | Flat JSON object containing any custom properties associated with the message. | [optional] 
**payload** | **str** | The payload of a reply action, if applicable. | [optional] 
**text** | **str** | The message text. Required for text messages.  | [optional] 
**media_url** | **str** | The mediaUrl for the message. Required for image/file messages.  | [optional] 
**media_type** | **str** | The mediaType for the message. Required for image/file messages.  | [optional] 
**alt_text** | **str** | An optional description of the image or the file for accessibility purposes. The field will be saved by default with the file name as the value. | [optional] 
**items** | [**list[MessageItem]**](MessageItem.md) | The items in the message list. Required for carousel and list messages.  | [optional] 
**actions** | [**list[Action]**](Action.md) | The actions in the message. | [optional] 
**block_chat_input** | **bool** | Indicates if the Web SDK chat input should be blocked. Defaults to false. Only for form messages.  | [optional] 
**display_settings** | [**DisplaySettings**](DisplaySettings.md) | Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings). | [optional] 
**fields** | [**list[FieldPost]**](FieldPost.md) | The fields in the form. Required for form messages.  | [optional] 
**destination** | [**Destination**](Destination.md) | Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type. | [optional] 
**override** | [**MessageOverride**](MessageOverride.md) | Specifies channel-specific overrides to use in order to bypass Smooch&#39;s message translation logic. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) | Data representing the location being sent in the message. | [optional] 
**location** | [**Location**](Location.md) | Additional information about the location being sent in the message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


