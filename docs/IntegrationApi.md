# smooch.IntegrationApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration**](IntegrationApi.md#create_integration) | **POST** /v1.1/apps/{appId}/integrations | 
[**create_integration_menu**](IntegrationApi.md#create_integration_menu) | **POST** /v1.1/apps/{appId}/integrations/{integrationId}/menu | 
[**delete_integration**](IntegrationApi.md#delete_integration) | **DELETE** /v1.1/apps/{appId}/integrations/{integrationId} | 
[**delete_integration_menu**](IntegrationApi.md#delete_integration_menu) | **DELETE** /v1.1/apps/{appId}/integrations/{integrationId}/menu | 
[**get_integration**](IntegrationApi.md#get_integration) | **GET** /v1.1/apps/{appId}/integrations/{integrationId} | 
[**get_integration_menu**](IntegrationApi.md#get_integration_menu) | **GET** /v1.1/apps/{appId}/integrations/{integrationId}/menu | 
[**list_integrations**](IntegrationApi.md#list_integrations) | **GET** /v1.1/apps/{appId}/integrations | 
[**update_integration**](IntegrationApi.md#update_integration) | **PUT** /v1.1/apps/{appId}/integrations/{integrationId} | 
[**update_integration_menu**](IntegrationApi.md#update_integration_menu) | **PUT** /v1.1/apps/{appId}/integrations/{integrationId}/menu | 
[**update_integration_profile**](IntegrationApi.md#update_integration_profile) | **PUT** /v1.1/apps/{appId}/integrations/{integrationId}/profile | 


# **create_integration**
> IntegrationResponse create_integration(app_id, integration_create_body)



Create an integration for the specified app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_create_body = smooch.IntegrationCreate() # IntegrationCreate | Body for a createIntegration request. Additional arguments are necessary based on integration type. For detailed instructions, visit our [official docs](https://docs.smooch.io/rest/#create-integration) 

try:
    api_response = api_instance.create_integration(app_id, integration_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_create_body** | [**IntegrationCreate**](IntegrationCreate.md)| Body for a createIntegration request. Additional arguments are necessary based on integration type. For detailed instructions, visit our [official docs](https://docs.smooch.io/rest/#create-integration)  | 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_integration_menu**
> MenuResponse create_integration_menu(app_id, integration_id, menu_create_body)



Create the specified integration’s menu, overriding the app menu if configured.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.
menu_create_body = smooch.Menu() # Menu | Body for a createMenu request.

try:
    api_response = api_instance.create_integration_menu(app_id, integration_id, menu_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_integration_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 
 **menu_create_body** | [**Menu**](Menu.md)| Body for a createMenu request. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> delete_integration(app_id, integration_id)



Delete the specified integration.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.

try:
    api_instance.delete_integration(app_id, integration_id)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration_menu**
> delete_integration_menu(app_id, integration_id)



Delete the specified integration’s menu.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.

try:
    api_instance.delete_integration_menu(app_id, integration_id)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_integration_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> IntegrationResponse get_integration(app_id, integration_id)



Get the specified integration.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.

try:
    api_response = api_instance.get_integration(app_id, integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_menu**
> MenuResponse get_integration_menu(app_id, integration_id)



Get the specified integration's menu.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.

try:
    api_response = api_instance.get_integration_menu(app_id, integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_integration_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> ListIntegrationsResponse list_integrations(app_id, types=types)



List integrations for the specified app.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
types = 'types_example' # str | List of types to filter the query by. More than one value can be specified through comma separation e.g. ?types=*twilio*,*line*.  (optional)

try:
    api_response = api_instance.list_integrations(app_id, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->list_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **types** | **str**| List of types to filter the query by. More than one value can be specified through comma separation e.g. ?types&#x3D;*twilio*,*line*.  | [optional] 

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration**
> IntegrationResponse update_integration(app_id, integration_id, integration_update_body)



Update the specified integration.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.
integration_update_body = smooch.IntegrationUpdate() # IntegrationUpdate | Body for a updateIntegration request. Additional arguments are necessary based on integration type. For detailed instructions, visit our [official docs](https://docs.smooch.io/rest/#create-integration) 

try:
    api_response = api_instance.update_integration(app_id, integration_id, integration_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 
 **integration_update_body** | [**IntegrationUpdate**](IntegrationUpdate.md)| Body for a updateIntegration request. Additional arguments are necessary based on integration type. For detailed instructions, visit our [official docs](https://docs.smooch.io/rest/#create-integration)  | 

### Return type

[**IntegrationResponse**](IntegrationResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_menu**
> MenuResponse update_integration_menu(app_id, integration_id, menu_update_body)



Update the specified integration’s menu.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.
menu_update_body = smooch.Menu() # Menu | Body for a updateMenu request.

try:
    api_response = api_instance.update_integration_menu(app_id, integration_id, menu_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_integration_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 
 **menu_update_body** | [**Menu**](Menu.md)| Body for a updateMenu request. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_profile**
> update_integration_profile(app_id, integration_id, integration_profile_body)



Update the specified integration’s profile.

### Example
```python
from __future__ import print_statement
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.IntegrationApi()
app_id = 'app_id_example' # str | Identifies the app.
integration_id = 'integration_id_example' # str | Identifies the integration.
integration_profile_body = smooch.IntegrationProfileUpdate() # IntegrationProfileUpdate | Body for a profileUpdate request.

try:
    api_instance.update_integration_profile(app_id, integration_id, integration_profile_body)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_integration_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **integration_id** | **str**| Identifies the integration. | 
 **integration_profile_body** | [**IntegrationProfileUpdate**](IntegrationProfileUpdate.md)| Body for a profileUpdate request. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

