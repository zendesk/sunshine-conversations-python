# IntegrationApiKeyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[ApiKey]**](ApiKey.md) | Integration keys of the supplied integration. | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration_api_key_list_response import IntegrationApiKeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationApiKeyListResponse from a JSON string
integration_api_key_list_response_instance = IntegrationApiKeyListResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationApiKeyListResponse.to_json())

# convert the object into a dict
integration_api_key_list_response_dict = integration_api_key_list_response_instance.to_dict()
# create an instance of IntegrationApiKeyListResponse from a dict
integration_api_key_list_response_from_dict = IntegrationApiKeyListResponse.from_dict(integration_api_key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


