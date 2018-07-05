# smooch.AppUserApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app_user**](AppUserApi.md#delete_app_user) | **DELETE** /v1/apps/{appId}/appusers/{userId} | 
[**delete_app_user_profile**](AppUserApi.md#delete_app_user_profile) | **DELETE** /v1/apps/{appId}/appusers/{userId}/profile | 
[**get_app_user**](AppUserApi.md#get_app_user) | **GET** /v1/apps/{appId}/appusers/{userId} | 
[**get_app_user_auth_code**](AppUserApi.md#get_app_user_auth_code) | **GET** /v1/apps/{appId}/appusers/{userId}/authcode | 
[**get_app_user_business_system_ids**](AppUserApi.md#get_app_user_business_system_ids) | **GET** /v1/apps/{appId}/appusers/{userId}/businesssystems | 
[**get_app_user_entity_ids**](AppUserApi.md#get_app_user_entity_ids) | **GET** /v1/apps/{appId}/appusers/{userId}/channels | 
[**get_link_requests**](AppUserApi.md#get_link_requests) | **GET** /v1/apps/{appId}/appusers/{userId}/linkrequest | 
[**link_app_user**](AppUserApi.md#link_app_user) | **POST** /v1/apps/{appId}/appusers/{userId}/channels | 
[**post_image_message**](AppUserApi.md#post_image_message) | **POST** /v1/apps/{appId}/appusers/{userId}/images | 
[**pre_create_app_user**](AppUserApi.md#pre_create_app_user) | **POST** /v1/apps/{appId}/appusers | 
[**unlink_app_user**](AppUserApi.md#unlink_app_user) | **DELETE** /v1/apps/{appId}/appusers/{userId}/channels/{channel} | 
[**update_app_user**](AppUserApi.md#update_app_user) | **PUT** /v1/apps/{appId}/appusers/{userId} | 


# **delete_app_user**
> delete_app_user(app_id, user_id)



Delete specified app user.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_instance.delete_app_user(app_id, user_id)
except ApiException as e:
    print("Exception when calling AppUserApi->delete_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_user_profile**
> AppUserResponse delete_app_user_profile(app_id, user_id)



Delete specified app user's profile.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_response = api_instance.delete_app_user_profile(app_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->delete_app_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_user**
> AppUserResponse get_app_user(app_id, user_id)



Get the specified app user.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_response = api_instance.get_app_user(app_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_user_auth_code**
> AuthCodeResponse get_app_user_auth_code(app_id, user_id)



Get an auth code for facilitating a channel transfer

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_response = api_instance.get_app_user_auth_code(app_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_app_user_auth_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AuthCodeResponse**](AuthCodeResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_user_business_system_ids**
> AppUserBusinessSystemsResponse get_app_user_business_system_ids(app_id, user_id)



Get specified app user's business system IDs.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_response = api_instance.get_app_user_business_system_ids(app_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_app_user_business_system_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AppUserBusinessSystemsResponse**](AppUserBusinessSystemsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_user_entity_ids**
> AppUserChannelsResponse get_app_user_entity_ids(app_id, user_id)



Get specified app user's channel entity IDs.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try:
    api_response = api_instance.get_app_user_entity_ids(app_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_app_user_entity_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AppUserChannelsResponse**](AppUserChannelsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_requests**
> LinkRequestResponse get_link_requests(app_id, user_id, integration_ids)



Fetch link requests for the specified app user.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
integration_ids = ['integration_ids_example'] # list[str] | List of integration IDs

try:
    api_response = api_instance.get_link_requests(app_id, user_id, integration_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_link_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **integration_ids** | [**list[str]**](str.md)| List of integration IDs | 

### Return type

[**LinkRequestResponse**](LinkRequestResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_app_user**
> AppUserResponse link_app_user(app_id, user_id, app_user_link_body)



Link specified app user to given channel.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
app_user_link_body = smooch.AppUserLink() # AppUserLink | Body for a linkAppUser request.

try:
    api_response = api_instance.link_app_user(app_id, user_id, app_user_link_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->link_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **app_user_link_body** | [**AppUserLink**](AppUserLink.md)| Body for a linkAppUser request. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_message**
> MessageResponse post_image_message(app_id, user_id, source, role)



Send an image message to the conversation.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
source = '/path/to/file.txt' # file | Image to be uploaded
role = 'role_example' # str | Role of the sender

try:
    api_response = api_instance.post_image_message(app_id, user_id, source, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->post_image_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **source** | **file**| Image to be uploaded | 
 **role** | **str**| Role of the sender | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_create_app_user**
> AppUserResponse pre_create_app_user(app_id, app_user_pre_create_body)



Pre-create an app user.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
app_user_pre_create_body = smooch.AppUserPreCreate() # AppUserPreCreate | Body for a preCreateAppUser request.

try:
    api_response = api_instance.pre_create_app_user(app_id, app_user_pre_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->pre_create_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **app_user_pre_create_body** | [**AppUserPreCreate**](AppUserPreCreate.md)| Body for a preCreateAppUser request. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_app_user**
> unlink_app_user(app_id, user_id, channel)



Unlink specified app user from given channel.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
channel = 'channel_example' # str | Name of the channel.

try:
    api_instance.unlink_app_user(app_id, user_id, channel)
except ApiException as e:
    print("Exception when calling AppUserApi->unlink_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **channel** | **str**| Name of the channel. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_user**
> AppUserResponse update_app_user(app_id, user_id, app_user_update_body)



Update the specified app user.

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
api_instance = smooch.AppUserApi()
app_id = 'app_id_example' # str | Identifies the app.
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
app_user_update_body = smooch.AppUserUpdate() # AppUserUpdate | Body for an updateAppUser request.

try:
    api_response = api_instance.update_app_user(app_id, user_id, app_user_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->update_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **app_user_update_body** | [**AppUserUpdate**](AppUserUpdate.md)| Body for an updateAppUser request. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

