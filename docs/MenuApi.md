# smooch.MenuApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_menu**](MenuApi.md#delete_menu) | **DELETE** /v1.1/apps/{appId}/menu | 
[**get_menu**](MenuApi.md#get_menu) | **GET** /v1.1/apps/{appId}/menu | 
[**update_menu**](MenuApi.md#update_menu) | **PUT** /v1.1/apps/{appId}/menu | 


# **delete_menu**
> MenuResponse delete_menu(app_id)



Remove the specified app’s menu.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.MenuApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.delete_menu(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->delete_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_menu**
> MenuResponse get_menu(app_id)



Get the specified app’s menu.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.MenuApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.get_menu(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->get_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_menu**
> MenuResponse update_menu(app_id, menu_update_body)



Configure the specified app’s menu.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.MenuApi()
app_id = 'app_id_example' # str | Identifies the app.
menu_update_body = smooch.Menu() # Menu | Body for a updateMenu request.

try:
    api_response = api_instance.update_menu(app_id, menu_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->update_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **menu_update_body** | [**Menu**](Menu.md)| Body for a updateMenu request. | 

### Return type

[**MenuResponse**](MenuResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

