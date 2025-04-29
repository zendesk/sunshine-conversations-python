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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


