# smooch.WebhookApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /v1.1/apps/{appId}/webhooks | 
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /v1.1/apps/{appId}/webhooks/{webhookId} | 
[**get_webhook**](WebhookApi.md#get_webhook) | **GET** /v1.1/apps/{appId}/webhooks/{webhookId} | 
[**list_webhooks**](WebhookApi.md#list_webhooks) | **GET** /v1.1/apps/{appId}/webhooks | 
[**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /v1.1/apps/{appId}/webhooks/{webhookId} | 


# **create_webhook**
> WebhookResponse create_webhook(app_id, webhook_create_body)



Create a webhook for the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.WebhookApi()
app_id = 'app_id_example' # str | Identifies the app.
webhook_create_body = smooch.WebhookCreate() # WebhookCreate | Body for a createWebhook request. 

try:
    api_response = api_instance.create_webhook(app_id, webhook_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **webhook_create_body** | [**WebhookCreate**](WebhookCreate.md)| Body for a createWebhook request.  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(app_id, webhook_id)



Delete the specified webhook.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.WebhookApi()
app_id = 'app_id_example' # str | Identifies the app.
webhook_id = 'webhook_id_example' # str | Identifies the webhook.

try:
    api_instance.delete_webhook(app_id, webhook_id)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **webhook_id** | **str**| Identifies the webhook. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> WebhookResponse get_webhook(app_id, webhook_id)



Get the specified webhook.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.WebhookApi()
app_id = 'app_id_example' # str | Identifies the app.
webhook_id = 'webhook_id_example' # str | Identifies the webhook.

try:
    api_response = api_instance.get_webhook(app_id, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **webhook_id** | **str**| Identifies the webhook. | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> ListWebhooksResponse list_webhooks(app_id)



List webhooks for the specified app.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.WebhookApi()
app_id = 'app_id_example' # str | Identifies the app.

try:
    api_response = api_instance.list_webhooks(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->list_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookResponse update_webhook(app_id, webhook_id, webhook_update_body)



Update the specified webhook.

### Example
```python
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_JWT'
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = smooch.WebhookApi()
app_id = 'app_id_example' # str | Identifies the app.
webhook_id = 'webhook_id_example' # str | Identifies the webhook.
webhook_update_body = smooch.WebhookUpdate() # WebhookUpdate | Body for an updateWebhook request. 

try:
    api_response = api_instance.update_webhook(app_id, webhook_id, webhook_update_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Identifies the app. | 
 **webhook_id** | **str**| Identifies the webhook. | 
 **webhook_update_body** | [**WebhookUpdate**](WebhookUpdate.md)| Body for an updateWebhook request.  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

