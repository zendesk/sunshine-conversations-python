# Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the item. | 
**description** | **str** | The description of the item. | [optional] 
**media_url** | **str** | The image url attached to the item. | [optional] 
**media_type** | **str** | The MIME type for any image attached in the mediaUrl. | [optional] 
**alt_text** | **str** | An optional description of the media for accessibility purposes. The field will be saved by default with the file name as the value. | [optional] 
**size** | **str** | The size of the image. | [optional] 
**actions** | [**list[ActionSubset]**](ActionSubset.md) | An array of objects representing the actions associated with the item. | 
**metadata** | [**object**](.md) | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


