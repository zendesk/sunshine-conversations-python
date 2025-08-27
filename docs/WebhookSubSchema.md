# WebhookSubSchema

The webhook that generated the payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the webhook. | [optional] 
**version** | **str** | Schema version of the payload delivered to this webhook (v2). | [optional] 

## Example

```python
from sunshine_conversations_client.model.webhook_sub_schema import WebhookSubSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubSchema from a JSON string
webhook_sub_schema_instance = WebhookSubSchema.from_json(json)
# print the JSON string representation of the object
print(WebhookSubSchema.to_json())

# convert the object into a dict
webhook_sub_schema_dict = webhook_sub_schema_instance.to_dict()
# create an instance of WebhookSubSchema from a dict
webhook_sub_schema_from_dict = WebhookSubSchema.from_dict(webhook_sub_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


