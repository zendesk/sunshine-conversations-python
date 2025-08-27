# MessagePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Author**](Author.md) | The author of the message. | 
**content** | [**Content**](Content.md) | The content of the message. | 
**destination** | [**Destination**](Destination.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**override** | [**MessageOverride**](MessageOverride.md) |  | [optional] 
**var_schema** | **str** | When &#x60;schema&#x60; is set to &#x60;\&quot;whatsapp\&quot;&#x60;, the &#x60;content&#x60; key is expected to conform to the [native WhatsApp schema](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates) for sending message templates. For more details, consult the documentation for [sending message templates on WhatsApp](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/message-overrides/#template-messages).  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_post import MessagePost

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePost from a JSON string
message_post_instance = MessagePost.from_json(json)
# print the JSON string representation of the object
print(MessagePost.to_json())

# convert the object into a dict
message_post_dict = message_post_instance.to_dict()
# create an instance of MessagePost from a dict
message_post_from_dict = MessagePost.from_dict(message_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


