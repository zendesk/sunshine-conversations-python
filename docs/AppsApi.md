# sunshine_conversations_client.AppsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppsApi.md#create_app) | **POST** /v2/apps | Create App
[**delete_app**](AppsApi.md#delete_app) | **DELETE** /v2/apps/{appId} | Delete App
[**get_app**](AppsApi.md#get_app) | **GET** /v2/apps/{appId} | Get App
[**list_apps**](AppsApi.md#list_apps) | **GET** /v2/apps | List Apps
[**update_app**](AppsApi.md#update_app) | **PATCH** /v2/apps/{appId} | Update App


## create_app
> AppResponse create_app(app_create_body)

Create App

Creates a new app. When using [service account](#service-accounts) credentials, the service account is automatically granted access to the app.

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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_create_body = sunshine_conversations_client.AppCreateBody() # AppCreateBody | 

    try:
        # Create App
        api_response = api_instance.create_app(app_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->create_app: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_create_body = sunshine_conversations_client.AppCreateBody() # AppCreateBody | 

    try:
        # Create App
        api_response = api_instance.create_app(app_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_create_body** | [**AppCreateBody**](AppCreateBody.md)|  | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**402** | Payment required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## delete_app
> object delete_app(app_id)

Delete App

Removes the specified app, including all its enabled integrations.

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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.

    try:
        # Delete App
        api_response = api_instance.delete_app(app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->delete_app: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.

    try:
        # Delete App
        api_response = api_instance.delete_app(app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

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

## get_app
> AppResponse get_app(app_id)

Get App

Fetches an individual app.

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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.

    try:
        # Get App
        api_response = api_instance.get_app(app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.

    try:
        # Get App
        api_response = api_instance.get_app(app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**AppResponse**](AppResponse.md)

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

## list_apps
> AppListResponse list_apps(page=pagefilter=filter)

List Apps

Lists all apps that a user is part of. This API is paginated through [cursor pagination](#section/Introduction/API-Pagination-and-Records-Limits).  ```shell /v2/apps?page[after]=5e1606762556d93e9c176f69&page[size]=10 ``` 

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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)
    filter = sunshine_conversations_client.AppListFilter() # AppListFilter | Contains parameters for filtering the results. (optional)

    try:
        # List Apps
        api_response = api_instance.list_apps(page=pagefilter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    page = sunshine_conversations_client.Page() # Page | Contains parameters for applying cursor pagination. (optional)
    filter = sunshine_conversations_client.AppListFilter() # AppListFilter | Contains parameters for filtering the results. (optional)

    try:
        # List Apps
        api_response = api_instance.list_apps(page=pagefilter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**Page**](.md)| Contains parameters for applying cursor pagination. | [optional] 
 **filter** | [**AppListFilter**](.md)| Contains parameters for filtering the results. | [optional] 

### Return type

[**AppListResponse**](AppListResponse.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## update_app
> AppResponse update_app(app_idapp_update_body)

Update App

Updates an app.

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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    app_update_body = sunshine_conversations_client.AppUpdateBody() # AppUpdateBody | 

    try:
        # Update App
        api_response = api_instance.update_app(app_idapp_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AppsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    app_update_body = sunshine_conversations_client.AppUpdateBody() # AppUpdateBody | 

    try:
        # Update App
        api_response = api_instance.update_app(app_idapp_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **app_update_body** | [**AppUpdateBody**](AppUpdateBody.md)|  | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

