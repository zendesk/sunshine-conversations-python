# DownloadMessageRefBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The id of the user. | 
**apple** | [**DownloadMessageRefBodyAllOfApple**](DownloadMessageRefBodyAllOfApple.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.download_message_ref_body import DownloadMessageRefBody

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadMessageRefBody from a JSON string
download_message_ref_body_instance = DownloadMessageRefBody.from_json(json)
# print the JSON string representation of the object
print(DownloadMessageRefBody.to_json())

# convert the object into a dict
download_message_ref_body_dict = download_message_ref_body_instance.to_dict()
# create an instance of DownloadMessageRefBody from a dict
download_message_ref_body_from_dict = DownloadMessageRefBody.from_dict(download_message_ref_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


