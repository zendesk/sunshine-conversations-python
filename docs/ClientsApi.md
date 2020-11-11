# sunshine_conversations_client.ClientsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientsApi.md#create_client) | **POST** /v2/apps/{appId}/users/{userIdOrExternalId}/clients | Create Client
[**list_clients**](ClientsApi.md#list_clients) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/clients | List Clients
[**remove_client**](ClientsApi.md#remove_client) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId}/clients/{clientId} | Remove Client


## create_client
> ClientResponse create_client(app_id, user_id_or_external_id, client_create)

Create Client

Create a client and link it to a channel specified by the matchCriteria.type.

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
configuration = sunshine_conversations_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Uncomment this if you want to use JWTs
# Configure Bearer authorization (JWT): bearerAuth
# configuration = sunshine_conversations_client.Configuration(
#    access_token = 'YOUR_BEARER_TOKEN'
#)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ClientsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    client_create = {"matchCriteria":{"type":"mailgun","integrationId":"582dedf230e788746891281a","primary":true,"address":"steveb@channel5.com","subject":"New message from {appName}"},"confirmation":{"type":"immediate","message":{"author":{"type":"business","displayName":"Steve","avatarUrl":"https://www.gravatar.com/image.jpg"},"content":{"type":"text","text":"Hello!"},"metadata":{"lang":"en-ca"}}},"target":{"conversationId":"029c31f25a21b47effd7be90"}} # ClientCreate | 

    try:
        # Create Client
        api_response = api_instance.create_client(app_id, user_id_or_external_id, client_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->create_client: %s\n" % e)
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
configuration = sunshine_conversations_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Uncomment this if you want to use JWTs
# Configure Bearer authorization (JWT): bearerAuth
# configuration = sunshine_conversations_client.Configuration(
#    access_token = 'YOUR_BEARER_TOKEN'
#)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ClientsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    client_create = {"matchCriteria":{"type":"mailgun","integrationId":"582dedf230e788746891281a","primary":true,"address":"steveb@channel5.com","subject":"New message from {appName}"},"confirmation":{"type":"immediate","message":{"author":{"type":"business","displayName":"Steve","avatarUrl":"https://www.gravatar.com/image.jpg"},"content":{"type":"text","text":"Hello!"},"metadata":{"lang":"en-ca"}}},"target":{"conversationId":"029c31f25a21b47effd7be90"}} # ClientCreate | 

    try:
        # Create Client
        api_response = api_instance.create_client(app_id, user_id_or_external_id, client_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 
 **client_create** | [**ClientCreate**](ClientCreate.md)|  | 

### Return type

[**ClientResponse**](ClientResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## list_clients
> ClientListResponse list_clients(app_id, user_id_or_external_id, page=page)

List Clients

Get all the clients for a particular user, including both linked clients and pending clients. This API is paginated through [cursor pagination](#section/Introduction/API-pagination-and-records-limits).  ```shell /v2/apps/:appId/users/:userId/clients?page[after]=5ebee0975ac5304b664a12fa ``` 

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
configuration = sunshine_conversations_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Uncomment this if you want to use JWTs
# Configure Bearer authorization (JWT): bearerAuth
# configuration = sunshine_conversations_client.Configuration(
#    access_token = 'YOUR_BEARER_TOKEN'
#)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ClientsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)

    try:
        # List Clients
        api_response = api_instance.list_clients(app_id, user_id_or_external_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)
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
configuration = sunshine_conversations_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Uncomment this if you want to use JWTs
# Configure Bearer authorization (JWT): bearerAuth
# configuration = sunshine_conversations_client.Configuration(
#    access_token = 'YOUR_BEARER_TOKEN'
#)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ClientsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)

    try:
        # List Clients
        api_response = api_instance.list_clients(app_id, user_id_or_external_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 
 **page** | [**Page**](.md)| Contains parameters for applying cursor pagination. | [optional] 

### Return type

[**ClientListResponse**](ClientListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## remove_client
> object remove_client(app_id, user_id_or_external_id, client_id)

Remove Client

Remove a particular client and unsubscribe it from all connected conversations.

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
configuration = sunshine_conversations_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Uncomment this if you want to use JWTs
# Configure Bearer authorization (JWT): bearerAuth
# configuration = sunshine_conversations_client.Configuration(
#    access_token = 'YOUR_BEARER_TOKEN'
#)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ClientsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    client_id = '5d8cff3cd55b040010928b5b' # str | The client's id.

    try:
        # Remove Client
        api_response = api_instance.remove_client(app_id, user_id_or_external_id, client_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->remove_client: %s\n" % e)
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
configuration = sunshine_conversations_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Uncomment this if you want to use JWTs
# Configure Bearer authorization (JWT): bearerAuth
# configuration = sunshine_conversations_client.Configuration(
#    access_token = 'YOUR_BEARER_TOKEN'
#)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ClientsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    client_id = '5d8cff3cd55b040010928b5b' # str | The client's id.

    try:
        # Remove Client
        api_response = api_instance.remove_client(app_id, user_id_or_external_id, client_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientsApi->remove_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 
 **client_id** | **str**| The client&#39;s id. | 

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
**400** | Cannot remove a client of type &#39;sdk&#39; |  -  |
**404** | Client not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

