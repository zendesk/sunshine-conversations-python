# ConversationUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A friendly name for the conversation, may be displayed to the business or the user.  | [optional] 
**description** | **str** | A short text describing the conversation. | [optional] 
**icon_url** | **str** | A custom conversation icon url. The image must be in either JPG, PNG, or GIF format | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_update_body import ConversationUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationUpdateBody from a JSON string
conversation_update_body_instance = ConversationUpdateBody.from_json(json)
# print the JSON string representation of the object
print(ConversationUpdateBody.to_json())

# convert the object into a dict
conversation_update_body_dict = conversation_update_body_instance.to_dict()
# create an instance of ConversationUpdateBody from a dict
conversation_update_body_from_dict = ConversationUpdateBody.from_dict(conversation_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


