# smooch.ConversationApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_activity**](ConversationApi.md#conversation_activity) | **POST** /v1.1/apps/{appId}/appusers/{userId}/conversation/activity | 
[**delete_message**](ConversationApi.md#delete_message) | **DELETE** /v1.1/apps/{appId}/appusers/{userId}/messages/{messageId} | 
[**delete_messages**](ConversationApi.md#delete_messages) | **DELETE** /v1.1/apps/{appId}/appusers/{userId}/messages | 
[**get_messages**](ConversationApi.md#get_messages) | **GET** /v1.1/apps/{appId}/appusers/{userId}/messages | 
[**post_message**](ConversationApi.md#post_message) | **POST** /v1.1/apps/{appId}/appusers/{userId}/messages | 
[**reset_unread_count**](ConversationApi.md#reset_unread_count) | **POST** /v1.1/apps/{appId}/appusers/{userId}/conversation/read | 


# **conversation_activity**
> ActivityResponse conversation_activity(app_id, user_id, conversation_activity_body)



Notify Smooch when an app maker starts or stops typing a response.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
conversation_activity_body = smooch.ConversationActivity() # ConversationActivity | Body for a triggerConversationActivity request.

try:
    api_response = api_instance.conversation_activity(app_id, user_id, conversation_activity_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->conversation_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **conversation_activity_body** | [**ConversationActivity**](ConversationActivity.md)| Body for a triggerConversationActivity request. | 

### Return type

[**ActivityResponse**](ActivityResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> delete_message(app_id, user_id, message_id)



Deletes a single message.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
message_id = 'message_id_example' # str | Identifies the message.

try:
    api_instance.delete_message(app_id, user_id, message_id)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **message_id** | **str**| Identifies the message. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_messages**
> delete_messages(app_id, user_id)



Clears the message history for a user, permanently deleting all messages, but leaving any connections to Messaging Channels and Business Systems intact. These connections allow for the conversation to continue in the future, while still being associated to the same appUser. 

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_instance.delete_messages(app_id, user_id)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> GetMessagesResponse get_messages(app_id, user_id, before=before, after=after)



Get the specified app user's messages.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
before = 'before_example' # str | Timestamp of message. The API will return 100 messages before the specified timestamp (excluding any messages with the provided timestamp). (optional)
after = 'after_example' # str | Timestamp of message. The API will return 100 messages after the specified timestamp (excluding any messages with the provided timestamp). (optional)

try:
    api_response = api_instance.get_messages(app_id, user_id, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **before** | **str**| Timestamp of message. The API will return 100 messages before the specified timestamp (excluding any messages with the provided timestamp). | [optional] 
 **after** | **str**| Timestamp of message. The API will return 100 messages after the specified timestamp (excluding any messages with the provided timestamp). | [optional] 

### Return type

[**GetMessagesResponse**](GetMessagesResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_message**
> MessageResponse post_message(app_id, user_id, message_post_body)



Post a message to or from the app user.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
message_post_body = smooch.MessagePost() # MessagePost | Body for a postMessage request. Additional arguments are necessary based on message type ([text](https://docs.smooch.io/rest#text-message), [image](https://docs.smooch.io/rest#image-message), [carousel](https://docs.smooch.io/rest#carousel-message), [list](https://docs.smooch.io/rest#list-message)) 

try:
    api_response = api_instance.post_message(app_id, user_id, message_post_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->post_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **message_post_body** | [**MessagePost**](MessagePost.md)| Body for a postMessage request. Additional arguments are necessary based on message type ([text](https://docs.smooch.io/rest#text-message), [image](https://docs.smooch.io/rest#image-message), [carousel](https://docs.smooch.io/rest#carousel-message), [list](https://docs.smooch.io/rest#list-message))  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_unread_count**
> reset_unread_count(app_id, user_id)



Reset the unread count of the conversation to 0.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_instance.reset_unread_count(app_id, user_id)
except ApiException as e:
    print("Exception when calling ConversationApi->reset_unread_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

