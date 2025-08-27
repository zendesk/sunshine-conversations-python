# DeviceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**Device**](Device.md) | The device. | [optional] 

## Example

```python
from sunshine_conversations_client.model.device_response import DeviceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceResponse from a JSON string
device_response_instance = DeviceResponse.from_json(json)
# print the JSON string representation of the object
print(DeviceResponse.to_json())

# convert the object into a dict
device_response_dict = device_response_instance.to_dict()
# create an instance of DeviceResponse from a dict
device_response_from_dict = DeviceResponse.from_dict(device_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


