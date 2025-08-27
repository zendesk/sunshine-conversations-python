# CarouselMessage

Carousel messages are a horizontally scrollable set of items that may each contain text, an image, and message actions. Not all messaging channels fully support carousel messages; currently only Facebook Messenger, LINE, Telegram, Viber, the Web Messenger, the Android SDK and the iOS SDK cover the full functionality. For all other platforms a carousel message is rendered as raw text. The raw text fallback does not include any images or postback message actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'carousel']
**text** | **str** | The fallback text message used when carousel messages are not supported by the channel. | [optional] [readonly] 
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**items** | [**List[Item]**](Item.md) | An array of objects representing the items associated with the message. Only present in carousel and list type messages. | 
**display_settings** | [**CarouselMessageDisplaySettings**](CarouselMessageDisplaySettings.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.carousel_message import CarouselMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselMessage from a JSON string
carousel_message_instance = CarouselMessage.from_json(json)
# print the JSON string representation of the object
print(CarouselMessage.to_json())

# convert the object into a dict
carousel_message_dict = carousel_message_instance.to_dict()
# create an instance of CarouselMessage from a dict
carousel_message_from_dict = CarouselMessage.from_dict(carousel_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


