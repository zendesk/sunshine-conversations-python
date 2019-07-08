# smooch.ServiceAccountApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_key**](ServiceAccountApi.md#create_secret_key) | **POST** /v1.1/serviceaccounts/{serviceAccountId}/keys | 
[**create_service_account**](ServiceAccountApi.md#create_service_account) | **POST** /v1.1/serviceaccounts | 
[**delete_secret_key**](ServiceAccountApi.md#delete_secret_key) | **DELETE** /v1.1/serviceaccounts/{serviceAccountId}/keys/{keyId} | 
[**delete_service_account**](ServiceAccountApi.md#delete_service_account) | **DELETE** /v1.1/serviceaccounts/{serviceAccountId} | 
[**get_jwt**](ServiceAccountApi.md#get_jwt) | **GET** /v1.1/serviceaccounts/{serviceAccountId}/keys/{keyId}/jwt | 
[**get_secret_key**](ServiceAccountApi.md#get_secret_key) | **GET** /v1.1/serviceaccounts/{serviceAccountId}/keys/{keyId} | 
[**get_service_account**](ServiceAccountApi.md#get_service_account) | **GET** /v1.1/serviceaccounts/{serviceAccountId} | 
[**list_secret_keys**](ServiceAccountApi.md#list_secret_keys) | **GET** /v1.1/serviceaccounts/{serviceAccountId}/keys | 
[**list_service_accounts**](ServiceAccountApi.md#list_service_accounts) | **GET** /v1.1/serviceaccounts | 
[**update_service_account**](ServiceAccountApi.md#update_service_account) | **PUT** /v1.1/serviceaccounts/{serviceAccountId} | 


# **create_secret_key**
> SecretKeyResponse create_secret_key(service_account_id, secret_key_create_body)



Create a secret key for the specified service account.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.
secret_key_create_body = smooch.SecretKeyCreate() # SecretKeyCreate | Body for a createSecretKey request.

try:
    api_response = api_instance.create_secret_key(service_account_id, secret_key_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->create_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 
 **secret_key_create_body** | [**SecretKeyCreate**](SecretKeyCreate.md)| Body for a createSecretKey request. | 

### Return type

[**SecretKeyResponse**](SecretKeyResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account**
> ServiceAccountResponse create_service_account(service_account_create_body)



Create a new service account.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_create_body = smooch.ServiceAccountCreate() # ServiceAccountCreate | Body for a createServiceAccount request.

try:
    api_response = api_instance.create_service_account(service_account_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->create_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_create_body** | [**ServiceAccountCreate**](ServiceAccountCreate.md)| Body for a createServiceAccount request. | 

### Return type

[**ServiceAccountResponse**](ServiceAccountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_key**
> delete_secret_key(service_account_id, key_id)



Delete the specified service account secret key.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_instance.delete_secret_key(service_account_id, key_id)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->delete_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_account**
> delete_service_account(service_account_id)



Delete the specified service account.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.

try:
    api_instance.delete_service_account(service_account_id)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->delete_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwt**
> JwtResponse get_jwt(service_account_id, key_id)



Get an account-scoped JWT for the specified service account secret key.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_response = api_instance.get_jwt(service_account_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->get_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_key**
> SecretKeyResponse get_secret_key(service_account_id, key_id)



Get the specified service account secret key.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.
key_id = 'key_id_example' # str | Identifies the secret key.

try:
    api_response = api_instance.get_secret_key(service_account_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->get_secret_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 
 **key_id** | **str**| Identifies the secret key. | 

### Return type

[**SecretKeyResponse**](SecretKeyResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_account**
> ServiceAccountResponse get_service_account(service_account_id)



Get the specified service account.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.

try:
    api_response = api_instance.get_service_account(service_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->get_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 

### Return type

[**ServiceAccountResponse**](ServiceAccountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secret_keys**
> ListSecretKeysResponse list_secret_keys(service_account_id)



List the secret keys for the specified service account.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.

try:
    api_response = api_instance.list_secret_keys(service_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->list_secret_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 

### Return type

[**ListSecretKeysResponse**](ListSecretKeysResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_accounts**
> ListServiceAccountsResponse list_service_accounts(limit=limit, offset=offset)



List all service accounts configured.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
limit = 25 # int | The number of records to return. (optional) (default to 25)
offset = 0 # int | The number of initial records to skip before picking records to return. (optional) (default to 0)

try:
    api_response = api_instance.list_service_accounts(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->list_service_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return. | [optional] [default to 25]
 **offset** | **int**| The number of initial records to skip before picking records to return. | [optional] [default to 0]

### Return type

[**ListServiceAccountsResponse**](ListServiceAccountsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> ServiceAccountResponse update_service_account(service_account_id, service_account_update_body)



Update the specified service account.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint


# OR

# Configure API key authorization (alternative): jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.ServiceAccountApi()
service_account_id = 'service_account_id_example' # str | Identifies the service account.
service_account_update_body = smooch.ServiceAccountUpdate() # ServiceAccountUpdate | Body for an updateServiceAccount request.

try:
    api_response = api_instance.update_service_account(service_account_id, service_account_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAccountApi->update_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**| Identifies the service account. | 
 **service_account_update_body** | [**ServiceAccountUpdate**](ServiceAccountUpdate.md)| Body for an updateServiceAccount request. | 

### Return type

[**ServiceAccountResponse**](ServiceAccountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

