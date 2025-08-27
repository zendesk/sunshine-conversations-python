# ClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**Client**](Client.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.client_response import ClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientResponse from a JSON string
client_response_instance = ClientResponse.from_json(json)
# print the JSON string representation of the object
print(ClientResponse.to_json())

# convert the object into a dict
client_response_dict = client_response_instance.to_dict()
# create an instance of ClientResponse from a dict
client_response_from_dict = ClientResponse.from_dict(client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


