# AttachmentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_url** | **str** | Uploaded attachment’s url.  &lt;aside class&#x3D;\&quot;notice\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; An authorization header is required to access the mediaUrl when private attachments are enabled. See [configuring private attachments for messaging](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/messaging_private_attachments/) guide for more details.&lt;/aside&gt;  | [optional] 
**media_type** | **str** | Uploaded attachment&#39;s media type | [optional] 

## Example

```python
from sunshine_conversations_client.model.attachment_schema import AttachmentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSchema from a JSON string
attachment_schema_instance = AttachmentSchema.from_json(json)
# print the JSON string representation of the object
print(AttachmentSchema.to_json())

# convert the object into a dict
attachment_schema_dict = attachment_schema_instance.to_dict()
# create an instance of AttachmentSchema from a dict
attachment_schema_from_dict = AttachmentSchema.from_dict(attachment_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


