# TextMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'text']
**text** | **str** | The text content of the message. Required unless &#x60;actions&#x60;, &#x60;htmlText&#x60; or &#x60;markdownText&#x60; is provided. | [optional] 
**html_text** | **str** | HTML text content of the message. Can be provided in place of &#x60;text&#x60;. Cannot be used with &#x60;markdownText&#x60;. If no &#x60;text&#x60; is provided, will be converted to &#x60;text&#x60; upon reception to be displayed on channels that do not support rich text. See [rich text](https://docs.smooch.io/guide/structured-messages/rich-text) documentation for more information. | [optional] 
**markdown_text** | **str** | Markdown text content of the message. Can be provided in place of &#x60;text&#x60;. Cannot be used with &#x60;htmlText&#x60;. Will be converted to &#x60;htmlText&#x60; upon reception. If converted &#x60;htmlText&#x60; exceeds 4096 characters, the message will be rejected. If no &#x60;text&#x60; is provided, will be converted to &#x60;text&#x60; upon reception to be displayed on channels that do not support rich text. See [rich text](https://docs.smooch.io/guide/structured-messages/rich-text) documentation for more information. | [optional] 
**actions** | [**list[Action]**](Action.md) | Array of message actions. | [optional] 
**payload** | **str** | The payload of a [reply button](https://docs.smooch.io/guide/structured-messages/#reply-buttons) response message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


