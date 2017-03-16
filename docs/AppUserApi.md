# smooch.AppUserApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_user_device_update**](AppUserApi.md#app_user_device_update) | **PUT** /appusers/{userId}/devices/{deviceId} | 
[**delete_app_user_profile**](AppUserApi.md#delete_app_user_profile) | **DELETE** /appusers/{userId}/profile | 
[**get_app_user**](AppUserApi.md#get_app_user) | **GET** /appusers/{userId} | 
[**get_app_user_entity_ids**](AppUserApi.md#get_app_user_entity_ids) | **GET** /appusers/{userId}/channels | 
[**link_app_user**](AppUserApi.md#link_app_user) | **POST** /appusers/{userId}/channels | 
[**post_image_message**](AppUserApi.md#post_image_message) | **POST** /appusers/{userId}/images | 
[**pre_create_app_user**](AppUserApi.md#pre_create_app_user) | **POST** /appusers | 
[**track_event**](AppUserApi.md#track_event) | **POST** /appusers/{userId}/events | 
[**unlink_app_user**](AppUserApi.md#unlink_app_user) | **DELETE** /appusers/{userId}/channels/{channel} | 
[**update_app_user**](AppUserApi.md#update_app_user) | **PUT** /appusers/{userId} | 


# **app_user_device_update**
> DeviceResponse app_user_device_update(user_id, device_id, app_user_device_update_body)



Update specified device information.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
device_id = 'device_id_example' # str | Identifies the device.
app_user_device_update_body = smooch.DeviceUpdate() # DeviceUpdate | Body for an updateAppUserDevice request.

try: 
    api_response = api_instance.app_user_device_update(user_id, device_id, app_user_device_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->app_user_device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **device_id** | **str**| Identifies the device. | 
 **app_user_device_update_body** | [**DeviceUpdate**](DeviceUpdate.md)| Body for an updateAppUserDevice request. | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_user_profile**
> AppUserResponse delete_app_user_profile(user_id)



Delete specified app user's profile.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try: 
    api_response = api_instance.delete_app_user_profile(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->delete_app_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AppUserResponse get_app_user(user_id)



Get the specified app user.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try: 
    api_response = api_instance.get_app_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_user_entity_ids**
> AppUserResponse get_app_user_entity_ids(user_id)



Get specified app user's channel entity IDs.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.

try: 
    api_response = api_instance.get_app_user_entity_ids(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->get_app_user_entity_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_app_user**
> AppUserResponse link_app_user(user_id, app_user_link_body)



Link specified app user to given channel.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
app_user_link_body = smooch.AppUserLink() # AppUserLink | Body for a linkAppUser request.

try: 
    api_response = api_instance.link_app_user(user_id, app_user_link_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->link_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> MessageResponse post_image_message(user_id, source, role)



Send an image message to the conversation.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
source = '/path/to/file.txt' # file | Image to be uploaded
role = 'role_example' # str | Role of the sender

try: 
    api_response = api_instance.post_image_message(user_id, source, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->post_image_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AppUserResponse pre_create_app_user(app_user_pre_create_body)



Pre-create an app user.

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
api_instance = smooch.AppUserApi()
app_user_pre_create_body = smooch.AppUserPreCreate() # AppUserPreCreate | Body for a preCreateAppUser request.

try: 
    api_response = api_instance.pre_create_app_user(app_user_pre_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->pre_create_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_user_pre_create_body** | [**AppUserPreCreate**](AppUserPreCreate.md)| Body for a preCreateAppUser request. | 

### Return type

[**AppUserResponse**](AppUserResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_event**
> TrackEventResponse track_event(user_id, track_event_body)



Track an event for the given app user.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
track_event_body = smooch.Event() # Event | Body for a trackEvent request.

try: 
    api_response = api_instance.track_event(user_id, track_event_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->track_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Identifies the user. Can be either the smoochId or the userId. | 
 **track_event_body** | [**Event**](Event.md)| Body for a trackEvent request. | 

### Return type

[**TrackEventResponse**](TrackEventResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_app_user**
> unlink_app_user(user_id, channel)



Unlink specified app user from given channel.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
channel = 'channel_example' # str | Name of the channel.

try: 
    api_instance.unlink_app_user(user_id, channel)
except ApiException as e:
    print("Exception when calling AppUserApi->unlink_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AppUserResponse update_app_user(user_id, app_user_update_body)



Update the specified app user.

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
api_instance = smooch.AppUserApi()
user_id = 'user_id_example' # str | Identifies the user. Can be either the smoochId or the userId.
app_user_update_body = smooch.AppUserUpdate() # AppUserUpdate | Body for an updateAppUser request.

try: 
    api_response = api_instance.update_app_user(user_id, app_user_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppUserApi->update_app_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

