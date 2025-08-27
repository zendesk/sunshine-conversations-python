# IntegrationApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the API key. | 

## Example

```python
from sunshine_conversations_client.model.integration_api_key import IntegrationApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationApiKey from a JSON string
integration_api_key_instance = IntegrationApiKey.from_json(json)
# print the JSON string representation of the object
print(IntegrationApiKey.to_json())

# convert the object into a dict
integration_api_key_dict = integration_api_key_instance.to_dict()
# create an instance of IntegrationApiKey from a dict
integration_api_key_from_dict = IntegrationApiKey.from_dict(integration_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


