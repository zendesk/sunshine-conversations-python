# smooch.TemplateApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplateApi.md#create_template) | **POST** /v1/apps/{appId}/templates | 
[**delete_template**](TemplateApi.md#delete_template) | **DELETE** /v1/apps/{appId}/templates/{templateId} | 
[**get_template**](TemplateApi.md#get_template) | **GET** /v1/apps/{appId}/templates/{templateId} | 
[**list_templates**](TemplateApi.md#list_templates) | **GET** /v1/apps/{appId}/templates | 
[**update_template**](TemplateApi.md#update_template) | **PUT** /v1/apps/{appId}/templates/{templateId} | 


# **create_template**
> TemplateResponse create_template(app_id, template_create_body)



Create a template for the specified app.

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
api_instance = smooch.TemplateApi()
app_id = 'app_id_example' # str | Identifies the app.
template_create_body = smooch.TemplateCreate() # TemplateCreate | Body for a createTemplate request. 

try:
    api_response = api_instance.create_template(app_id, template_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **template_create_body** | [**TemplateCreate**](TemplateCreate.md)| Body for a createTemplate request.  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(app_id, template_id)



Delete the specified template.

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
api_instance = smooch.TemplateApi()
app_id = 'app_id_example' # str | Identifies the app.
template_id = 'template_id_example' # str | Identifies the template.

try:
    api_instance.delete_template(app_id, template_id)
except ApiException as e:
    print("Exception when calling TemplateApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **template_id** | **str**| Identifies the template. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> TemplateResponse get_template(app_id, template_id)



Get the specified template.

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
api_instance = smooch.TemplateApi()
app_id = 'app_id_example' # str | Identifies the app.
template_id = 'template_id_example' # str | Identifies the template.

try:
    api_response = api_instance.get_template(app_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **template_id** | **str**| Identifies the template. | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> ListTemplatesResponse list_templates(app_id, limit=limit, offset=offset)



List templates for the specified app.

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
api_instance = smooch.TemplateApi()
app_id = 'app_id_example' # str | Identifies the app.
limit = 25 # int | The number of records to return. (optional) (default to 25)
offset = 0 # int | The number of initial records to skip before picking records to return. (optional) (default to 0)

try:
    api_response = api_instance.list_templates(app_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **limit** | **int**| The number of records to return. | [optional] [default to 25]
 **offset** | **int**| The number of initial records to skip before picking records to return. | [optional] [default to 0]

### Return type

[**ListTemplatesResponse**](ListTemplatesResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> TemplateResponse update_template(app_id, template_id, template_update_body)



Update the specified template.

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
api_instance = smooch.TemplateApi()
app_id = 'app_id_example' # str | Identifies the app.
template_id = 'template_id_example' # str | Identifies the template.
template_update_body = smooch.TemplateUpdate() # TemplateUpdate | Body for an updateTemplate request. 

try:
    api_response = api_instance.update_template(app_id, template_id, template_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **template_id** | **str**| Identifies the template. | 
 **template_update_body** | [**TemplateUpdate**](TemplateUpdate.md)| Body for an updateTemplate request.  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

