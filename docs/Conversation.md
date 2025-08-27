# Conversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the conversation. | [optional] 
**type** | [**ConversationType**](ConversationType.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**active_switchboard_integration** | [**SwitchboardIntegrationWebhook**](SwitchboardIntegrationWebhook.md) | The current switchboard integration that is in control of the conversation. This field is omitted if no &#x60;activeSwitchboardIntegration&#x60; exists for the conversation. | [optional] 
**pending_switchboard_integration** | [**SwitchboardIntegrationWebhook**](SwitchboardIntegrationWebhook.md) | The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control. | [optional] 
**is_default** | **bool** | Whether the conversation is the default conversation for the user. Will be true for the first personal conversation created for the user, and false in all other cases.  | [optional] 
**display_name** | **str** | A friendly name for the conversation, may be displayed to the business or the user.  | [optional] 
**description** | **str** | A short text describing the conversation. | [optional] 
**icon_url** | **str** | A custom conversation icon url. The image must be in either JPG, PNG, or GIF format | [optional] 
**business_last_read** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the conversation was last marked as read with role business.  | [optional] 
**last_updated_at** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the last message was received in the conversation, or the creation time if no messages have been received yet.  | [optional] 
**created_at** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the creation time of the conversation.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print(Conversation.to_json())

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_from_dict = Conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


