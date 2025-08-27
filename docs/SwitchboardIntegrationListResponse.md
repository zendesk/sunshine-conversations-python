# SwitchboardIntegrationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboard_integrations** | [**List[SwitchboardIntegration]**](SwitchboardIntegration.md) | List of returned switchboard integrations. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_integration_list_response import SwitchboardIntegrationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardIntegrationListResponse from a JSON string
switchboard_integration_list_response_instance = SwitchboardIntegrationListResponse.from_json(json)
# print the JSON string representation of the object
print(SwitchboardIntegrationListResponse.to_json())

# convert the object into a dict
switchboard_integration_list_response_dict = switchboard_integration_list_response_instance.to_dict()
# create an instance of SwitchboardIntegrationListResponse from a dict
switchboard_integration_list_response_from_dict = SwitchboardIntegrationListResponse.from_dict(switchboard_integration_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


