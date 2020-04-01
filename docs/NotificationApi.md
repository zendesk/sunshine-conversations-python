# smooch.NotificationApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_notification**](NotificationApi.md#post_notification) | **POST** /v1/apps/{appId}/notifications | 


# **post_notification**
> NotificationResponse post_notification(app_id, notification_post_body)



Post a notification to an externalId.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.NotificationApi()
app_id = 'app_id_example' # str | Identifies the app.
notification_post_body = smooch.NotificationPost() # NotificationPost | Body for a postNotification request. 

try:
    api_response = api_instance.post_notification(app_id, notification_post_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->post_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **notification_post_body** | [**NotificationPost**](NotificationPost.md)| Body for a postNotification request.  | 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

