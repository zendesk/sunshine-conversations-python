# Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the message. | [optional] 
**received** | **str** | A datetime string with the format &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60; representing when Sunshine Conversations received the message. | [optional] 
**author** | [**Author**](Author.md) |  | [optional] 
**activity** | [**ActivityMessage**](ActivityMessage.md) | Details of the system activity that generated this message. This field is used when actions taken by the system generate a persisted message to notify the user or agent of an event that occurred. For example, when a user&#39;s Ticket gets closed. This property applies only to informational text messages generated via system events. | [optional] 
**content** | [**Content**](Content.md) | The content of the message. | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**quoted_message** | [**QuotedMessage**](QuotedMessage.md) | The quoted message is currently only available for WhatsApp and Web Messenger &#x60;formResponse&#x60; messages. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**deleted** | **bool** | true if the message serves as a placeholder for one that has been deleted. | [optional] 

## Example

```python
from sunshine_conversations_client.model.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


