# ClientListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**List[Client]**](Client.md) | List of returned clients. | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.client_list_response import ClientListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientListResponse from a JSON string
client_list_response_instance = ClientListResponse.from_json(json)
# print the JSON string representation of the object
print(ClientListResponse.to_json())

# convert the object into a dict
client_list_response_dict = client_list_response_instance.to_dict()
# create an instance of ClientListResponse from a dict
client_list_response_from_dict = ClientListResponse.from_dict(client_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


