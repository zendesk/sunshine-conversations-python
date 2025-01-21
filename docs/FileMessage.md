# FileMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of message. | [default to 'file']
**media_url** | **str** | The URL for media, such as an image, attached to the message. &lt;aside class&#x3D;\&quot;notice\&quot;&gt;Note that for private attachments an authorization header is required to access the mediaUrl. See &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/messaging_private_attachments/\&quot;&gt;Configuring private attachments for messaging&lt;/a&gt; guide for more details.&lt;/aside&gt;  | 
**media_size** | **float** | The size of the media. | [optional] [readonly] 
**media_type** | **str** | The media type of the file. | [optional] [readonly] 
**alt_text** | **str** | An optional description of the file for accessibility purposes. The field will be saved by default with the file name as the value. | [optional] 
**text** | **str** | The text content of the message. | [optional] 
**attachment_id** | **str** | An identifier used by Sunshine Conversations for internal purposes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


