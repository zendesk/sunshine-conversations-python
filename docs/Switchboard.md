# Switchboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the switchboard. | 
**enabled** | **bool** | Whether the switchboard is enabled. Allows creating the switchboard in a disabled state so that messages don&#39;t get lost or misrouted during switchboard configuration. When a switchboard is disabled, integrations linked to the switchboard will receive all events. | 
**default_switchboard_integration_id** | **str** | The id of the switchboard integration that will be given control when a new conversation begins. It will also be used for conversations that existed before the switchboard was enabled. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard import Switchboard

# TODO update the JSON string below
json = "{}"
# create an instance of Switchboard from a JSON string
switchboard_instance = Switchboard.from_json(json)
# print the JSON string representation of the object
print(Switchboard.to_json())

# convert the object into a dict
switchboard_dict = switchboard_instance.to_dict()
# create an instance of Switchboard from a dict
switchboard_from_dict = Switchboard.from_dict(switchboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


