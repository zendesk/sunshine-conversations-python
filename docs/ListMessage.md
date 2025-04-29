# ListMessage

List messages are a vertically scrollable set of items that may each contain text, an image, and message actions. Not all messaging channels fully support list messages. * Facebook Messenger and WeChat have native support. * For LINE and our Android, iOS and Web SDK, Sunshine Conversations converts list messages to carousel. * On WhatsApp, Telegram and Twitter, Sunshine Conversations converts list messages to multiple rich messages. * On all other platforms, Sunshine Conversations converts list messages to raw text. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'list']
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**items** | [**list[Item]**](Item.md) | An array of objects representing the items associated with the message. Only present in carousel and list type messages. | 
**actions** | [**list[ActionSubset]**](ActionSubset.md) | An array of objects representing the actions associated with the message. The array length is limited by the third party channel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


