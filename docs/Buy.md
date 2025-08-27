# Buy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | [default to 'buy']
**text** | **str** | The button text. | 
**amount** | **int** | The amount being charged. It needs to be specified in cents and is an integer (9.99$ -&gt; 999). | 
**currency** | **str** | An ISO 4217 standard currency code in lowercase. Used for actions of type buy. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.buy import Buy

# TODO update the JSON string below
json = "{}"
# create an instance of Buy from a JSON string
buy_instance = Buy.from_json(json)
# print the JSON string representation of the object
print(Buy.to_json())

# convert the object into a dict
buy_dict = buy_instance.to_dict()
# create an instance of Buy from a dict
buy_from_dict = Buy.from_dict(buy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


