# WhatsAppConversionEventsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whatsapp** | [**MetaConversionEvent**](MetaConversionEvent.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.whats_app_conversion_events_body import WhatsAppConversionEventsBody

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsAppConversionEventsBody from a JSON string
whats_app_conversion_events_body_instance = WhatsAppConversionEventsBody.from_json(json)
# print the JSON string representation of the object
print(WhatsAppConversionEventsBody.to_json())

# convert the object into a dict
whats_app_conversion_events_body_dict = whats_app_conversion_events_body_instance.to_dict()
# create an instance of WhatsAppConversionEventsBody from a dict
whats_app_conversion_events_body_from_dict = WhatsAppConversionEventsBody.from_dict(whats_app_conversion_events_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


