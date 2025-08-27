# AcceptControlBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the &#x60;switchboard:acceptControl&#x60; and &#x60;switchboard:acceptControl:failure&#x60; webhooks. | [optional] 

## Example

```python
from sunshine_conversations_client.model.accept_control_body import AcceptControlBody

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptControlBody from a JSON string
accept_control_body_instance = AcceptControlBody.from_json(json)
# print the JSON string representation of the object
print(AcceptControlBody.to_json())

# convert the object into a dict
accept_control_body_dict = accept_control_body_instance.to_dict()
# create an instance of AcceptControlBody from a dict
accept_control_body_from_dict = AcceptControlBody.from_dict(accept_control_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


