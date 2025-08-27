# Links

Previous and next page links, if they exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | **str** | A link to the previous page. Not specified if there are no previous pages. | [optional] 
**next** | **str** | A link to the next page. Not specified if there are no subsequent pages. | [optional] 

## Example

```python
from sunshine_conversations_client.model.links import Links

# TODO update the JSON string below
json = "{}"
# create an instance of Links from a JSON string
links_instance = Links.from_json(json)
# print the JSON string representation of the object
print(Links.to_json())

# convert the object into a dict
links_dict = links_instance.to_dict()
# create an instance of Links from a dict
links_from_dict = Links.from_dict(links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


