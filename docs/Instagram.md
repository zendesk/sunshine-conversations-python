# Instagram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | Instagram Direct setup steps:   - Take note of your Facebook app ID and secret (apps can be created at [developer.facebook.com](https://developer.facebook.com));   - The Facebook app must have been submitted to Meta for app review with the \&quot;pages_manage_metadata\&quot; (to retrieve Page Access Tokens for the Pages and apps that the app user administers and to set a webhook), \&quot;instagram_basic\&quot;, and \&quot;instagram_manage_messages\&quot; (to retrieve basic Instagram account information and send messages) permissions.   - In order to integrate an Instagram Direct app, you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.  | [optional] [default to 'instagram']
**page_access_token** | **str** | The Facebook Page Access Token of the Facebook page that is linked to your Instagram account. | 
**app_id** | **str** | Your Facebook App ID. | 
**app_secret** | **str** | Your Facebook App secret. | 
**business_name** | **str** | Your Instagram Business account name | [optional] [readonly] 
**business_username** | **str** | Your Instagram Business unique username | [optional] [readonly] 
**page_id** | **str** | The ID of the Facebook Page linked to your Instagram Business account | [optional] [readonly] 
**business_id** | **str** | The ID of the Instagram Business account | [optional] [readonly] 
**username** | **str** | The Facebook user&#39;s username. This is returned when integrating through the Dashboard | [optional] [readonly] 
**user_id** | **str** | The Facebook user&#39;s user ID. This is returned when integrating through the Dashboard | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.instagram import Instagram

# TODO update the JSON string below
json = "{}"
# create an instance of Instagram from a JSON string
instagram_instance = Instagram.from_json(json)
# print the JSON string representation of the object
print(Instagram.to_json())

# convert the object into a dict
instagram_dict = instagram_instance.to_dict()
# create an instance of Instagram from a dict
instagram_from_dict = Instagram.from_dict(instagram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


