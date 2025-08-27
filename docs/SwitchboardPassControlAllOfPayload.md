# SwitchboardPassControlAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation from which the switchboard event was fired. On success, the payload will include an &#x60;activeSwitchboardIntegration&#x60;, representing the switchboard integration that is now in control of the conversation. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**reason** | **str** | Reason for the pass control action, if applicable. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_pass_control_all_of_payload import SwitchboardPassControlAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardPassControlAllOfPayload from a JSON string
switchboard_pass_control_all_of_payload_instance = SwitchboardPassControlAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(SwitchboardPassControlAllOfPayload.to_json())

# convert the object into a dict
switchboard_pass_control_all_of_payload_dict = switchboard_pass_control_all_of_payload_instance.to_dict()
# create an instance of SwitchboardPassControlAllOfPayload from a dict
switchboard_pass_control_all_of_payload_from_dict = SwitchboardPassControlAllOfPayload.from_dict(switchboard_pass_control_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


