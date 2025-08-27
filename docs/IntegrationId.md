# IntegrationId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The id of the integration to deliver the message to. Will return an error if the integration does not exist or if the user does not have a client for the integration attached to the conversation.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.integration_id import IntegrationId

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationId from a JSON string
integration_id_instance = IntegrationId.from_json(json)
# print the JSON string representation of the object
print(IntegrationId.to_json())

# convert the object into a dict
integration_id_dict = integration_id_instance.to_dict()
# create an instance of IntegrationId from a dict
integration_id_from_dict = IntegrationId.from_dict(integration_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


