# sunshine_conversations_client.AttachmentsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment**](AttachmentsApi.md#delete_attachment) | **POST** /v2/apps/{appId}/attachments/remove | Delete Attachment
[**upload_attachment**](AttachmentsApi.md#upload_attachment) | **POST** /v2/apps/{appId}/attachments | Upload Attachment


# **delete_attachment**
> object delete_attachment(app_id, attachment_delete_body)

Delete Attachment

Remove an attachment uploaded to Sunshine Conversations through the Upload attachment API.
See [Attachments for Messages](#section/Attachments-for-Messages) to have attachments automatically deleted when deleting messages, conversations or users.
<aside class="notice"><strong>Note:</strong> Deleted attachments can remain available on our CDN's cache up to 15 minutes after the delete call.</aside>


### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import sunshine_conversations_client
from sunshine_conversations_client.models.attachment_delete_body import AttachmentDeleteBody
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
configuration = sunshine_conversations_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = sunshine_conversations_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    attachment_delete_body = sunshine_conversations_client.AttachmentDeleteBody() # AttachmentDeleteBody | 

    try:
        # Delete Attachment
        api_response = api_instance.delete_attachment(app_id, attachment_delete_body)
        print("The response of AttachmentsApi->delete_attachment:\n")
        pprint(api_response)
    except Exception as e:
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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_attachment**
> AttachmentResponse upload_attachment(app_id, access, source, var_for=var_for, conversation_id=conversation_id)

Upload Attachment

Upload an attachment to Sunshine Conversations to use in future messages. Files are uploaded using the multipart/form-data content type. Use the returned mediaUrl to send a file, image or carousel message.
<aside class="notice"><strong>Note:</strong> Sunshine Conversations limits the size and type of file you can upload to the platform. See the <a href="https://support.zendesk.com/hc/en-us/articles/8435939957914#topic_v1r_rwr_mdc">file validation</a> guide for more details.</aside>


### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import sunshine_conversations_client
from sunshine_conversations_client.models.attachment_response import AttachmentResponse
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
configuration = sunshine_conversations_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = sunshine_conversations_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.AttachmentsApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    access = 'public' # str | The access level for the attachment. Currently the only available access level is public. Private is not supported. (default to 'public')
    source = None # bytearray | 
    var_for = 'message' # str | Specifies the intended container for the attachment, to enable automatic attachment deletion (on deletion of associated message, conversation or user). For now, only message is supported. See [Attachments for Messages](#section/Attachments-for-Messages) for details. (optional)
    conversation_id = 'c616a583e4c240a871818541' # str | Links the attachment getting uploaded to the conversation ID. (optional)

    try:
        # Upload Attachment
        api_response = api_instance.upload_attachment(app_id, access, source, var_for=var_for, conversation_id=conversation_id)
        print("The response of AttachmentsApi->upload_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->upload_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **access** | **str**| The access level for the attachment. Currently the only available access level is public. Private is not supported. | [default to &#39;public&#39;]
 **source** | **bytearray**|  | 
 **var_for** | **str**| Specifies the intended container for the attachment, to enable automatic attachment deletion (on deletion of associated message, conversation or user). For now, only message is supported. See [Attachments for Messages](#section/Attachments-for-Messages) for details. | [optional] 
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

