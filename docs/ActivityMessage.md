# ActivityMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of system activity that generated the message. The value of this field determines the dynamic content that is rendered to the end-user / agent when viewing this message. Each &#x60;type&#x60; value will have a set of pre-defined, localized strings that describe the activity. | [default to 'ticket:transfer:email']
**data** | **Dict[str, object]** | No additional data is supplied with the \&quot;ticket:transfer:email\&quot; activity type at this time. | [optional] 

## Example

```python
from sunshine_conversations_client.model.activity_message import ActivityMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityMessage from a JSON string
activity_message_instance = ActivityMessage.from_json(json)
# print the JSON string representation of the object
print(ActivityMessage.to_json())

# convert the object into a dict
activity_message_dict = activity_message_instance.to_dict()
# create an instance of ActivityMessage from a dict
activity_message_from_dict = ActivityMessage.from_dict(activity_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


