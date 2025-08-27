# MetaConversionEvent

The conversion event data expected by Meta.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**MetaConversionEventPayload**](MetaConversionEventPayload.md) |  | 

## Example

```python
from sunshine_conversations_client.model.meta_conversion_event import MetaConversionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MetaConversionEvent from a JSON string
meta_conversion_event_instance = MetaConversionEvent.from_json(json)
# print the JSON string representation of the object
print(MetaConversionEvent.to_json())

# convert the object into a dict
meta_conversion_event_dict = meta_conversion_event_instance.to_dict()
# create an instance of MetaConversionEvent from a dict
meta_conversion_event_from_dict = MetaConversionEvent.from_dict(meta_conversion_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


