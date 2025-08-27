# MessageWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the message. | [optional] 
**received** | **str** | A datetime string with the format &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60; representing when Sunshine Conversations received the message. | [optional] 
**author** | [**AuthorWebhook**](AuthorWebhook.md) |  | [optional] 
**content** | [**Content**](Content.md) | The content of the message. | [optional] 
**source** | [**MessageWebhookSource**](MessageWebhookSource.md) |  | [optional] 
**quoted_message** | [**QuotedMessage**](QuotedMessage.md) | The quoted message is currently only available for WhatsApp and Web Messenger &#x60;formResponse&#x60; messages. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**deleted** | **bool** | true if the message serves as a placeholder for one that has been deleted. | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_webhook import MessageWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of MessageWebhook from a JSON string
message_webhook_instance = MessageWebhook.from_json(json)
# print the JSON string representation of the object
print(MessageWebhook.to_json())

# convert the object into a dict
message_webhook_dict = message_webhook_instance.to_dict()
# create an instance of MessageWebhook from a dict
message_webhook_from_dict = MessageWebhook.from_dict(message_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


