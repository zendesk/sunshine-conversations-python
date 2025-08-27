# IosUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**certificate** | **str** | The binary of your APN certificate base64 encoded. | [optional] 
**password** | **str** | The password for your APN certificate. | [optional] 
**production** | **bool** | The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified. | [optional] 
**auto_update_badge** | **bool** | Use the unread count of the conversation as the application badge. | [optional] 
**can_user_see_conversation_list** | **bool** | Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where &#x60;settings.multiConvoEnabled&#x60; is set to &#x60;true&#x60;*.  | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the iOS integration. | [optional] 

## Example

```python
from sunshine_conversations_client.model.ios_update import IosUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IosUpdate from a JSON string
ios_update_instance = IosUpdate.from_json(json)
# print the JSON string representation of the object
print(IosUpdate.to_json())

# convert the object into a dict
ios_update_dict = ios_update_instance.to_dict()
# create an instance of IosUpdate from a dict
ios_update_from_dict = IosUpdate.from_dict(ios_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


