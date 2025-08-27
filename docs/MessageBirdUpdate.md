# MessageBirdUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.message_bird_update import MessageBirdUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageBirdUpdate from a JSON string
message_bird_update_instance = MessageBirdUpdate.from_json(json)
# print the JSON string representation of the object
print(MessageBirdUpdate.to_json())

# convert the object into a dict
message_bird_update_dict = message_bird_update_instance.to_dict()
# create an instance of MessageBirdUpdate from a dict
message_bird_update_from_dict = MessageBirdUpdate.from_dict(message_bird_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


