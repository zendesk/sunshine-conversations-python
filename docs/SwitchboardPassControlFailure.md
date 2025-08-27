# SwitchboardPassControlFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the event. May be used to ensure that an event is not processed twice in the case of a webhook that is re-tried due to an error or timeout. | [optional] 
**type** | **str** | The type of the event. Will match one of the subscribed triggers for your [webhook](#operation/CreateWebhook). | [optional] 
**created_at** | **str** | A timestamp signifying when the event was generated. Formatted as &#x60;YYYY-MM-DDThh:mm:ss.SSSZ&#x60;. | [optional] 
**payload** | [**SwitchboardAcceptControlFailureAllOfPayload**](SwitchboardAcceptControlFailureAllOfPayload.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.switchboard_pass_control_failure import SwitchboardPassControlFailure

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchboardPassControlFailure from a JSON string
switchboard_pass_control_failure_instance = SwitchboardPassControlFailure.from_json(json)
# print the JSON string representation of the object
print(SwitchboardPassControlFailure.to_json())

# convert the object into a dict
switchboard_pass_control_failure_dict = switchboard_pass_control_failure_instance.to_dict()
# create an instance of SwitchboardPassControlFailure from a dict
switchboard_pass_control_failure_from_dict = SwitchboardPassControlFailure.from_dict(switchboard_pass_control_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


