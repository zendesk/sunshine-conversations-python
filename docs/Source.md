# Source

The source of the message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An identifier for the channel from which a message originated. May include one of api, sdk, messenger, or any number of other channels. | 
**integration_id** | **str** | Identifier indicating which integration the message was sent from. For user messages only. | [optional] 
**original_message_id** | **str** | Message identifier assigned by the originating channel. | [optional] 
**original_message_timestamp** | **str** | A datetime string with the format &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60; representing when the third party channel received the message. | [optional] 
**client** | [**Client**](Client.md) | The client from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the &#x60;includeFullSource&#x60; option is enabled. | [optional] 
**device** | [**Device**](Device.md) | The device from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the &#x60;includeFullSource&#x60; option is enabled. | [optional] 

## Example

```python
from sunshine_conversations_client.model.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


