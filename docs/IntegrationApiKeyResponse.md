# IntegrationApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ApiKey**](ApiKey.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration_api_key_response import IntegrationApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationApiKeyResponse from a JSON string
integration_api_key_response_instance = IntegrationApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationApiKeyResponse.to_json())

# convert the object into a dict
integration_api_key_response_dict = integration_api_key_response_instance.to_dict()
# create an instance of IntegrationApiKeyResponse from a dict
integration_api_key_response_from_dict = IntegrationApiKeyResponse.from_dict(integration_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


