# sunshine_conversations_client.SwitchboardIntegrationsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_switchboard_integration**](SwitchboardIntegrationsApi.md#create_switchboard_integration) | **POST** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations | Create Switchboard Integration
[**delete_switchboard_integration**](SwitchboardIntegrationsApi.md#delete_switchboard_integration) | **DELETE** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations/{switchboardIntegrationId} | Delete Switchboard Integration
[**list_switchboard_integrations**](SwitchboardIntegrationsApi.md#list_switchboard_integrations) | **GET** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations | List Switchboard Integrations
[**update_switchboard_integration**](SwitchboardIntegrationsApi.md#update_switchboard_integration) | **PATCH** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations/{switchboardIntegrationId} | Update Switchboard Integration


## create_switchboard_integration
> SwitchboardIntegrationResponse create_switchboard_integration(app_id, switchboard_id, switchboard_integration_create_body)

Create Switchboard Integration

Create a switchboard integration.

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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.
    switchboard_integration_create_body = {"name":"bot","integrationType":"zd:agentWorkspace","deliverStandbyEvents":true,"nextSwitchboardIntegrationId":"5ef21b86e933b7355c11c606","messageHistoryCount":5} # SwitchboardIntegrationCreateBody | 

    try:
        # Create Switchboard Integration
        api_response = api_instance.create_switchboard_integration(app_id, switchboard_id, switchboard_integration_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->create_switchboard_integration: %s\n" % e)
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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.
    switchboard_integration_create_body = {"name":"bot","integrationType":"zd:agentWorkspace","deliverStandbyEvents":true,"nextSwitchboardIntegrationId":"5ef21b86e933b7355c11c606","messageHistoryCount":5} # SwitchboardIntegrationCreateBody | 

    try:
        # Create Switchboard Integration
        api_response = api_instance.create_switchboard_integration(app_id, switchboard_id, switchboard_integration_create_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->create_switchboard_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **switchboard_id** | **str**| Identifies the switchboard. | 
 **switchboard_integration_create_body** | [**SwitchboardIntegrationCreateBody**](SwitchboardIntegrationCreateBody.md)|  | 

### Return type

[**SwitchboardIntegrationResponse**](SwitchboardIntegrationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Only one switchboard per app can be created |  -  |
**404** | Switchboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## delete_switchboard_integration
> object delete_switchboard_integration(app_id, switchboard_id, switchboard_integration_id)

Delete Switchboard Integration

Deletes the switchboard integration. If the deleted switchboard integration had an active status for some conversations, the default switchboard integration will replace it. Note that it is forbidden to delete a switchboard integration if it's the default one (a new one must be chosen first) or if another switchboard integration's `nextSwitchboardIntegrationId` refers to it. The integration that was linked to the deleted switchboard integration will start receiving all conversation events, regardless of the switchboard status.

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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.
    switchboard_integration_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard integration.

    try:
        # Delete Switchboard Integration
        api_response = api_instance.delete_switchboard_integration(app_id, switchboard_id, switchboard_integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->delete_switchboard_integration: %s\n" % e)
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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.
    switchboard_integration_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard integration.

    try:
        # Delete Switchboard Integration
        api_response = api_instance.delete_switchboard_integration(app_id, switchboard_id, switchboard_integration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->delete_switchboard_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **switchboard_id** | **str**| Identifies the switchboard. | 
 **switchboard_integration_id** | **str**| Identifies the switchboard integration. | 

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

## list_switchboard_integrations
> SwitchboardIntegrationListResponse list_switchboard_integrations(app_id, switchboard_id)

List Switchboard Integrations

Lists all switchboard integrations linked to the switchboard. 

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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.

    try:
        # List Switchboard Integrations
        api_response = api_instance.list_switchboard_integrations(app_id, switchboard_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->list_switchboard_integrations: %s\n" % e)
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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.

    try:
        # List Switchboard Integrations
        api_response = api_instance.list_switchboard_integrations(app_id, switchboard_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->list_switchboard_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **switchboard_id** | **str**| Identifies the switchboard. | 

### Return type

[**SwitchboardIntegrationListResponse**](SwitchboardIntegrationListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Switchboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## update_switchboard_integration
> SwitchboardIntegrationResponse update_switchboard_integration(app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body)

Update Switchboard Integration

Updates a switchboard integration record.

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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.
    switchboard_integration_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard integration.
    switchboard_integration_update_body = {"name":"bot","integrationType":"zd:agentWorkspace","deliverStandbyEvents":true,"nextSwitchboardIntegrationId":"5ef21b86e933b7355c11c606","messageHistoryCount":5} # SwitchboardIntegrationUpdateBody | 

    try:
        # Update Switchboard Integration
        api_response = api_instance.update_switchboard_integration(app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->update_switchboard_integration: %s\n" % e)
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
    api_instance = sunshine_conversations_client.SwitchboardIntegrationsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    switchboard_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard.
    switchboard_integration_id = '5d8cff3cd55b040010928b5b' # str | Identifies the switchboard integration.
    switchboard_integration_update_body = {"name":"bot","integrationType":"zd:agentWorkspace","deliverStandbyEvents":true,"nextSwitchboardIntegrationId":"5ef21b86e933b7355c11c606","messageHistoryCount":5} # SwitchboardIntegrationUpdateBody | 

    try:
        # Update Switchboard Integration
        api_response = api_instance.update_switchboard_integration(app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SwitchboardIntegrationsApi->update_switchboard_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **switchboard_id** | **str**| Identifies the switchboard. | 
 **switchboard_integration_id** | **str**| Identifies the switchboard integration. | 
 **switchboard_integration_update_body** | [**SwitchboardIntegrationUpdateBody**](SwitchboardIntegrationUpdateBody.md)|  | 

### Return type

[**SwitchboardIntegrationResponse**](SwitchboardIntegrationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Enabled switchboard must have an associated default switchboardIntegration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

