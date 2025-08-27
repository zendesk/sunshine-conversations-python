# SwitchboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboard** | [**Switchboard**](Switchboard.md) | The switchboard. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_response import SwitchboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardResponse from a JSON string
switchboard_response_instance = SwitchboardResponse.from_json(json)
# print the JSON string representation of the object
print(SwitchboardResponse.to_json())

# convert the object into a dict
switchboard_response_dict = switchboard_response_instance.to_dict()
# create an instance of SwitchboardResponse from a dict
switchboard_response_from_dict = SwitchboardResponse.from_dict(switchboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


