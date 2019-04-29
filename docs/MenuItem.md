# MenuItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The button text of the menu item. | 
**uri** | **str** | A valid address, like http://smooch.io. Required for a link type item. | [optional] 
**type** | **str** | Can either be link, postback, which correspond to Smooch’s link and postback actions, or submenu for nested menus. See [**MenuItemTypeEnum**](Enums.md#MenuItemTypeEnum) for available values. | 
**payload** | **str** | A payload for a postback. Required for a postback type item. | [optional] 
**items** | [**list[SubMenuItem]**](SubMenuItem.md) | A list of menu items for a submenu. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


