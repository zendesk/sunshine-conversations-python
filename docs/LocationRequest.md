# LocationRequest

A location request action will prompt the user to share their location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | [default to 'locationRequest']
**text** | **str** | The button text. | 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.location_request import LocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LocationRequest from a JSON string
location_request_instance = LocationRequest.from_json(json)
# print the JSON string representation of the object
print(LocationRequest.to_json())

# convert the object into a dict
location_request_dict = location_request_instance.to_dict()
# create an instance of LocationRequest from a dict
location_request_from_dict = LocationRequest.from_dict(location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


