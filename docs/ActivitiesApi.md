# sunshine_conversations_client.ActivitiesApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_activity**](ActivitiesApi.md#post_activity) | **POST** /v2/apps/{appId}/conversations/{conversationId}/activity | Post Activity


# **post_activity**
> object post_activity(app_id, conversation_id, activity_post)

Post Activity

Notify Sunshine Conversations of different conversation activities. Supported activity types are:
* Typing activity
* Conversation read event


### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import sunshine_conversations_client
from sunshine_conversations_client.models.activity_post import ActivityPost
from sunshine_conversations_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smooch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sunshine_conversations_client.Configuration(
    host = "https://api.smooch.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sunshine_conversations_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = sunshine_conversations_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ActivitiesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    activity_post = {"author":{"type":"user","userId":"5963c0d619a30a2e00de36b8"},"type":"conversation:read"} # ActivityPost | 

    try:
        # Post Activity
        api_response = api_instance.post_activity(app_id, conversation_id, activity_post)
        print("The response of ActivitiesApi->post_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->post_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 
 **activity_post** | [**ActivityPost**](ActivityPost.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

