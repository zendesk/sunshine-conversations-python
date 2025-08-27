# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the device. | [optional] 
**type** | **str** | The type of integration that the device represents. | [optional] 
**guid** | **str** | A unique identifier for the device, generated client-side by the SDK. | [optional] 
**client_id** | **str** | The id of the client to which this device is associated. | [optional] 
**status** | **str** | The device status. Indicates if the device will receive push notifications or not. | [optional] 
**integration_id** | **str** | The ID of the integration that the device was created for. | [optional] 
**last_seen** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the last time the user interacted with this device. | [optional] 
**push_notification_token** | **str** | The token used for push notifications on Android and iOS devices. | [optional] 
**info** | **Dict[str, object]** | A flat curated object with properties that vary for each SDK platform. All keys are optional and not guaranteed to be available. | [optional] 
**app_version** | **str** | Version of the mobile app in which the SDK is embedded. Not applicable for devices of type web. | [optional] 

## Example

```python
from sunshine_conversations_client.model.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


