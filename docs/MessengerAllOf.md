# MessengerAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Facebook Messenger Setup steps: - Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); - The Facebook app must have been submitted to Meta for app review with the “pages_manage_metadata” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. - In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.  | [optional] [default to 'messenger']
**page_access_token** | **str** | A Facebook Page Access Token. | 
**app_id** | **str** | A Facebook App ID. | 
**app_secret** | **str** | A Facebook App Secret. | 
**page_id** | **float** | A Facebook page ID. | [optional] 
**page_name** | **str** | A Facebook page name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


