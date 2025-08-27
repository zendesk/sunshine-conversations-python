# ReleaseControlBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for the release control action. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the &#x60;switchboard:releaseControl&#x60; webhook. | [optional] 

## Example

```python
from sunshine_conversations_client.model.release_control_body import ReleaseControlBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseControlBody from a JSON string
release_control_body_instance = ReleaseControlBody.from_json(json)
# print the JSON string representation of the object
print(ReleaseControlBody.to_json())

# convert the object into a dict
release_control_body_dict = release_control_body_instance.to_dict()
# create an instance of ReleaseControlBody from a dict
release_control_body_from_dict = ReleaseControlBody.from_dict(release_control_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


