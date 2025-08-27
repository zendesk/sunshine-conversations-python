# ClientAddEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation associated with the creation of the client. This field is only present when the reason is &#x60;channelLinking&#x60; and when attaching the client to a specific conversation.  | [optional] 
**user** | [**UserTruncated**](UserTruncated.md) | The user associated with the client. | [optional] 
**client** | [**Client**](Client.md) | The client that was just created. | [optional] 
**reason** | **str** | The reason for which the client was added. * &#x60;channelLinking&#x60; - The client was created as a result of initiating a channel link. * &#x60;sdkLogin&#x60; - The client was created as a result of logging into an SDK device. * &#x60;authCode&#x60; - The client was created as a result of initializing an SDK client with an &#x60;authCode&#x60;.  | [optional] 
**source** | [**SourceWebhook**](SourceWebhook.md) | The source where this event originated from. This could be the API or an SDK device. | [optional] 

## Example

```python
from sunshine_conversations_client.model.client_add_event_all_of_payload import ClientAddEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAddEventAllOfPayload from a JSON string
client_add_event_all_of_payload_instance = ClientAddEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ClientAddEventAllOfPayload.to_json())

# convert the object into a dict
client_add_event_all_of_payload_dict = client_add_event_all_of_payload_instance.to_dict()
# create an instance of ClientAddEventAllOfPayload from a dict
client_add_event_all_of_payload_from_dict = ClientAddEventAllOfPayload.from_dict(client_add_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


