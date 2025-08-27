# Meta

Response metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | A flag that indicates if there are more records that can be fetched. | [optional] 
**after_cursor** | **str** | A record id that can be used as a &#x60;page[after]&#x60; parameter in a new request to get the next page.  Not specified if there are no subsequent pages.  | [optional] 
**before_cursor** | **str** | A record id that can be used as a &#x60;page[before]&#x60; parameter in a new request to get the previous page.  Not specified if there are no previous pages.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.meta import Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Meta from a JSON string
meta_instance = Meta.from_json(json)
# print the JSON string representation of the object
print(Meta.to_json())

# convert the object into a dict
meta_dict = meta_instance.to_dict()
# create an instance of Meta from a dict
meta_from_dict = Meta.from_dict(meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


