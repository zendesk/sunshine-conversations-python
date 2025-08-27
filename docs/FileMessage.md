# FileMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'file']
**media_url** | **str** | The URL for media, such as an image, attached to the message. &lt;aside class&#x3D;\&quot;notice\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; An authorization header is required to access the mediaUrl when private attachments are enabled. See [configuring private attachments for messaging](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/messaging_private_attachments/) guide for more details.&lt;/aside&gt;  | 
**media_size** | **float** | The size of the media. | [optional] [readonly] 
**media_type** | **str** | The media type of the file. | [optional] [readonly] 
**alt_text** | **str** | An optional description of the file for accessibility purposes. The field will be saved by default with the file name as the value. | [optional] 
**text** | **str** | The text content of the message. | [optional] 
**block_chat_input** | **bool** | When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user&#39;s ability to send messages in the conversation. | [optional] 
**html_text** | **str** | HTML text content of the message. Can be provided in place of &#x60;text&#x60;. Cannot be used with &#x60;markdownText&#x60;. If no &#x60;text&#x60; is provided, will be converted to &#x60;text&#x60; upon reception to be displayed on channels that do not support rich text. See [rich text](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/structured-messages/#rich-text) documentation for more information. | [optional] 
**markdown_text** | **str** | Markdown text content of the message. Can be provided in place of &#x60;text&#x60;. Cannot be used with &#x60;htmlText&#x60;. Will be converted to &#x60;htmlText&#x60; upon reception. If converted &#x60;htmlText&#x60; exceeds 4096 characters, the message will be rejected. If no &#x60;text&#x60; is provided, will be converted to &#x60;text&#x60; upon reception to be displayed on channels that do not support rich text. See [rich text](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/structured-messages/#rich-text) documentation for more information. | [optional] 
**attachment_id** | **str** | An identifier used by Sunshine Conversations for internal purposes. | [optional] 

## Example

```python
from sunshine_conversations_client.model.file_message import FileMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FileMessage from a JSON string
file_message_instance = FileMessage.from_json(json)
# print the JSON string representation of the object
print(FileMessage.to_json())

# convert the object into a dict
file_message_dict = file_message_instance.to_dict()
# create an instance of FileMessage from a dict
file_message_from_dict = FileMessage.from_dict(file_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


