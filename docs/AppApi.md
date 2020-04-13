# smooch.AppApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppApi.md#create_app) | **POST** /v1.1/apps | 
[**create_secret_key**](AppApi.md#create_secret_key) | **POST** /v1.1/apps/{appId}/keys | 
[**delete_app**](AppApi.md#delete_app) | **DELETE** /v1.1/apps/{appId} | 
[**delete_secret_key**](AppApi.md#delete_secret_key) | **DELETE** /v1.1/apps/{appId}/keys/{keyId} | 
[**get_app**](AppApi.md#get_app) | **GET** /v1.1/apps/{appId} | 
[**get_app_jwt**](AppApi.md#get_app_jwt) | **GET** /v1.1/apps/{appId}/keys/{keyId}/jwt | 
[**get_sdk_ids**](AppApi.md#get_sdk_ids) | **GET** /v1.1/apps/{appId}/sdks | 
[**get_secret_key**](AppApi.md#get_secret_key) | **GET** /v1.1/apps/{appId}/keys/{keyId} | 
[**list_apps**](AppApi.md#list_apps) | **GET** /v1.1/apps | 
[**list_secret_keys**](AppApi.md#list_secret_keys) | **GET** /v1.1/apps/{appId}/keys | 
[**update_app**](AppApi.md#update_app) | **PUT** /v1.1/apps/{appId} | 


# **create_app**
> AppResponse create_app(app_create_body)



Create a new app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_create_body = smooch.AppCreate() # AppCreate | Body for a createApp request.

try:
    api_response = api_instance.create_app(app_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_create_body** | [**AppCreate**](AppCreate.md)| Body for a createApp request. | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret_key**
> SecretKeyResponse create_secret_key(app_id, secret_key_create_body)



Create a secret key for the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
secret_key_create_body = smooch.SecretKeyCreate() # SecretKeyCreate | Body for a createSecretKey request.

try:
    api_response = api_instance.create_secret_key(app_id, secret_key_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->create_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **secret_key_create_body** | [**SecretKeyCreate**](SecretKeyCreate.md)| Body for a createSecretKey request. | 

### Return type

[**SecretKeyResponse**](SecretKeyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> delete_app(app_id)



Delete the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_instance.delete_app(app_id)
except ApiException as e:
    print("Exception when calling AppApi->delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_key**
> delete_secret_key(app_id, key_id)



Delete the specified secret key.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_instance.delete_secret_key(app_id, key_id)
except ApiException as e:
    print("Exception when calling AppApi->delete_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> AppResponse get_app(app_id)



Get the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.get_app(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_jwt**
> JwtResponse get_app_jwt(app_id, key_id)



Get an app-scoped JWT for the specified secret key.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_response = api_instance.get_app_jwt(app_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_app_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdk_ids**
> GetSdkIdsResponse get_sdk_ids(app_id)



Retrieve the IDs of the three SDK integrations (`android`, `ios`, and `web`) for the specified app, to be used when initializing the SDKs.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.get_sdk_ids(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_sdk_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**GetSdkIdsResponse**](GetSdkIdsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_key**
> SecretKeyResponse get_secret_key(app_id, key_id)



Get the specified secret key.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_response = api_instance.get_secret_key(app_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

[**SecretKeyResponse**](SecretKeyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> ListAppsResponse list_apps(limit=limit, offset=offset, service_account_id=service_account_id)



List all apps configured.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
limit = 25 # int | The number of records to return. (optional) (default to 25)
offset = 0 # int | The number of initial records to skip before picking records to return. (optional) (default to 0)
service_account_id = '' # str | The service account ID for which to list apps. (optional) (default to )

try:
    api_response = api_instance.list_apps(limit=limit, offset=offset, service_account_id=service_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return. | [optional] [default to 25]
 **offset** | **int**| The number of initial records to skip before picking records to return. | [optional] [default to 0]
 **service_account_id** | **str**| The service account ID for which to list apps. | [optional] [default to ]

### Return type

[**ListAppsResponse**](ListAppsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secret_keys**
> ListSecretKeysResponse list_secret_keys(app_id)



List the secret keys for the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.list_secret_keys(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->list_secret_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**ListSecretKeysResponse**](ListSecretKeysResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> AppResponse update_app(app_id, app_update_body)



Update the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# Configure HTTP basic authorization (recommended): basicAuth
smooch.configuration.username = 'API_KEY_ID'
smooch.configuration.password = 'API_KEY_SECRET'

# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.AppApi()
app_id = 'app_id_example' # str | Identifies the app.
app_update_body = smooch.AppUpdate() # AppUpdate | Body for an updateApp request.

try:
    api_response = api_instance.update_app(app_id, app_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **app_update_body** | [**AppUpdate**](AppUpdate.md)| Body for an updateApp request. | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

