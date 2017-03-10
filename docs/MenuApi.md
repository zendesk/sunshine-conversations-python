# swagger_client.MenuApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_menu**](MenuApi.md#delete_menu) | **DELETE** /menu | 
[**get_menu**](MenuApi.md#get_menu) | **GET** /menu | 
[**update_menu**](MenuApi.md#update_menu) | **PUT** /menu | 


# **delete_menu**
> MenuResponse delete_menu()



Remove the specified app’s menu.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: appToken
swagger_client.configuration.api_key['app-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['app-token'] = 'Bearer'
# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MenuApi()

try: 
    api_response = api_instance.delete_menu()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->delete_menu: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[appToken](../README.md#appToken), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_menu**
> MenuResponse get_menu()



Get the specified app’s menu.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MenuApi()

try: 
    api_response = api_instance.get_menu()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->get_menu: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_menu**
> MenuResponse update_menu(menu_update)



Configure the specified app’s menu.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MenuApi()
menu_update = swagger_client.Menu() # Menu | Supported properties for a updateMenu request.

try: 
    api_response = api_instance.update_menu(menu_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->update_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_update** | [**Menu**](Menu.md)| Supported properties for a updateMenu request. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

