# AppleUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**authentication_message_secret** | **str** | A secret used to create the state value when sending Apple authentication 2.0 messages | [optional] 

## Example

```python
from sunshine_conversations_client.model.apple_update import AppleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AppleUpdate from a JSON string
apple_update_instance = AppleUpdate.from_json(json)
# print the JSON string representation of the object
print(AppleUpdate.to_json())

# convert the object into a dict
apple_update_dict = apple_update_instance.to_dict()
# create an instance of AppleUpdate from a dict
apple_update_from_dict = AppleUpdate.from_dict(apple_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


