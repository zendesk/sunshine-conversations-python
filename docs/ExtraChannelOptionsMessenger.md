# ExtraChannelOptionsMessenger

Messenger channel options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messenger_extensions** | **bool** | For webview type actions, a boolean value indicating whether the URL should be loaded with Messenger Extensions enabled. [More info](https://developers.facebook.com/docs/messenger-platform/send-api-reference/url-button). | [optional] [default to False]
**webview_share_button** | **str** | For webview type actions, a string value indicating if the share button should be hidden. [More Info](https://developers.facebook.com/docs/messenger-platform/reference/buttons/url). | [optional] 

## Example

```python
from sunshine_conversations_client.model.extra_channel_options_messenger import ExtraChannelOptionsMessenger

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChannelOptionsMessenger from a JSON string
extra_channel_options_messenger_instance = ExtraChannelOptionsMessenger.from_json(json)
# print the JSON string representation of the object
print(ExtraChannelOptionsMessenger.to_json())

# convert the object into a dict
extra_channel_options_messenger_dict = extra_channel_options_messenger_instance.to_dict()
# create an instance of ExtraChannelOptionsMessenger from a dict
extra_channel_options_messenger_from_dict = ExtraChannelOptionsMessenger.from_dict(extra_channel_options_messenger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


