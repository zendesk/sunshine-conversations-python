# SourceWithCampaignWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An identifier for the channel from which a message originated. May include one of api, sdk, messenger, or any number of other channels. | [optional] 
**integration_id** | **str** | Identifier indicating which integration the message was sent from. For user messages only. | [optional] 
**original_message_id** | **str** | Message identifier assigned by the originating channel. | [optional] 
**original_message_timestamp** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing when the third-party channel received the message. | [optional] 
**client** | [**Client**](Client.md) | The client from which the user authored the message or activity, if applicable. This field will only be present if the &#x60;includeFullSource&#x60; option is enabled for the webhook. | [optional] 
**device** | [**Device**](Device.md) | The device from which the user authored the message or activity, if applicable. This field will only be present if the &#x60;includeFullSource&#x60; option is enabled for the webhook | [optional] 
**campaign** | [**Campaign**](Campaign.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.source_with_campaign_webhook import SourceWithCampaignWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SourceWithCampaignWebhook from a JSON string
source_with_campaign_webhook_instance = SourceWithCampaignWebhook.from_json(json)
# print the JSON string representation of the object
print(SourceWithCampaignWebhook.to_json())

# convert the object into a dict
source_with_campaign_webhook_dict = source_with_campaign_webhook_instance.to_dict()
# create an instance of SourceWithCampaignWebhook from a dict
source_with_campaign_webhook_from_dict = SourceWithCampaignWebhook.from_dict(source_with_campaign_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


