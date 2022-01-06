# sunshine_conversations_client.WebhooksApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /v2/apps/{appId}/integrations/{integrationId}/webhooks | Create Webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId} | Delete Webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId} | Get Webhook
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /v2/apps/{appId}/integrations/{integrationId}/webhooks | List Webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId} | Update Webhook


## create_webhook
> WebhookResponse create_webhook(app_id, integration_id, webhook_create_body)

Create Webhook

Creates a new webhook associated with a Sunshine Conversations Connect integration or a custom integration.

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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_create_body = sunshine_conversations_client.WebhookCreateBody() # WebhookCreateBody | 

    try:
        # Create Webhook
        api_response = api_instance.create_webhook(app_id, integration_id, webhook_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_create_body = sunshine_conversations_client.WebhookCreateBody() # WebhookCreateBody | 

    try:
        # Create Webhook
        api_response = api_instance.create_webhook(app_id, integration_id, webhook_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **webhook_create_body** | [**WebhookCreateBody**](WebhookCreateBody.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## delete_webhook
> object delete_webhook(app_id, integration_id, webhook_id)

Delete Webhook

Deletes the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.

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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_id = '029c31f25a21b47effd7be90' # str | The id of the webhook.

    try:
        # Delete Webhook
        api_response = api_instance.delete_webhook(app_id, integration_id, webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_id = '029c31f25a21b47effd7be90' # str | The id of the webhook.

    try:
        # Delete Webhook
        api_response = api_instance.delete_webhook(app_id, integration_id, webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **webhook_id** | **str**| The id of the webhook. | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## get_webhook
> WebhookResponse get_webhook(app_id, integration_id, webhook_id)

Get Webhook

Gets the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.

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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_id = '029c31f25a21b47effd7be90' # str | The id of the webhook.

    try:
        # Get Webhook
        api_response = api_instance.get_webhook(app_id, integration_id, webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_id = '029c31f25a21b47effd7be90' # str | The id of the webhook.

    try:
        # Get Webhook
        api_response = api_instance.get_webhook(app_id, integration_id, webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **webhook_id** | **str**| The id of the webhook. | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## list_webhooks
> WebhookListResponse list_webhooks(app_id, integration_id)

List Webhooks

Lists all webhooks for a given Sunshine Conversations Connect integration or custom integration.

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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.

    try:
        # List Webhooks
        api_response = api_instance.list_webhooks(app_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.

    try:
        # List Webhooks
        api_response = api_instance.list_webhooks(app_id, integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 

### Return type

[**WebhookListResponse**](WebhookListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## update_webhook
> WebhookResponse update_webhook(app_id, integration_id, webhook_id, webhook_body)

Update Webhook

Updates the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.

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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_id = '029c31f25a21b47effd7be90' # str | The id of the webhook.
    webhook_body = sunshine_conversations_client.WebhookBody() # WebhookBody | 

    try:
        # Update Webhook
        api_response = api_instance.update_webhook(app_id, integration_id, webhook_id, webhook_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
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
    api_instance = sunshine_conversations_client.WebhooksApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    integration_id = '029c31f25a21b47effd7be90' # str | The id of the integration.
    webhook_id = '029c31f25a21b47effd7be90' # str | The id of the webhook.
    webhook_body = sunshine_conversations_client.WebhookBody() # WebhookBody | 

    try:
        # Update Webhook
        api_response = api_instance.update_webhook(app_id, integration_id, webhook_id, webhook_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| The id of the integration. | 
 **webhook_id** | **str**| The id of the webhook. | 
 **webhook_body** | [**WebhookBody**](WebhookBody.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

