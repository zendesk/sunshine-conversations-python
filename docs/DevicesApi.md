# sunshine_conversations_client.DevicesApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device**](DevicesApi.md#get_device) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/devices/{deviceId} | Get Device
[**list_devices**](DevicesApi.md#list_devices) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/devices | List Devices


## get_device
> DeviceResponse get_device(app_id, user_id_or_external_id, device_id)

Get Device

Fetches a specific Device. 

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
    api_instance = sunshine_conversations_client.DevicesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    device_id = '5d8cff3cd55b040010928b5b' # str | The device's id.

    try:
        # Get Device
        api_response = api_instance.get_device(app_id, user_id_or_external_id, device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
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
    api_instance = sunshine_conversations_client.DevicesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.
    device_id = '5d8cff3cd55b040010928b5b' # str | The device's id.

    try:
        # Get Device
        api_response = api_instance.get_device(app_id, user_id_or_external_id, device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 
 **device_id** | **str**| The device&#39;s id. | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

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

## list_devices
> DeviceListResponse list_devices(app_id, user_id_or_external_id)

List Devices

Get all the devices for a particular user. The Devices are sorted based on last seen time. 

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
    api_instance = sunshine_conversations_client.DevicesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # List Devices
        api_response = api_instance.list_devices(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->list_devices: %s\n" % e)
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
    api_instance = sunshine_conversations_client.DevicesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    user_id_or_external_id = '42589ad070d43be9b00ff7e5' # str | The user's id or externalId.

    try:
        # List Devices
        api_response = api_instance.list_devices(app_id, user_id_or_external_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->list_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id_or_external_id** | **str**| The user&#39;s id or externalId. | 

### Return type

[**DeviceListResponse**](DeviceListResponse.md)

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

