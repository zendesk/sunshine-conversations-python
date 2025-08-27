# ClientAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ClientType**](ClientType.md) |  | [optional] 
**client_id** | **str** | The id of the client being referenced. | [optional] 

## Example

```python
from sunshine_conversations_client.model.client_association import ClientAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAssociation from a JSON string
client_association_instance = ClientAssociation.from_json(json)
# print the JSON string representation of the object
print(ClientAssociation.to_json())

# convert the object into a dict
client_association_dict = client_association_instance.to_dict()
# create an instance of ClientAssociation from a dict
client_association_from_dict = ClientAssociation.from_dict(client_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


