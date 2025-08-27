# WebhookCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | URL to be called when the webhook is triggered. | 
**triggers** | **List[str]** | An array of triggers the integration is subscribed to. This property is case sensitive. [More details](https://developer.zendesk.com/api-reference/conversations/#section/Webhook-Triggers). | 
**include_full_user** | **bool** | A boolean specifying whether webhook payloads should include the complete user schema for events involving a specific user. | [optional] [default to False]
**include_full_source** | **bool** | A boolean specifying whether webhook payloads should include the client and device object (when applicable). | [optional] [default to False]

## Example

```python
from sunshine_conversations_client.model.webhook_create_body import WebhookCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateBody from a JSON string
webhook_create_body_instance = WebhookCreateBody.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateBody.to_json())

# convert the object into a dict
webhook_create_body_dict = webhook_create_body_instance.to_dict()
# create an instance of WebhookCreateBody from a dict
webhook_create_body_from_dict = WebhookCreateBody.from_dict(webhook_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


