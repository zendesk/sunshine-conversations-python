# LocationMessageCoordinates

The coordinates of the location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | Global latitude. | 
**long** | **float** | Global longitude. | 

## Example

```python
from sunshine_conversations_client.model.location_message_coordinates import LocationMessageCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMessageCoordinates from a JSON string
location_message_coordinates_instance = LocationMessageCoordinates.from_json(json)
# print the JSON string representation of the object
print(LocationMessageCoordinates.to_json())

# convert the object into a dict
location_message_coordinates_dict = location_message_coordinates_instance.to_dict()
# create an instance of LocationMessageCoordinates from a dict
location_message_coordinates_from_dict = LocationMessageCoordinates.from_dict(location_message_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


