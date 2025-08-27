# ClientUpdateEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation which triggered a change in the client. | [optional] 
**user** | [**UserTruncated**](UserTruncated.md) | The user associated with the client. | [optional] 
**client** | [**Client**](Client.md) | The updated client. | [optional] 
**reason** | **str** | The reason for which the client was updated. * &#x60;confirmed&#x60; - The client is now active and ready to use. * &#x60;blocked&#x60; - The user has unsubscribed from the conversation. * &#x60;unblocked&#x60; - A previously unsubscribed user resubscribed to the conversation. * &#x60;matched&#x60; - The channel found a user that matches the information provided.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.client_update_event_all_of_payload import ClientUpdateEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUpdateEventAllOfPayload from a JSON string
client_update_event_all_of_payload_instance = ClientUpdateEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ClientUpdateEventAllOfPayload.to_json())

# convert the object into a dict
client_update_event_all_of_payload_dict = client_update_event_all_of_payload_instance.to_dict()
# create an instance of ClientUpdateEventAllOfPayload from a dict
client_update_event_all_of_payload_from_dict = ClientUpdateEventAllOfPayload.from_dict(client_update_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


