# SwitchboardListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboards** | [**List[Switchboard]**](Switchboard.md) | List of returned switchboards. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_list_response import SwitchboardListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardListResponse from a JSON string
switchboard_list_response_instance = SwitchboardListResponse.from_json(json)
# print the JSON string representation of the object
print(SwitchboardListResponse.to_json())

# convert the object into a dict
switchboard_list_response_dict = switchboard_list_response_instance.to_dict()
# create an instance of SwitchboardListResponse from a dict
switchboard_list_response_from_dict = SwitchboardListResponse.from_dict(switchboard_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


