# PassControlBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboard_integration** | **str** | The id or the name of the switchboard integration that will become active. May also use the &#x60;next&#x60; keyword to transfer control to the next switchboard integration designated in the switchboard hierarchy configuration | 
**reason** | **str** | Reason for the pass control action. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the &#x60;switchboard:passControl&#x60; webhook. | [optional] 

## Example

```python
from sunshine_conversations_client.model.pass_control_body import PassControlBody

# TODO update the JSON string below
json = "{}"
# create an instance of PassControlBody from a JSON string
pass_control_body_instance = PassControlBody.from_json(json)
# print the JSON string representation of the object
print(PassControlBody.to_json())

# convert the object into a dict
pass_control_body_dict = pass_control_body_instance.to_dict()
# create an instance of PassControlBody from a dict
pass_control_body_from_dict = PassControlBody.from_dict(pass_control_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


