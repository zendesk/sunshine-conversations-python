# SourceWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An identifier for the channel from which a message originated. May include one of api, sdk, messenger, or any number of other channels. | [optional] 
**integration_id** | **str** | Identifier indicating which integration the message was sent from. For user messages only. | [optional] 
**original_message_id** | **str** | Message identifier assigned by the originating channel. | [optional] 
**original_message_timestamp** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing when the third-party channel received the message. | [optional] 
**client** | [**Client**](Client.md) | The client from which the user authored the message or activity, if applicable. This field will only be present if the &#x60;includeFullSource&#x60; option is enabled for the webhook. | [optional] 
**device** | [**Device**](Device.md) | The device from which the user authored the message or activity, if applicable. This field will only be present if the &#x60;includeFullSource&#x60; option is enabled for the webhook | [optional] 

## Example

```python
from sunshine_conversations_client.model.source_webhook import SourceWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SourceWebhook from a JSON string
source_webhook_instance = SourceWebhook.from_json(json)
# print the JSON string representation of the object
print(SourceWebhook.to_json())

# convert the object into a dict
source_webhook_dict = source_webhook_instance.to_dict()
# create an instance of SourceWebhook from a dict
source_webhook_from_dict = SourceWebhook.from_dict(source_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


