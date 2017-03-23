# smooch.ConversationApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_messages**](ConversationApi.md#delete_messages) | **DELETE** /appusers/{userId}/messages | 
[**get_messages**](ConversationApi.md#get_messages) | **GET** /appusers/{userId}/messages | 
[**post_message**](ConversationApi.md#post_message) | **POST** /appusers/{userId}/messages | 
[**reset_unread_count**](ConversationApi.md#reset_unread_count) | **POST** /appusers/{userId}/conversation/read | 
[**trigger_typing_activity**](ConversationApi.md#trigger_typing_activity) | **POST** /appusers/{userId}/conversation/activity | 


# **delete_messages**
> delete_messages(user_id)



Clears the message history for a user, permanently deleting all messages, but leaving any connections to Messaging Channels and Business Systems intact. These connections allow for the conversation to continue in the future, while still being associated to the same appUser. 

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_instance.delete_messages(user_id)
except ApiException as e:
    print("Exception when calling ConversationApi->delete_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> GetMessagesResponse get_messages(user_id, before=before, after=after)



Get the specified app user's messages.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
before = 'before_example' # str | Timestamp of message. The API will return 100 messages before the specified timestamp (excluding any messages with the provided timestamp). (optional)
after = 'after_example' # str | Timestamp of message. The API will return 100 messages after the specified timestamp (excluding any messages with the provided timestamp). (optional)

try:
    api_response = api_instance.get_messages(user_id, before=before, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> PostMessagesResponse post_message(user_id, message_post_body)



Post a message to or from the app user.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
message_post_body = smooch.MessagePost() # MessagePost | Body for a postMessage request. Additional arguments are necessary based on message type ([text](https://docs.smooch.io/rest#text-message), [image](https://docs.smooch.io/rest#image-message), [carousel](https://docs.smooch.io/rest#carousel-message), [list](https://docs.smooch.io/rest#list-message)) 

try:
    api_response = api_instance.post_message(user_id, message_post_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationApi->post_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **message_post_body** | [**MessagePost**](MessagePost.md)| Body for a postMessage request. Additional arguments are necessary based on message type ([text](https://docs.smooch.io/rest#text-message), [image](https://docs.smooch.io/rest#image-message), [carousel](https://docs.smooch.io/rest#carousel-message), [list](https://docs.smooch.io/rest#list-message))  | 

### Return type

[**PostMessagesResponse**](PostMessagesResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_unread_count**
> reset_unread_count(user_id)



Reset the unread count of the conversation to 0.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_instance.reset_unread_count(user_id)
except ApiException as e:
    print("Exception when calling ConversationApi->reset_unread_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_typing_activity**
> trigger_typing_activity(user_id, typing_activity_trigger_body)



Notify Smooch when an app maker starts or stops typing a response.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ConversationApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
typing_activity_trigger_body = smooch.TypingActivityTrigger() # TypingActivityTrigger | Body for a triggerTypingActivity request.

try:
    api_instance.trigger_typing_activity(user_id, typing_activity_trigger_body)
except ApiException as e:
    print("Exception when calling ConversationApi->trigger_typing_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **typing_activity_trigger_body** | [**TypingActivityTrigger**](TypingActivityTrigger.md)| Body for a triggerTypingActivity request. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

