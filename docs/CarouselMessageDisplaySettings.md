# CarouselMessageDisplaySettings

Settings to adjust the carousel layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_aspect_ratio** | **str** | Specifies how to display all carousel images. Valid values are horizontal (default) and square. Only supported in Facebook Messenger, Web Messenger, Android SDK and iOS SDK carousels. | [optional] 

## Example

```python
from sunshine_conversations_client.model.carousel_message_display_settings import CarouselMessageDisplaySettings

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselMessageDisplaySettings from a JSON string
carousel_message_display_settings_instance = CarouselMessageDisplaySettings.from_json(json)
# print the JSON string representation of the object
print(CarouselMessageDisplaySettings.to_json())

# convert the object into a dict
carousel_message_display_settings_dict = carousel_message_display_settings_instance.to_dict()
# create an instance of CarouselMessageDisplaySettings from a dict
carousel_message_display_settings_from_dict = CarouselMessageDisplaySettings.from_dict(carousel_message_display_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


