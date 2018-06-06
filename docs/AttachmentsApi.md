# smooch.AttachmentsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_attachment**](AttachmentsApi.md#remove_attachment) | **POST** /v1/apps/{appId}/attachments/remove | 
[**upload_attachment**](AttachmentsApi.md#upload_attachment) | **POST** /v1/apps/{appId}/attachments | 


# **remove_attachment**
> remove_attachment(app_id, attachment_remove_body)



Remove an attachment uploaded to Smooch.

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
attachment_remove_body = smooch.AttachmentRemove() # AttachmentRemove | Body for a removeAttachment request. 

try:
    api_instance.remove_attachment(app_id, attachment_remove_body)
except ApiException as e:
    print("Exception when calling AttachmentsApi->remove_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **attachment_remove_body** | [**AttachmentRemove**](AttachmentRemove.md)| Body for a removeAttachment request.  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_attachment**
> AttachmentResponse upload_attachment(app_id, source, access, _for=_for, app_user_id=app_user_id, user_id=user_id)



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
_for = '_for_example' # str | The intended container for the attachment (optional)
app_user_id = 'app_user_id_example' # str | The appUserId of the user that will receive the attachment Used in attachments for messages  (optional)
user_id = 'user_id_example' # str | The userId of the user that will receive the attachment Used in attachments for messages  (optional)

try:
    api_response = api_instance.upload_attachment(app_id, source, access, _for=_for, app_user_id=app_user_id, user_id=user_id)
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
 **_for** | **str**| The intended container for the attachment | [optional] 
 **app_user_id** | **str**| The appUserId of the user that will receive the attachment Used in attachments for messages  | [optional] 
 **user_id** | **str**| The userId of the user that will receive the attachment Used in attachments for messages  | [optional] 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

