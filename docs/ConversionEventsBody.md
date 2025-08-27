# ConversionEventsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messenger** | [**MetaConversionEvent**](MetaConversionEvent.md) |  | [optional] 
**instagram** | [**MetaConversionEvent**](MetaConversionEvent.md) |  | [optional] 
**whatsapp** | [**MetaConversionEvent**](MetaConversionEvent.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversion_events_body import ConversionEventsBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionEventsBody from a JSON string
conversion_events_body_instance = ConversionEventsBody.from_json(json)
# print the JSON string representation of the object
print(ConversionEventsBody.to_json())

# convert the object into a dict
conversion_events_body_dict = conversion_events_body_instance.to_dict()
# create an instance of ConversionEventsBody from a dict
conversion_events_body_from_dict = ConversionEventsBody.from_dict(conversion_events_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


