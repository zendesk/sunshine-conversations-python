# SwitchboardAcceptControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the event. May be used to ensure that an event is not processed twice in the case of a webhook that is re-tried due to an error or timeout. | [optional] 
**type** | **str** | The type of the event. Will match one of the subscribed triggers for your [webhook](#operation/CreateWebhook). | [optional] 
**created_at** | **str** | A timestamp signifying when the event was generated. Formatted as &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60;. | [optional] 
**payload** | [**SwitchboardAcceptControlAllOfPayload**](SwitchboardAcceptControlAllOfPayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_accept_control import SwitchboardAcceptControl

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardAcceptControl from a JSON string
switchboard_accept_control_instance = SwitchboardAcceptControl.from_json(json)
# print the JSON string representation of the object
print(SwitchboardAcceptControl.to_json())

# convert the object into a dict
switchboard_accept_control_dict = switchboard_accept_control_instance.to_dict()
# create an instance of SwitchboardAcceptControl from a dict
switchboard_accept_control_from_dict = SwitchboardAcceptControl.from_dict(switchboard_accept_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


