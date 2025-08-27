# AndroidUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**project_id** | **str** | Your project ID from your generated private key file. | [optional] 
**client_email** | **str** | Your client email from your generated private key file. | [optional] 
**private_key** | **str** | Your private key from your generated private key file. | [optional] 
**server_key** | **str** | Your server key from the fcm console. | [optional] 
**sender_id** | **str** | Your sender id from the fcm console. | [optional] 
**can_user_see_conversation_list** | **bool** | Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where &#x60;settings.multiConvoEnabled&#x60; is set to &#x60;true&#x60;*.  | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the android integration. | [optional] 

## Example

```python
from sunshine_conversations_client.model.android_update import AndroidUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidUpdate from a JSON string
android_update_instance = AndroidUpdate.from_json(json)
# print the JSON string representation of the object
print(AndroidUpdate.to_json())

# convert the object into a dict
android_update_dict = android_update_instance.to_dict()
# create an instance of AndroidUpdate from a dict
android_update_from_dict = AndroidUpdate.from_dict(android_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


