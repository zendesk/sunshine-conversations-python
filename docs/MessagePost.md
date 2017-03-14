# MessagePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**destination** | [**Destination**](Destination.md) | Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type. | [optional] 
**metadata** | **object** |  | [optional] 
**payload** | **str** |  | [optional] 
**text** | **str** | Required for text messages. | [optional] 
**media_url** | **str** | Required for image messages. | [optional] 
**media_type** | **str** |  | [optional] 
**items** | [**list[MessageItem]**](MessageItem.md) | Required for carousel and list messages. | [optional] 
**actions** | [**list[Action]**](Action.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


