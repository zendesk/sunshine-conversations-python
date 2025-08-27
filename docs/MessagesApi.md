# sunshine_conversations_client.MessagesApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_messages**](MessagesApi.md#delete_all_messages) | **DELETE** /v2/apps/{appId}/conversations/{conversationId}/messages | Delete All Messages
[**delete_message**](MessagesApi.md#delete_message) | **DELETE** /v2/apps/{appId}/conversations/{conversationId}/messages/{messageId} | Delete Message
[**list_messages**](MessagesApi.md#list_messages) | **GET** /v2/apps/{appId}/conversations/{conversationId}/messages | List Messages
[**post_message**](MessagesApi.md#post_message) | **POST** /v2/apps/{appId}/conversations/{conversationId}/messages | Post Message


## delete_all_messages
> object delete_all_messages(app_idconversation_id)

Delete All Messages

Delete all messages of a particular conversation.

### Example

Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.

    try:
        # Delete All Messages
        api_response = api_instance.delete_all_messages(app_idconversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->delete_all_messages: %s\n" % e)
```

Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.

    try:
        # Delete All Messages
        api_response = api_instance.delete_all_messages(app_idconversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->delete_all_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## delete_message
> object delete_message(app_idconversation_idmessage_id)

Delete Message

Delete a single message of a particular conversation.

### Example

Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    message_id = '029c31f25a21b47effd7be90' # str | The id of the message.

    try:
        # Delete Message
        api_response = api_instance.delete_message(app_idconversation_idmessage_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->delete_message: %s\n" % e)
```

Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    message_id = '029c31f25a21b47effd7be90' # str | The id of the message.

    try:
        # Delete Message
        api_response = api_instance.delete_message(app_idconversation_idmessage_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 
 **message_id** | **str**| The id of the message. | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## list_messages
> MessageListResponse list_messages(app_idconversation_idpage=page)

List Messages

List all messages for a particular conversation. This API is paginated through [cursor pagination](#section/Introduction/API-Pagination-and-Records-Limits), in the _backwards_ direction, with the most recent (i.e. last) page of messages being returned by default. The `hasMore` flag indicates whether more messages exist in the direction you are currently paginating through. To page backwards in the history, use the `beforeCursor` or follow the `prev` link. The page size limit is fixed at 100 messages per page.  ```shell /v2/apps/:appId/conversations/:conversationId/messages?page[before]=5f32b88acf6bf25073b2be56 ``` 

### Example

Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)

    try:
        # List Messages
        api_response = api_instance.list_messages(app_idconversation_idpage=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```

Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)

    try:
        # List Messages
        api_response = api_instance.list_messages(app_idconversation_idpage=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 
 **page** | [**Page**](.md)| Contains parameters for applying cursor pagination. | [optional] 

### Return type

[**MessageListResponse**](MessageListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## post_message
> MessagePostResponse post_message(app_idconversation_idmessage_post)

Post Message

Send a message in a particular conversation.

### Example

Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    message_post = sunshine_conversations_client.MessagePost() # MessagePost | 

    try:
        # Post Message
        api_response = api_instance.post_message(app_idconversation_idmessage_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->post_message: %s\n" % e)
```

Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import sunshine_conversations_client
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.MessagesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    message_post = sunshine_conversations_client.MessagePost() # MessagePost | 

    try:
        # Post Message
        api_response = api_instance.post_message(app_idconversation_idmessage_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessagesApi->post_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 
 **message_post** | [**MessagePost**](MessagePost.md)|  | 

### Return type

[**MessagePostResponse**](MessagePostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**423** | Message limit reached &lt;aside class&#x3D;\&quot;notice\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; To learn more about the conversation message limit, consult the section in the introduction linked &lt;a href&#x3D;\&quot;#section/Introduction/Conversation-Size-Limits\&quot;&gt;here&lt;/a&gt;.&lt;/aside&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

