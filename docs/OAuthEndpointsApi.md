# sunshine_conversations_client.OAuthEndpointsApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](OAuthEndpointsApi.md#authorize) | **GET** /oauth/authorize | Authorize
[**get_token**](OAuthEndpointsApi.md#get_token) | **POST** /oauth/token | Get Token
[**get_token_info**](OAuthEndpointsApi.md#get_token_info) | **GET** /v2/tokenInfo | Get Token Info
[**revoke_access**](OAuthEndpointsApi.md#revoke_access) | **DELETE** /oauth/authorization | Revoke Access


# **authorize**
> authorize(client_id, response_type, state=state, redirect_uri=redirect_uri)

Authorize

This endpoint begins the OAuth flow. It relies on a browser session for authentication.
If the user is not logged in to Zendesk they will be redirected to the login page. 
If the user has many Zendesk accounts, they will first be prompted to select the one 
they wish to integrate with. They will then be presented with an Allow/Deny dialog, 
describing details of the access your integration is requesting.

Use `oauth-bridge.zendesk.com/sc` as the base URL when redirecting the user to this endpoint.

```
https://oauth-bridge.zendesk.com/sc/oauth/authorize?response_type=code&client_id={client_id}
```


### Example


```python
import sunshine_conversations_client
from sunshine_conversations_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smooch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sunshine_conversations_client.Configuration(
    host = "https://api.smooch.io"
)


# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.OAuthEndpointsApi(api_client)
    client_id = '5e4af71a81966cfff3ef6550' # str | Your integration’s unique identifier
    response_type = 'code' # str | For now the only acceptable value is code.
    state = 'Pending' # str | You may pass in any arbitrary string value here which will be returned to you along with the code via browser redirect. (optional)
    redirect_uri = 'https://example.org' # str | You may pass in a redirect_uri to determine which URI the response is redirected to. This URI must be contained in the list configured by your integration. If this option is not passed, the first URI present in the list will be used. (optional)

    try:
        # Authorize
        api_instance.authorize(client_id, response_type, state=state, redirect_uri=redirect_uri)
    except Exception as e:
        print("Exception when calling OAuthEndpointsApi->authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Your integration’s unique identifier | 
 **response_type** | **str**| For now the only acceptable value is code. | 
 **state** | **str**| You may pass in any arbitrary string value here which will be returned to you along with the code via browser redirect. | [optional] 
 **redirect_uri** | **str**| You may pass in a redirect_uri to determine which URI the response is redirected to. This URI must be contained in the list configured by your integration. If this option is not passed, the first URI present in the list will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> GetToken200Response get_token(get_token_request)

Get Token

This endpoint is used to exchange an authorization code for an access token. 
It should only be used in server-to-server calls.

Use `oauth-bridge.zendesk.com/sc` as the base URL when invoking this endpoint.

```
POST https://oauth-bridge.zendesk.com/sc/oauth/token
```


### Example


```python
import sunshine_conversations_client
from sunshine_conversations_client.models.get_token200_response import GetToken200Response
from sunshine_conversations_client.models.get_token_request import GetTokenRequest
from sunshine_conversations_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smooch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sunshine_conversations_client.Configuration(
    host = "https://api.smooch.io"
)


# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.OAuthEndpointsApi(api_client)
    get_token_request = sunshine_conversations_client.GetTokenRequest() # GetTokenRequest | 

    try:
        # Get Token
        api_response = api_instance.get_token(get_token_request)
        print("The response of OAuthEndpointsApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthEndpointsApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_token_request** | [**GetTokenRequest**](GetTokenRequest.md)|  | 

### Return type

[**GetToken200Response**](GetToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_info**
> AppResponse get_token_info()

Get Token Info

This endpoint can be used to retrieve the app linked to the OAuth token. Typically used after receiving an access
token via OAuth, in order to retrieve the app's `id` and `subdomain` to be used in future calls. May also be used
to confirm that the credentials are still valid.

Use `oauth-bridge.zendesk.com/sc` as the base URL when invoking this endpoint.

```
GET https://oauth-bridge.zendesk.com/sc/v2/tokenInfo
```


### Example


```python
import sunshine_conversations_client
from sunshine_conversations_client.models.app_response import AppResponse
from sunshine_conversations_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smooch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sunshine_conversations_client.Configuration(
    host = "https://api.smooch.io"
)


# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.OAuthEndpointsApi(api_client)

    try:
        # Get Token Info
        api_response = api_instance.get_token_info()
        print("The response of OAuthEndpointsApi->get_token_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthEndpointsApi->get_token_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_access**
> object revoke_access()

Revoke Access

This endpoint is used to revoke your integration's access to the user's app. Revoking access means your integration will no longer be able to interact with the app, and any webhooks the integration had previously configured will be removed. 
Calling this endpoint is equivalent to the user removing your integration manually. Your integration's `removeUrl` (if configured) will also be called when an integration is removed in this way.


### Example

* Basic Authentication (basicAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
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
    api_instance = sunshine_conversations_client.OAuthEndpointsApi(api_client)

    try:
        # Revoke Access
        api_response = api_instance.revoke_access()
        print("The response of OAuthEndpointsApi->revoke_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthEndpointsApi->revoke_access: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

