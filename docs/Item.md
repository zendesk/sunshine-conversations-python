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
**actions** | [**List[ActionSubset]**](ActionSubset.md) | An array of objects representing the actions associated with the item. | 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


