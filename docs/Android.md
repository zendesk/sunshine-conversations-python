# Android


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | &lt;aside class&#x3D;\&quot;notice\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Firebase Cloud Messaging has deprecated its legacy APIs for HTTP and XMPP. Legacy credentials &lt;code&gt;serverKey&lt;/code&gt; and &lt;code&gt;senderId&lt;/code&gt; will stop working as of June 2024 and must be replaced with OAuth 2.0 access token based credentials.&lt;/aside&gt;  To configure an android integration, first visit the [Firebase Console](https://console.firebase.google.com/).  Generate a private key from the Service accounts tab in the settings.  Copy the &#x60;project_id&#x60;, &#x60;client_email&#x60; and &#x60;private_key&#x60; from the generated JSON file and call the create integrations endpoint with this data.  | [optional] [default to 'android']
**project_id** | **str** | Your project ID from your generated private key file. | [optional] 
**client_email** | **str** | Your client email from your generated private key file. | [optional] 
**private_key** | **str** | Your private key from your generated private key file. | [optional] 
**server_key** | **str** | Your server key from the fcm console. | [optional] 
**sender_id** | **str** | Your sender id from the fcm console. | [optional] 
**can_user_see_conversation_list** | **bool** | Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where &#x60;settings.multiConvoEnabled&#x60; is set to &#x60;true&#x60;*.  | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the android integration. | [optional] 
**attachments_enabled** | **bool** | Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.  | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.android import Android

# TODO update the JSON string below
json = "{}"
# create an instance of Android from a JSON string
android_instance = Android.from_json(json)
# print the JSON string representation of the object
print(Android.to_json())

# convert the object into a dict
android_dict = android_instance.to_dict()
# create an instance of Android from a dict
android_from_dict = Android.from_dict(android_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


