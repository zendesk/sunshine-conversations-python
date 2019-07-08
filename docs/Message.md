# Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The message ID, generated automatically. | 
**author_id** | **str** | The ID of the message&#39;s author. | 
**role** | **str** | The role of the individual posting the message. See [**RoleEnum**](Enums.md#RoleEnum) for available values. | 
**type** | **str** | The message type. See [**MessageTypeEnum**](Enums.md#MessageTypeEnum) for available values. | 
**source** | [**Source**](Source.md) | The source of the message. | [optional] 
**name** | **str** | The display name of the message author. | 
**text** | **str** | The message text. Required for text messages.  | 
**email** | **str** | The email address of the message author. | [optional] 
**avatar_url** | **str** | The URL of the desired message avatar image. | 
**received** | **float** | The unix timestamp of the moment the message was received. | 
**media_url** | **str** | The mediaUrl for the message. Required for image/file messages.  | [optional] 
**media_type** | **str** | The mediaType for the message. Required for image/file messages.  | [optional] 
**metadata** | **object** | Flat JSON object containing any custom properties associated with the message. | [optional] 
**items** | [**list[MessageItem]**](MessageItem.md) | The items in the message list. Required for carousel and list messages.  | [optional] 
**actions** | [**list[Action]**](Action.md) | The actions in the message. | [optional] 
**payload** | **str** | The payload of a reply action, if applicable. | [optional] 
**display_settings** | [**DisplaySettings**](DisplaySettings.md) | Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings). | [optional] 
**block_chat_input** | **bool** | Indicates if the Web SDK chat input should be blocked. Defaults to false. Only for form messages.  | [optional] 
**fields** | [**list[Field]**](Field.md) | The fields in the form. Required for form and formResponse messages.  | [optional] 
**submitted** | **bool** | Indicates if the form was submitted. Generated automatically. | [optional] 
**quoted_message** | [**QuotedMessage**](QuotedMessage.md) | The form message a formResponse message responds to. Required for formResponse messages.  | [optional] 
**text_fallback** | **str** | The text fallback displayed in channels that do not support form messages. Only for formResponse messages. Generated automatically.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


