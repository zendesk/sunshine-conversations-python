# swagger_client.ConversationApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_messages**](ConversationApi.md#get_messages) | **GET** /appusers/{userId}/messages | 
[**reset_unread_count**](ConversationApi.md#reset_unread_count) | **POST** /appusers/{userId}/conversation/read | 
[**trigger_typing_activity**](ConversationApi.md#trigger_typing_activity) | **POST** /appusers/{userId}/conversation/activity | 


# **get_messages**
> GetMessagesResponse get_messages(user_id, before=before, after=after)



Get the specified app users messages.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: appToken
swagger_client.configuration.api_key['app-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['app-token'] = 'Bearer'
# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConversationApi()
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

[appToken](../README.md#appToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_unread_count**
> reset_unread_count(user_id)



Reset the unread count of the conversation to 0. If the conversation has not yet been created for the specified app user 404 will be returned.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: appToken
swagger_client.configuration.api_key['app-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['app-token'] = 'Bearer'
# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConversationApi()
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

[appToken](../README.md#appToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_typing_activity**
> trigger_typing_activity(user_id, typing_activity_trigger)



Notify Smooch when an app maker starts or stops typing a response.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: appToken
swagger_client.configuration.api_key['app-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['app-token'] = 'Bearer'
# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConversationApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
typing_activity_trigger = swagger_client.TypingActivityTrigger() # TypingActivityTrigger | Supported properties for a triggerTypingActivity request.

try: 
    api_instance.trigger_typing_activity(user_id, typing_activity_trigger)
except ApiException as e:
    print("Exception when calling ConversationApi->trigger_typing_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **typing_activity_trigger** | [**TypingActivityTrigger**](TypingActivityTrigger.md)| Supported properties for a triggerTypingActivity request. | 

### Return type

void (empty response body)

### Authorization

[appToken](../README.md#appToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

