# ClientRemoveEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation associated with the removal of the client. This field is only present when the reason is &#x60;theft&#x60;, &#x60;linkCancelled&#x60; or &#x60;linkFailed&#x60;. Note that for the &#x60;theft&#x60; reason, the conversation will not be present if it has been deleted.  | [optional] 
**user** | [**UserTruncated**](UserTruncated.md) | The user associated with the client. | [optional] 
**client** | [**Client**](Client.md) | The removed client. | [optional] 
**reason** | **str** | The reason for which the client was removed. * &#x60;api&#x60; - The client was removed using the API. * &#x60;linkCancelled&#x60; - The user cancelled a channel link. * &#x60;linkFailed&#x60; - The client was removed after a channel link attempt failed. * &#x60;sdk&#x60; - The client was removed using the SDK. * &#x60;theft&#x60; - The client was transferred to another user due to a channel link.  | [optional] 
**error** | **object** | Object containing details of what went wrong. This field will only be present when the reason is &#x60;linkCancelled&#x60; or &#x60;linkFailed&#x60;. | [optional] 
**source** | [**SourceWebhook**](SourceWebhook.md) | The source where this event originated from. This could be the API or an SDK device. | [optional] 

## Example

```python
from sunshine_conversations_client.model.client_remove_event_all_of_payload import ClientRemoveEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClientRemoveEventAllOfPayload from a JSON string
client_remove_event_all_of_payload_instance = ClientRemoveEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ClientRemoveEventAllOfPayload.to_json())

# convert the object into a dict
client_remove_event_all_of_payload_dict = client_remove_event_all_of_payload_instance.to_dict()
# create an instance of ClientRemoveEventAllOfPayload from a dict
client_remove_event_all_of_payload_from_dict = ClientRemoveEventAllOfPayload.from_dict(client_remove_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


