# Custom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | To configure a custom integration you need to setup a webhook with a set of triggers and target.  | [optional] [default to 'custom']
**webhooks** | [**List[Webhook]**](Webhook.md) | An array of webhooks associated with the custom integration. | 

## Example

```python
from sunshine_conversations_client.model.custom import Custom

# TODO update the JSON string below
json = "{}"
# create an instance of Custom from a JSON string
custom_instance = Custom.from_json(json)
# print the JSON string representation of the object
print(Custom.to_json())

# convert the object into a dict
custom_dict = custom_instance.to_dict()
# create an instance of Custom from a dict
custom_from_dict = Custom.from_dict(custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


