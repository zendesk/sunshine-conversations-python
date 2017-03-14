# smooch.InitApi

All URIs are relative to *https://api.smooch.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**init**](InitApi.md#init) | **POST** /init | 


# **init**
> InitResponse init(init_body)



This API is called by an iOS, Android, or browser client when the app is first loaded. It serves a number of purposes. 1. Initializes a new *appUser* and *client* if they don’t yet exist. 2. Updates an existing app user’s profile and client information. 3. Authenticates the *appUser* if *jwt* credentials are provided. 

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
api_instance = smooch.InitApi()
init_body = smooch.Init() # Init | Body for an init request.

try: 
    api_response = api_instance.init(init_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InitApi->init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **init_body** | [**Init**](Init.md)| Body for an init request. | 

### Return type

[**InitResponse**](InitResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

