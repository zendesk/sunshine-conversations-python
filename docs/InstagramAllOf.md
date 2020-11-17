# InstagramAllOf

Instagram Direct setup steps: Take note of your Facebook app ID and secret (apps can be created at [developer.facebook.com](https://developer.facebook.com)); The Facebook app must have been submitted to Facebook for app review with the \"manage_pages\" (to retrieve Page Access Tokens for the Pages and apps that the app user administers and to set a webhook), \"instagram_basic\", and \"instagram_manage_messages\" (to retrieve basic Instagram account information and send messages) permissions. In order to integrate an Instagram Direct app, you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of integration. | [optional] [default to 'instagram']
**page_access_token** | **str** | The Facebook Page Access Token of the Facebook page that is linked to your Instagram account. | 
**app_id** | **str** | Your Facebook App ID. | 
**app_secret** | **str** | Your Facebook App secret. | 
**business_name** | **str** | Your Instagram Business account name | [optional] [readonly] 
**business_username** | **str** | Your Instagram Business unique username | [optional] [readonly] 
**page_id** | **str** | The ID of the Facebook Page linked to your Instagram Business account | [optional] [readonly] 
**business_id** | **str** | The ID of the Instagram Business account | [optional] [readonly] 
**username** | **str** | The Facebook user&#39;s username. This is returned when integrating through the Dashboard | [optional] [readonly] 
**user_id** | **str** | The Facebook user&#39;s user ID. This is returned when integrating through the Dashboard | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


