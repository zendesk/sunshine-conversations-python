# LocationMessageLocation

Information about the location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A string representing the address of the location. | [optional] 
**name** | **str** | A string representing the name of the location. | [optional] 

## Example

```python
from sunshine_conversations_client.model.location_message_location import LocationMessageLocation

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMessageLocation from a JSON string
location_message_location_instance = LocationMessageLocation.from_json(json)
# print the JSON string representation of the object
print(LocationMessageLocation.to_json())

# convert the object into a dict
location_message_location_dict = location_message_location_instance.to_dict()
# create an instance of LocationMessageLocation from a dict
location_message_location_from_dict = LocationMessageLocation.from_dict(location_message_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


