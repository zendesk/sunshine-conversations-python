# InstagramConversionEventsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instagram** | [**MetaConversionEvent**](MetaConversionEvent.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.instagram_conversion_events_body import InstagramConversionEventsBody

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramConversionEventsBody from a JSON string
instagram_conversion_events_body_instance = InstagramConversionEventsBody.from_json(json)
# print the JSON string representation of the object
print(InstagramConversionEventsBody.to_json())

# convert the object into a dict
instagram_conversion_events_body_dict = instagram_conversion_events_body_instance.to_dict()
# create an instance of InstagramConversionEventsBody from a dict
instagram_conversion_events_body_from_dict = InstagramConversionEventsBody.from_dict(instagram_conversion_events_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


