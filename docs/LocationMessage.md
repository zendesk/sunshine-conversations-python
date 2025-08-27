# LocationMessage

A location type message includes the coordinates (latitude and longitude) of a location and an optional location object which can include the name and address of the location. Typically sent in response to a Location Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'location']
**text** | **str** | The fallback text message used when location messages are not supported by the channel. | [optional] [readonly] 
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**coordinates** | [**LocationMessageCoordinates**](LocationMessageCoordinates.md) |  | 
**location** | [**LocationMessageLocation**](LocationMessageLocation.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.location_message import LocationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMessage from a JSON string
location_message_instance = LocationMessage.from_json(json)
# print the JSON string representation of the object
print(LocationMessage.to_json())

# convert the object into a dict
location_message_dict = location_message_instance.to_dict()
# create an instance of LocationMessage from a dict
location_message_from_dict = LocationMessage.from_dict(location_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


