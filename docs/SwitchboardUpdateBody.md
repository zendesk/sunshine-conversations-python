# SwitchboardUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the switchboard is enabled. Allows creating the switchboard in a disabled state so that messages don&#39;t get lost or misrouted during switchboard configuration. When a switchboard is disabled, integrations linked to the switchboard will receive all events. | [optional] 
**default_switchboard_integration_id** | **str** | The id of the switchboard integration that will be given control when a new conversation begins. It will also be used for conversations that existed before the switchboard was enabled. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_update_body import SwitchboardUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardUpdateBody from a JSON string
switchboard_update_body_instance = SwitchboardUpdateBody.from_json(json)
# print the JSON string representation of the object
print(SwitchboardUpdateBody.to_json())

# convert the object into a dict
switchboard_update_body_dict = switchboard_update_body_instance.to_dict()
# create an instance of SwitchboardUpdateBody from a dict
switchboard_update_body_from_dict = SwitchboardUpdateBody.from_dict(switchboard_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


