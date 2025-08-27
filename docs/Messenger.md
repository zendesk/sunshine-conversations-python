# Messenger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | Facebook Messenger Setup steps: - Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); - The Facebook app must have been submitted to Meta for app review with the “pages_manage_metadata” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. - In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.  | [optional] [default to 'messenger']
**page_access_token** | **str** | A Facebook Page Access Token. | 
**app_id** | **str** | A Facebook App ID. | 
**app_secret** | **str** | A Facebook App Secret. | 
**page_id** | **float** | A Facebook page ID. | [optional] 
**page_name** | **str** | A Facebook page name. | [optional] 

## Example

```python
from sunshine_conversations_client.model.messenger import Messenger

# TODO update the JSON string below
json = "{}"
# create an instance of Messenger from a JSON string
messenger_instance = Messenger.from_json(json)
# print the JSON string representation of the object
print(Messenger.to_json())

# convert the object into a dict
messenger_dict = messenger_instance.to_dict()
# create an instance of Messenger from a dict
messenger_from_dict = Messenger.from_dict(messenger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


