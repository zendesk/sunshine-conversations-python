# SwitchboardIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboard_integration** | [**SwitchboardIntegration**](SwitchboardIntegration.md) | The switchboard integration. | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_integration_response import SwitchboardIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardIntegrationResponse from a JSON string
switchboard_integration_response_instance = SwitchboardIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(SwitchboardIntegrationResponse.to_json())

# convert the object into a dict
switchboard_integration_response_dict = switchboard_integration_response_instance.to_dict()
# create an instance of SwitchboardIntegrationResponse from a dict
switchboard_integration_response_from_dict = SwitchboardIntegrationResponse.from_dict(switchboard_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


