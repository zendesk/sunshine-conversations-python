# AttachmentDeleteBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_url** | **str** | The media URL used for a file or image message. | 

## Example

```python
from sunshine_conversations_client.model.attachment_delete_body import AttachmentDeleteBody

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentDeleteBody from a JSON string
attachment_delete_body_instance = AttachmentDeleteBody.from_json(json)
# print the JSON string representation of the object
print(AttachmentDeleteBody.to_json())

# convert the object into a dict
attachment_delete_body_dict = attachment_delete_body_instance.to_dict()
# create an instance of AttachmentDeleteBody from a dict
attachment_delete_body_from_dict = AttachmentDeleteBody.from_dict(attachment_delete_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


