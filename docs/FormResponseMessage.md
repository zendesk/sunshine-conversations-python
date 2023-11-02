# FormResponseMessage

A formResponse type message is a response to a form type message. formResponse type messages are only supported as responses to form messages on Web Messenger and cannot be sent via the API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'formResponse']
**fields** | [**list[FormResponseMessageField]**](FormResponseMessageField.md) | Array of field objects that contain the submitted fields. | 
**text_fallback** | **str** | A string containing the &#x60;label: value&#x60; of all fields, each separated by a newline character. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


