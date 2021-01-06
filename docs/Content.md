# Content

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'template']
**text** | **str** | The fallback text message used when location messages are not supported by the channel. | [optional] [readonly] 
**actions** | [**list[ActionSubset]**](ActionSubset.md) | An array of objects representing the actions associated with the message. The array length is limited by the third party channel. | [optional] 
**items** | [**list[Item]**](Item.md) | An array of objects representing the items associated with the message. Only present in carousel and list type messages. | 
**display_settings** | [**CarouselMessageDisplaySettings**](CarouselMessageDisplaySettings.md) |  | [optional] 
**media_url** | **str** | The URL for media, such as an image, attached to the message. | 
**media_size** | **float** | The size of the media. | [optional] [readonly] 
**media_type** | **str** | The media type of the file. | [optional] [readonly] 
**alt_text** | **str** | An optional description of the image for accessibility purposes. The field will be saved by default with the file name as the value. | [optional] 
**block_chat_input** | **bool** | true if the message should block the chat input on Web Messenger. form message only. | [optional] 
**fields** | [**list[Field]**](Field.md) | Array of field objects that contain the submitted fields. | 
**text_fallback** | **str** | A string containing the &#x60;label: value&#x60; of all fields, each separated by a newline character. | [optional] [readonly] 
**coordinates** | [**LocationMessageCoordinates**](LocationMessageCoordinates.md) |  | 
**location** | [**LocationMessageLocation**](LocationMessageLocation.md) |  | [optional] 
**template** | [**object**](.md) | The whatsapp template message to send. For more information, consult the [guide](https://docs.smooch.io/guide/whatsapp#sending-message-templates). &#x60;schema&#x60; must be set to &#x60;whatsapp&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


