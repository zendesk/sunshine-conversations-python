# MessageItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the message item. | 
**description** | **str** | The text description, or subtitle. | [optional] 
**media_url** | **str** | The image URL to be shown in the carousel/list item. | [optional] 
**size** | **str** | The size of the image to be shown in the carousel/list item. Only top item of Facebook Messenger carousel supported. See Enums.md for available values.  | [optional] 
**media_type** | **str** | If a *mediaUrl* was specified, the media type is defined here, for example *image/jpeg*. | [optional] 
**actions** | [**list[Action]**](Action.md) | Array of [action buttons](https://docs.smooch.io/rest/#action-buttons). At least 1 is required, a maximum of 3 are allowed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


