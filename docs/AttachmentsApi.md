# smooch.AttachmentsApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_attachment**](AttachmentsApi.md#upload_attachment) | **POST** /apps/{appId}/attachments | 


# **upload_attachment**
> AttachmentResponse upload_attachment(app_id, source, access)



Upload an attachment to Smooch to use in future messages.

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
api_instance = smooch.AttachmentsApi()
app_id = 'app_id_example' # str | Identifies the app.
source = '/path/to/file.txt' # file | File to be uploaded
access = 'access_example' # str | Access level for the resulting file

try:
    api_response = api_instance.upload_attachment(app_id, source, access)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **source** | **file**| File to be uploaded | 
 **access** | **str**| Access level for the resulting file | 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
