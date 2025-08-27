# MessageWebhookSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An identifier for the channel from which a message originated. May include one of api, sdk, messenger, or any number of other channels. | 
**integration_id** | **str** | Identifier indicating which integration the message was sent from. For user messages only. | [optional] 
**original_message_id** | **str** | Message identifier assigned by the originating channel. | [optional] 
**original_message_timestamp** | **str** | A datetime string with the format &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60; representing when the third party channel received the message. | [optional] 
**client** | [**Client**](Client.md) | The client from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the &#x60;includeFullSource&#x60; option is enabled. | [optional] 
**device** | [**Device**](Device.md) | The device from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the &#x60;includeFullSource&#x60; option is enabled. | [optional] 
**campaign** | [**Campaign**](Campaign.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_webhook_source import MessageWebhookSource

# TODO update the JSON string below
json = "{}"
# create an instance of MessageWebhookSource from a JSON string
message_webhook_source_instance = MessageWebhookSource.from_json(json)
# print the JSON string representation of the object
print(MessageWebhookSource.to_json())

# convert the object into a dict
message_webhook_source_dict = message_webhook_source_instance.to_dict()
# create an instance of MessageWebhookSource from a dict
message_webhook_source_from_dict = MessageWebhookSource.from_dict(message_webhook_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


