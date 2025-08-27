# ClientCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_criteria** | [**MatchCriteria**](MatchCriteria.md) |  | 
**confirmation** | [**Confirmation**](Confirmation.md) |  | 
**target** | [**Target**](Target.md) |  | 

## Example

```python
from sunshine_conversations_client.model.client_create import ClientCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCreate from a JSON string
client_create_instance = ClientCreate.from_json(json)
# print the JSON string representation of the object
print(ClientCreate.to_json())

# convert the object into a dict
client_create_dict = client_create_instance.to_dict()
# create an instance of ClientCreate from a dict
client_create_from_dict = ClientCreate.from_dict(client_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


