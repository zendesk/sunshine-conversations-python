# Ios


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | To configure an ios integration, call the create integration endpoint with a base64 encoded Apple Push Notification certificate from the [Apple Developer Portal](https://developer.apple.com/).  | [optional] [default to 'ios']
**certificate** | **str** | The binary of your APN certificate base64 encoded. To base64 encode your certificate you can use this command in the terminal: &#x60;openssl base64 -in YOUR_CERTIFICATE.p12 | tr -d &#39;\\n&#39;&#x60;  | [optional] 
**password** | **str** | The password for your APN certificate. | [optional] 
**production** | **bool** | The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified. | [optional] 
**auto_update_badge** | **bool** | Use the unread count of the conversation as the application badge. | [optional] 
**can_user_see_conversation_list** | **bool** | Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where &#x60;settings.multiConvoEnabled&#x60; is set to &#x60;true&#x60;*.  | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the iOS integration. | [optional] 
**attachments_enabled** | **bool** | Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.  | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.ios import Ios

# TODO update the JSON string below
json = "{}"
# create an instance of Ios from a JSON string
ios_instance = Ios.from_json(json)
# print the JSON string representation of the object
print(Ios.to_json())

# convert the object into a dict
ios_dict = ios_instance.to_dict()
# create an instance of Ios from a dict
ios_from_dict = Ios.from_dict(ios_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


