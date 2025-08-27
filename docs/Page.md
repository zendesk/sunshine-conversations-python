# Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | A record id. Results will only contain the records that come after the specified record.  Only one of &#x60;after&#x60; or &#x60;before&#x60; can be provided, not both.  | [optional] 
**before** | **str** | A record id. Results will only contain the records that come before the specified record. Only one of &#x60;after&#x60; or &#x60;before&#x60; can be provided, not both.  | [optional] 
**size** | **int** | The number of records to return. Does not apply to the &#x60;listMessages&#x60; endpoint. | [optional] [default to 25]

## Example

```python
from sunshine_conversations_client.model.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


