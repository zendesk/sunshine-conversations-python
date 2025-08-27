# ConversationTruncated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the conversation. | [optional] 
**type** | [**ConversationType**](ConversationType.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**active_switchboard_integration** | [**SwitchboardIntegrationWebhook**](SwitchboardIntegrationWebhook.md) | The current switchboard integration that is in control of the conversation. This field is omitted if no &#x60;activeSwitchboardIntegration&#x60; exists for the conversation. | [optional] 
**pending_switchboard_integration** | [**SwitchboardIntegrationWebhook**](SwitchboardIntegrationWebhook.md) | The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_truncated import ConversationTruncated

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationTruncated from a JSON string
conversation_truncated_instance = ConversationTruncated.from_json(json)
# print the JSON string representation of the object
print(ConversationTruncated.to_json())

# convert the object into a dict
conversation_truncated_dict = conversation_truncated_instance.to_dict()
# create an instance of ConversationTruncated from a dict
conversation_truncated_from_dict = ConversationTruncated.from_dict(conversation_truncated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


