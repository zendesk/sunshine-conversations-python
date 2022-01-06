# sunshine_conversations_client.CustomIntegrationApiKeysApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_integration_key**](CustomIntegrationApiKeysApi.md#create_custom_integration_key) | **POST** /v2/apps/{appId}/integrations/{integrationId}/keys | Create Integration Key
[**delete_custom_integration_key**](CustomIntegrationApiKeysApi.md#delete_custom_integration_key) | **DELETE** /v2/apps/{appId}/integrations/{integrationId}/keys/{keyId} | Delete Integration Key
[**get_custom_integration_key**](CustomIntegrationApiKeysApi.md#get_custom_integration_key) | **GET** /v2/apps/{appId}/integrations/{integrationId}/keys/{keyId} | Get Integration Key
[**list_custom_integration_keys**](CustomIntegrationApiKeysApi.md#list_custom_integration_keys) | **GET** /v2/apps/{appId}/integrations/{integrationId}/keys | List Integration Keys


## create_custom_integration_key
> IntegrationApiKeyResponse create_custom_integration_key(app_id, integration_id, integration_api_key)

Create Integration Key

Creates an API key for the specified custom integration. The response body will include a secret as well it’s corresponding id, which you can use to generate JSON Web Tokens to securely make API calls on behalf of the integration.

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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    integration_api_key = sunshine_conversations_client.IntegrationApiKey() # IntegrationApiKey | 

    try:
        # Create Integration Key
        api_response = api_instance.create_custom_integration_key(app_id, integration_id, integration_api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->create_custom_integration_key: %s\n" % e)
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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    integration_api_key = sunshine_conversations_client.IntegrationApiKey() # IntegrationApiKey | 

    try:
        # Create Integration Key
        api_response = api_instance.create_custom_integration_key(app_id, integration_id, integration_api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->create_custom_integration_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **integration_api_key** | [**IntegrationApiKey**](IntegrationApiKey.md)|  | 

### Return type

[**IntegrationApiKeyResponse**](IntegrationApiKeyResponse.md)

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

## delete_custom_integration_key
> object delete_custom_integration_key(app_id, integration_id, key_id)

Delete Integration Key

Removes an API key.

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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    key_id = 'int_5d8cff3cd55b040010928b5b' # str | The id of the key.

    try:
        # Delete Integration Key
        api_response = api_instance.delete_custom_integration_key(app_id, integration_id, key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->delete_custom_integration_key: %s\n" % e)
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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    key_id = 'int_5d8cff3cd55b040010928b5b' # str | The id of the key.

    try:
        # Delete Integration Key
        api_response = api_instance.delete_custom_integration_key(app_id, integration_id, key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->delete_custom_integration_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **key_id** | **str**| The id of the key. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## get_custom_integration_key
> IntegrationApiKeyResponse get_custom_integration_key(app_id, integration_id, key_id)

Get Integration Key

Get the specified API key.

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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    key_id = 'int_5d8cff3cd55b040010928b5b' # str | The id of the key.

    try:
        # Get Integration Key
        api_response = api_instance.get_custom_integration_key(app_id, integration_id, key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->get_custom_integration_key: %s\n" % e)
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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    key_id = 'int_5d8cff3cd55b040010928b5b' # str | The id of the key.

    try:
        # Get Integration Key
        api_response = api_instance.get_custom_integration_key(app_id, integration_id, key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->get_custom_integration_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **key_id** | **str**| The id of the key. | 

### Return type

[**IntegrationApiKeyResponse**](IntegrationApiKeyResponse.md)

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

## list_custom_integration_keys
> IntegrationApiKeyListResponse list_custom_integration_keys(app_id, integration_id)

List Integration Keys

Lists all API keys for a given integration.

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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.

    try:
        # List Integration Keys
        api_response = api_instance.list_custom_integration_keys(app_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->list_custom_integration_keys: %s\n" % e)
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
    api_instance = sunshine_conversations_client.CustomIntegrationApiKeysApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.

    try:
        # List Integration Keys
        api_response = api_instance.list_custom_integration_keys(app_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomIntegrationApiKeysApi->list_custom_integration_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 

### Return type

[**IntegrationApiKeyListResponse**](IntegrationApiKeyListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | API keys are available only for custom integrations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

