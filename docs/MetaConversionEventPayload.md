# MetaConversionEventPayload

The payload to be sent to Meta's conversion events API. Should contain the exact structure expected by [Meta's Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event) except for the `user_data` field, which will be provided by Zendesk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | The array of conversion events to be sent to Meta&#39;s conversion events API. | 

## Example

```python
from sunshine_conversations_client.model.meta_conversion_event_payload import MetaConversionEventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MetaConversionEventPayload from a JSON string
meta_conversion_event_payload_instance = MetaConversionEventPayload.from_json(json)
# print the JSON string representation of the object
print(MetaConversionEventPayload.to_json())

# convert the object into a dict
meta_conversion_event_payload_dict = meta_conversion_event_payload_instance.to_dict()
# create an instance of MetaConversionEventPayload from a dict
meta_conversion_event_payload_from_dict = MetaConversionEventPayload.from_dict(meta_conversion_event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


