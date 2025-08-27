# Link

A link action will open the provided URI when tapped.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | [default to 'link']
**uri** | **str** | The action URI. This is the link that will be used in the clients when clicking the button. | 
**text** | **str** | The button text. | 
**default** | **bool** | Boolean value indicating whether the action is the default action for a message item in Facebook Messenger. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**extra_channel_options** | [**ExtraChannelOptions**](ExtraChannelOptions.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print(Link.to_json())

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_from_dict = Link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


