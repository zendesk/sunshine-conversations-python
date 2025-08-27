# SwitchboardAcceptControlAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation from which the switchboard event was fired. Will include an &#x60;activeSwitchboardIntegration&#x60; representing the integration that has just accepted control. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_accept_control_all_of_payload import SwitchboardAcceptControlAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardAcceptControlAllOfPayload from a JSON string
switchboard_accept_control_all_of_payload_instance = SwitchboardAcceptControlAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(SwitchboardAcceptControlAllOfPayload.to_json())

# convert the object into a dict
switchboard_accept_control_all_of_payload_dict = switchboard_accept_control_all_of_payload_instance.to_dict()
# create an instance of SwitchboardAcceptControlAllOfPayload from a dict
switchboard_accept_control_all_of_payload_from_dict = SwitchboardAcceptControlAllOfPayload.from_dict(switchboard_accept_control_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


