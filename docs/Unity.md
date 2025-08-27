# Unity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | To configure a Unity integration, create an integration with type &#39;unity&#39; by calling the Create Integration endpoint.  | [optional] [default to 'unity']
**can_user_see_conversation_list** | **bool** | Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where &#x60;settings.multiConvoEnabled&#x60; is set to &#x60;true&#x60;*.  | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the Unity integration. | [optional] 
**attachments_enabled** | **bool** | Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.  | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.unity import Unity

# TODO update the JSON string below
json = "{}"
# create an instance of Unity from a JSON string
unity_instance = Unity.from_json(json)
# print the JSON string representation of the object
print(Unity.to_json())

# convert the object into a dict
unity_dict = unity_instance.to_dict()
# create an instance of Unity from a dict
unity_from_dict = Unity.from_dict(unity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


