# Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The message ID, generated automatically. | 
**author_id** | **str** | The ID of the message&#39;s author. | 
**role** | **str** | The role of the individual posting the message. Can be either *appUser* or *appMaker*. | 
**type** | **str** | The message type. | 
**name** | **str** | The display name of the message author. | 
**text** | **str** | The message text. Required for text messages.  | 
**email** | **str** | The email address of the message author. | [optional] 
**avatar_url** | **str** | The URL of the desired message avatar image. | 
**received** | **float** | The unix timestamp of the moment the message was received. | 
**media_url** | **str** | The mediaUrl for the image. Required for image messages.  | [optional] 
**media_type** | **str** | The mediaType for the image. Required for image messages.  | [optional] 
**metadata** | **object** | Flat JSON object containing any custom properties associated with the message. | [optional] 
**items** | [**list[MessageItem]**](MessageItem.md) | The items in the message list. Required for carousel and list messages.  | [optional] 
**actions** | [**list[Action]**](Action.md) | The actions in the message. | [optional] 
**payload** | **str** | The payload of a reply action, if applicable. | [optional] 
**display_settings** | [**DisplaySettings**](DisplaySettings.md) | Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


