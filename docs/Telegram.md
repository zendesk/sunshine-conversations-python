# Telegram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | To configure a Telegram integration, acquire the required information from the user and call the Create Integration endpoint.  | [optional] [default to 'telegram']
**token** | **str** | Telegram Bot Token. | 
**username** | **str** | Username of the botId | [optional] [readonly] 
**bot_id** | **str** | A human-friendly name used to identify the integration. | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.telegram import Telegram

# TODO update the JSON string below
json = "{}"
# create an instance of Telegram from a JSON string
telegram_instance = Telegram.from_json(json)
# print the JSON string representation of the object
print(Telegram.to_json())

# convert the object into a dict
telegram_dict = telegram_instance.to_dict()
# create an instance of Telegram from a dict
telegram_from_dict = Telegram.from_dict(telegram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


