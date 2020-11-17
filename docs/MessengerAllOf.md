# MessengerAllOf

Facebook Messenger Setup steps: Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); The Facebook app must have been submitted to Facebook for app review with the “manage_pages” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of integration. | [optional] [default to 'messenger']
**page_access_token** | **str** | A Facebook Page Access Token. | 
**app_id** | **str** | A Facebook App ID. | 
**app_secret** | **str** | A Facebook App Secret. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


