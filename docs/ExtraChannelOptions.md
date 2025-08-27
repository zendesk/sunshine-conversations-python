# ExtraChannelOptions

Extra options to pass directly to the channel API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messenger** | [**ExtraChannelOptionsMessenger**](ExtraChannelOptionsMessenger.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.extra_channel_options import ExtraChannelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChannelOptions from a JSON string
extra_channel_options_instance = ExtraChannelOptions.from_json(json)
# print the JSON string representation of the object
print(ExtraChannelOptions.to_json())

# convert the object into a dict
extra_channel_options_dict = extra_channel_options_instance.to_dict()
# create an instance of ExtraChannelOptions from a dict
extra_channel_options_from_dict = ExtraChannelOptions.from_dict(extra_channel_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


