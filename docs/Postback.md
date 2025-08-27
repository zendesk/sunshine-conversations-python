# Postback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | [default to 'postback']
**text** | **str** | The button text. | 
**payload** | **str** | The payload of a postback or reply button. | 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.postback import Postback

# TODO update the JSON string below
json = "{}"
# create an instance of Postback from a JSON string
postback_instance = Postback.from_json(json)
# print the JSON string representation of the object
print(Postback.to_json())

# convert the object into a dict
postback_dict = postback_instance.to_dict()
# create an instance of Postback from a dict
postback_from_dict = Postback.from_dict(postback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


