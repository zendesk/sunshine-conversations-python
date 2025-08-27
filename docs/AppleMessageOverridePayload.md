# AppleMessageOverridePayload

The exact payload to send to the channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **object** |  | [optional] 
**with_capabilities** | **List[str]** | List of capabilities needed for the override message to be received by the end user.   &#x60;LIST&#x60; : for list picker; &#x60;TIME&#x60; : for time picker; &#x60;FORM&#x60; : for form; &#x60;QUICK&#x60; : for quick reply; &#x60;AUTH2&#x60; : for authentication  | [optional] 

## Example

```python
from sunshine_conversations_client.model.apple_message_override_payload import AppleMessageOverridePayload

# TODO update the JSON string below
json = "{}"
# create an instance of AppleMessageOverridePayload from a JSON string
apple_message_override_payload_instance = AppleMessageOverridePayload.from_json(json)
# print the JSON string representation of the object
print(AppleMessageOverridePayload.to_json())

# convert the object into a dict
apple_message_override_payload_dict = apple_message_override_payload_instance.to_dict()
# create an instance of AppleMessageOverridePayload from a dict
apple_message_override_payload_from_dict = AppleMessageOverridePayload.from_dict(apple_message_override_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


