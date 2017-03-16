# MessagePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of the individual posting the message. Can be either *appUser* or *appMaker*. | 
**type** | **str** | The message type. | 
**name** | **str** | The display name of the message author. | [optional] 
**email** | **str** | The email address of the message author. | [optional] 
**avatar_url** | **str** | The URL of the desired message avatar image. | [optional] 
**metadata** | **object** | Flat JSON object containing any custom properties associated with the message. | [optional] 
**payload** | **str** | The payload of a reply action, if applicable. | [optional] 
**text** | **str** | The message text. Required for text messages.  | [optional] 
**media_url** | **str** | The mediaUrl for the image. Required for image messages.  | [optional] 
**media_type** | **str** | The mediaType for the image. Required for image messages.  | [optional] 
**items** | [**list[MessageItem]**](MessageItem.md) | The items in the message list. Required for carousel and list messages.  | [optional] 
**actions** | [**list[Action]**](Action.md) | The actions in the message. | [optional] 
**destination** | [**Destination**](Destination.md) | Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


