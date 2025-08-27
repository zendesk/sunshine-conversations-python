# PostbackWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | The payload associated with the postback. | [optional] 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.postback_webhook import PostbackWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PostbackWebhook from a JSON string
postback_webhook_instance = PostbackWebhook.from_json(json)
# print the JSON string representation of the object
print(PostbackWebhook.to_json())

# convert the object into a dict
postback_webhook_dict = postback_webhook_instance.to_dict()
# create an instance of PostbackWebhook from a dict
postback_webhook_from_dict = PostbackWebhook.from_dict(postback_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


