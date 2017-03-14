# smooch.IntegrationApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration**](IntegrationApi.md#create_integration) | **POST** /apps/{appId}/integrations | 
[**list_integrations**](IntegrationApi.md#list_integrations) | **GET** /apps/{appId}/integrations | 


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
smooch.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

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
smooch.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

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

