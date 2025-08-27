# AuthorWebhook

The author of the activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The &#x60;type&#x60; of the author. | 
**user_id** | **str** | The id of the user. Only supported when author &#x60;type&#x60; is &#x60;user&#x60;. | [optional] 
**user** | [**User**](User.md) | The user that authored the message or activity. &#x60;profile&#x60; is included in the payload if the &#x60;includeFullUser&#x60; option is enabled. | [optional] 

## Example

```python
from sunshine_conversations_client.model.author_webhook import AuthorWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorWebhook from a JSON string
author_webhook_instance = AuthorWebhook.from_json(json)
# print the JSON string representation of the object
print(AuthorWebhook.to_json())

# convert the object into a dict
author_webhook_dict = author_webhook_instance.to_dict()
# create an instance of AuthorWebhook from a dict
author_webhook_from_dict = AuthorWebhook.from_dict(author_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


