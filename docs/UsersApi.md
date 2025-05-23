# sunshine_conversations_client.UsersApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v2/apps/{appId}/users | Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId} | Delete User
[**delete_user_personal_information**](UsersApi.md#delete_user_personal_information) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId}/personalinformation | Delete User Personal Information
[**get_user**](UsersApi.md#get_user) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId} | Get User
[**sync_user**](UsersApi.md#sync_user) | **POST** /v2/apps/{appId}/users/{zendeskId}/sync | Synchronize User
[**update_user**](UsersApi.md#update_user) | **PATCH** /v2/apps/{appId}/users/{userIdOrExternalId} | Update User


## create_user
> UserResponse create_user(app_id, user_create_body)

Create User

Creates a new user.

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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_create_body = sunshine_conversations_client.UserCreateBody() # UserCreateBody | 

    try:
        # Create User
        api_response = api_instance.create_user(app_id, user_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_create_body = sunshine_conversations_client.UserCreateBody() # UserCreateBody | 

    try:
        # Create User
        api_response = api_instance.create_user(app_id, user_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_create_body** | [**UserCreateBody**](UserCreateBody.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## delete_user
> object delete_user(app_id, user_id_or_external_id)

Delete User

Delete a user, its clients and its conversation history. The user is considered completely deleted once the `user:delete` webhook is fired. To only delete a user’s personal information, see [Delete User Personal Information](#operation/deleteUserPersonalInformation).

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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # Delete User
        api_response = api_instance.delete_user(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # Delete User
        api_response = api_instance.delete_user(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 

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

## delete_user_personal_information
> UserResponse delete_user_personal_information(app_id, user_id_or_external_id)

Delete User Personal Information

Delete a user’s personal information. Calling this API will clear `givenName`, `surname`, `email` and `avatarUrl` and every custom property for the specified user. For every client owned by the user, it will also clear `displayName`, `avatarUrl` and any channel specific information stored in the info and raw fields. Calling this API doesn’t delete the user’s conversation history. To fully delete the user, see [Delete User](#operation/deleteUser).

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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # Delete User Personal Information
        api_response = api_instance.delete_user_personal_information(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user_personal_information: %s\n" % e)
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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # Delete User Personal Information
        api_response = api_instance.delete_user_personal_information(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user_personal_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 

### Return type

[**UserResponse**](UserResponse.md)

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

## get_user
> UserResponse get_user(app_id, user_id_or_external_id)

Get User

Fetches an individual user.

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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # Get User
        api_response = api_instance.get_user(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # Get User
        api_response = api_instance.get_user(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 

### Return type

[**UserResponse**](UserResponse.md)

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

## sync_user
> UserResponse sync_user(app_id, zendesk_id, sync_user_body=sync_user_body)

Synchronize User

Synchronize a messaging user with its core Zendesk user counterpart. Messaging users are separate objects linked to a core Zendesk user record by `zendeskId`. It is possible for changes to be made to the core Zendesk user record in a way that causes the messaging user to fall out of sync. The core Zendesk user might have their primary email changed, for example. This endpoint can be used to update the messaging user with the `profile.givenName`, `profile.surname`, `externalId`, and primary email identity of its core Zendesk user counterpart.<br/><br/>It is also possible for two Zendesk users to be merged. In such a case, this API can be used to apply that merger on the messaging side. The surviving Zendesk user id can be specified via the `survivingZendeskId` parameter of the request body, and the outgoing `zendeskId` is specified in the request path. <aside class=\"notice\">Only the primary email identity of the core Zendesk user will be synchronized, and it will be set on the identities array, not in the profile.</aside> <br/> <aside class=\"notice\">In some circumstances, a single call to this API might produce changes on more than one messaging user. If the externalId or email being synchronized already exists on a different messaging user within the account, the conflict will be resolved by merging those messaging users together, if possible. If a conflicting messaging user is already linked to a core Zendesk user by zendeskId it cannot be merged. In this case, the conflicting externalId or email will instead be removed and reassigned to the messaging user that is being synchronized.</aside>

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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    zendesk_id = '35436' # str | The ID that links a messaging user to its core Zendesk user counterpart. This ID can be used to fetch the core user record via the Zendesk Support API. 
    sync_user_body = sunshine_conversations_client.SyncUserBody() # SyncUserBody |  (optional)

    try:
        # Synchronize User
        api_response = api_instance.sync_user(app_id, zendesk_id, sync_user_body=sync_user_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->sync_user: %s\n" % e)
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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    zendesk_id = '35436' # str | The ID that links a messaging user to its core Zendesk user counterpart. This ID can be used to fetch the core user record via the Zendesk Support API. 
    sync_user_body = sunshine_conversations_client.SyncUserBody() # SyncUserBody |  (optional)

    try:
        # Synchronize User
        api_response = api_instance.sync_user(app_id, zendesk_id, sync_user_body=sync_user_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->sync_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **zendesk_id** | **str**| The ID that links a messaging user to its core Zendesk user counterpart. This ID can be used to fetch the core user record via the Zendesk Support API.  | 
 **sync_user_body** | [**SyncUserBody**](SyncUserBody.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

## update_user
> UserResponse update_user(app_id, user_id_or_external_id, user_update_body)

Update User

Updates a user.

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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    user_update_body = sunshine_conversations_client.UserUpdateBody() # UserUpdateBody | 

    try:
        # Update User
        api_response = api_instance.update_user(app_id, user_id_or_external_id, user_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
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
    api_instance = sunshine_conversations_client.UsersApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    user_update_body = sunshine_conversations_client.UserUpdateBody() # UserUpdateBody | 

    try:
        # Update User
        api_response = api_instance.update_user(app_id, user_id_or_external_id, user_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 
 **user_update_body** | [**UserUpdateBody**](UserUpdateBody.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

