# sunshine_conversations_client.AttachmentsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment**](AttachmentsApi.md#delete_attachment) | **POST** /v2/apps/{appId}/attachments/remove | Delete Attachment
[**generate_media_json_web_token**](AttachmentsApi.md#generate_media_json_web_token) | **POST** /v2/apps/{appId}/attachments/token | Generate Media Token
[**set_cookie**](AttachmentsApi.md#set_cookie) | **GET** /v2/apps/{appId}/attachments/cookie | Set Cookie
[**upload_attachment**](AttachmentsApi.md#upload_attachment) | **POST** /v2/apps/{appId}/attachments | Upload Attachment


## delete_attachment
> object delete_attachment(app_id, attachment_delete_body)

Delete Attachment

Remove an attachment uploaded to Sunshine Conversations through the Upload attachment API. See [Attachments for Messages](#section/Attachments-for-Messages) to have attachments automatically deleted when deleting messages, conversations or users. <aside class=\"notice\">Note that deleted attachments can remain available on our CDN’s cache up to 15 minutes after the delete call.</aside> 

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
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    attachment_delete_body = sunshine_conversations_client.AttachmentDeleteBody() # AttachmentDeleteBody | 

    try:
        # Delete Attachment
        api_response = api_instance.delete_attachment(app_id, attachment_delete_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    attachment_delete_body = sunshine_conversations_client.AttachmentDeleteBody() # AttachmentDeleteBody | 

    try:
        # Delete Attachment
        api_response = api_instance.delete_attachment(app_id, attachment_delete_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **attachment_delete_body** | [**AttachmentDeleteBody**](AttachmentDeleteBody.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Attachment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## generate_media_json_web_token
> AttachmentMediaTokenResponse generate_media_json_web_token(app_id, attachment_media_token_body)

Generate Media Token

Generates a media JWT for a list of attachment paths. 

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
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    attachment_media_token_body = sunshine_conversations_client.AttachmentMediaTokenBody() # AttachmentMediaTokenBody | 

    try:
        # Generate Media Token
        api_response = api_instance.generate_media_json_web_token(app_id, attachment_media_token_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->generate_media_json_web_token: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    attachment_media_token_body = sunshine_conversations_client.AttachmentMediaTokenBody() # AttachmentMediaTokenBody | 

    try:
        # Generate Media Token
        api_response = api_instance.generate_media_json_web_token(app_id, attachment_media_token_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->generate_media_json_web_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **attachment_media_token_body** | [**AttachmentMediaTokenBody**](AttachmentMediaTokenBody.md)|  | 

### Return type

[**AttachmentMediaTokenResponse**](AttachmentMediaTokenResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## set_cookie
> object set_cookie(app_id)

Set Cookie

With the media JWT retrieved, pass it in the header of the below request as it’s authorization in order to set a cookie in the user’s browser corresponding to the path within the media JWT. The expiration date of this cookie will match the expiration date of the media JWT.  

### Example

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

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.

    try:
        # Set Cookie
        api_response = api_instance.set_cookie(app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->set_cookie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## upload_attachment
> AttachmentResponse upload_attachment(app_id, access, source, _for=_for, conversation_id=conversation_id)

Upload Attachment

Upload an attachment to Sunshine Conversations to use in future messages. Files are uploaded using the multipart/form-data content type. Use the returned mediaUrl to send a file, image or carousel message. <aside class=\"notice\">Note that Sunshine Conversations limits the size and type of file you can upload to the platform. See the <a href=\"https://docs.smooch.io/guide/validating-files\">file validation</a> guide for more details.</aside> 

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
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    access = 'public' # str | The access level for the attachment. Currently the available access levels are public and private. If you are a licensed Zendesk customer, you must use public. Private is not supported. (default to 'public')
    source = '/path/to/file' # file | 
    _for = 'message' # str | Specifies the intended container for the attachment, to enable automatic attachment deletion (on deletion of associated message, conversation or user). For now, only message is supported. See [Attachments for Messages](#section/Attachments-for-Messages) for details. (optional)
    conversation_id = 'c616a583e4c240a871818541' # str | Links the attachment getting uploaded to the conversation ID. (optional)

    try:
        # Upload Attachment
        api_response = api_instance.upload_attachment(app_id, access, source, _for=_for, conversation_id=conversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
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
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    access = 'public' # str | The access level for the attachment. Currently the available access levels are public and private. If you are a licensed Zendesk customer, you must use public. Private is not supported. (default to 'public')
    source = '/path/to/file' # file | 
    _for = 'message' # str | Specifies the intended container for the attachment, to enable automatic attachment deletion (on deletion of associated message, conversation or user). For now, only message is supported. See [Attachments for Messages](#section/Attachments-for-Messages) for details. (optional)
    conversation_id = 'c616a583e4c240a871818541' # str | Links the attachment getting uploaded to the conversation ID. (optional)

    try:
        # Upload Attachment
        api_response = api_instance.upload_attachment(app_id, access, source, _for=_for, conversation_id=conversation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **access** | **str**| The access level for the attachment. Currently the available access levels are public and private. If you are a licensed Zendesk customer, you must use public. Private is not supported. | [default to &#39;public&#39;]
 **source** | **file**|  | 
 **_for** | **str**| Specifies the intended container for the attachment, to enable automatic attachment deletion (on deletion of associated message, conversation or user). For now, only message is supported. See [Attachments for Messages](#section/Attachments-for-Messages) for details. | [optional] 
 **conversation_id** | **str**| Links the attachment getting uploaded to the conversation ID. | [optional] 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

