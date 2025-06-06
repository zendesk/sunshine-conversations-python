# sunshine_conversations_client.ConversationsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conversation**](ConversationsApi.md#create_conversation) | **POST** /v2/apps/{appId}/conversations | Create Conversation
[**delete_conversation**](ConversationsApi.md#delete_conversation) | **DELETE** /v2/apps/{appId}/conversations/{conversationId} | Delete Conversation
[**download_message_ref**](ConversationsApi.md#download_message_ref) | **POST** /v2/apps/{appId}/conversations/{conversationId}/download | Download Message Ref
[**get_conversation**](ConversationsApi.md#get_conversation) | **GET** /v2/apps/{appId}/conversations/{conversationId} | Get Conversation
[**list_conversations**](ConversationsApi.md#list_conversations) | **GET** /v2/apps/{appId}/conversations | List Conversations
[**update_conversation**](ConversationsApi.md#update_conversation) | **PATCH** /v2/apps/{appId}/conversations/{conversationId} | Update Conversation


## create_conversation
> ConversationResponse create_conversation(app_id, conversation_create_body)

Create Conversation

Create a conversation for the specified user(s).

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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_create_body = sunshine_conversations_client.ConversationCreateBody() # ConversationCreateBody | 

    try:
        # Create Conversation
        api_response = api_instance.create_conversation(app_id, conversation_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->create_conversation: %s\n" % e)
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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_create_body = sunshine_conversations_client.ConversationCreateBody() # ConversationCreateBody | 

    try:
        # Create Conversation
        api_response = api_instance.create_conversation(app_id, conversation_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->create_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_create_body** | [**ConversationCreateBody**](ConversationCreateBody.md)|  | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## delete_conversation
> object delete_conversation(app_id, conversation_id)

Delete Conversation

Delete an entire conversation record, along with its messages and attachments. Note that the default conversation cannot be deleted, but the messages contained [can be](#deleteAllMessages).

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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.

    try:
        # Delete Conversation
        api_response = api_instance.delete_conversation(app_id, conversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->delete_conversation: %s\n" % e)
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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.

    try:
        # Delete Conversation
        api_response = api_instance.delete_conversation(app_id, conversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->delete_conversation: %s\n" % e)
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
**400** | Bad request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## download_message_ref
> dict(str, object) download_message_ref(app_id, conversation_id, download_message_ref_body)

Download Message Ref

When a third party channel provides a reference of a data, this API can be used to download the reference and fetch the full data. Currently, only apple channel is supported.

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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    download_message_ref_body = {"userId":"6e416caac6a5e9544e3fb6d7","apple":{"interactiveDataRef":{"url":"https://p61-content.icloud.com/M58C0A1A2EB62B6E899B4F28996E8DA229E1914295299C39944B2F2CA7482AE50.C01USN00","bid":"com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension","key":"00c0d1827fdc858fe7b42421de1fb289c2ee0a9463d787ce4f118506f970bd6e38","signature":"81a619c81da5a01c6139219a5d20e17430c631e1eb","owner":"M58C0A2A1EB62B4E859B4F28996E8DA229E1914295299C39944B2F2CA7482AE50.C01USN00"}}} # DownloadMessageRefBody | 

    try:
        # Download Message Ref
        api_response = api_instance.download_message_ref(app_id, conversation_id, download_message_ref_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->download_message_ref: %s\n" % e)
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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    download_message_ref_body = {"userId":"6e416caac6a5e9544e3fb6d7","apple":{"interactiveDataRef":{"url":"https://p61-content.icloud.com/M58C0A1A2EB62B6E899B4F28996E8DA229E1914295299C39944B2F2CA7482AE50.C01USN00","bid":"com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension","key":"00c0d1827fdc858fe7b42421de1fb289c2ee0a9463d787ce4f118506f970bd6e38","signature":"81a619c81da5a01c6139219a5d20e17430c631e1eb","owner":"M58C0A2A1EB62B4E859B4F28996E8DA229E1914295299C39944B2F2CA7482AE50.C01USN00"}}} # DownloadMessageRefBody | 

    try:
        # Download Message Ref
        api_response = api_instance.download_message_ref(app_id, conversation_id, download_message_ref_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->download_message_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 
 **download_message_ref_body** | [**DownloadMessageRefBody**](DownloadMessageRefBody.md)|  | 

### Return type

**dict(str, object)**

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

## get_conversation
> ConversationResponse get_conversation(app_id, conversation_id)

Get Conversation

Fetches an individual conversation.

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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.

    try:
        # Get Conversation
        api_response = api_instance.get_conversation(app_id, conversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.

    try:
        # Get Conversation
        api_response = api_instance.get_conversation(app_id, conversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

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

## list_conversations
> ConversationListResponse list_conversations(app_id, filter, page=page)

List Conversations

Lists all conversations that a user is part of. This API is paginated through [cursor pagination](#section/Introduction/API-pagination-and-records-limits). ```shell /v2/apps/:appId/conversations?filter[userId]=42589ad070d43be9b00ff7e5 ``` 

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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    filter = sunshine_conversations_client.ConversationListFilter() # ConversationListFilter | Contains parameters for filtering the results.
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)

    try:
        # List Conversations
        api_response = api_instance.list_conversations(app_id, filter, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->list_conversations: %s\n" % e)
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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    filter = sunshine_conversations_client.ConversationListFilter() # ConversationListFilter | Contains parameters for filtering the results.
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)

    try:
        # List Conversations
        api_response = api_instance.list_conversations(app_id, filter, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->list_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **filter** | [**ConversationListFilter**](.md)| Contains parameters for filtering the results. | 
 **page** | [**Page**](.md)| Contains parameters for applying cursor pagination. | [optional] 

### Return type

[**ConversationListResponse**](ConversationListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## update_conversation
> ConversationResponse update_conversation(app_id, conversation_id, conversation_update_body)

Update Conversation

Updates a conversation record.

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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    conversation_update_body = sunshine_conversations_client.ConversationUpdateBody() # ConversationUpdateBody | 

    try:
        # Update Conversation
        api_response = api_instance.update_conversation(app_id, conversation_id, conversation_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->update_conversation: %s\n" % e)
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
    api_instance = sunshine_conversations_client.ConversationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    conversation_update_body = sunshine_conversations_client.ConversationUpdateBody() # ConversationUpdateBody | 

    try:
        # Update Conversation
        api_response = api_instance.update_conversation(app_id, conversation_id, conversation_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConversationsApi->update_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **conversation_id** | **str**| Identifies the conversation. | 
 **conversation_update_body** | [**ConversationUpdateBody**](ConversationUpdateBody.md)|  | 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

