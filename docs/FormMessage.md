# FormMessage

A form type message without text or actions. Only supported in the Web SDK.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'form']
**submitted** | **bool** | Flag which states whether the form is submitted. | [optional] [readonly] 
**block_chat_input** | **bool** | true if the message should block the chat input on Web Messenger. | [optional] 
**fields** | [**list[FormMessageField]**](FormMessageField.md) | An array of objects representing fields associated with the message. Only present in form and formResponse messages. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


