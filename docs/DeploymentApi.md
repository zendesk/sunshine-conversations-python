# smooch.DeploymentApi

All URIs are relative to *https://api.smooch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_phone_number**](DeploymentApi.md#activate_phone_number) | **POST** /v1.1/whatsapp/deployments/{deploymentId}/activate | 
[**confirm_code**](DeploymentApi.md#confirm_code) | **POST** /v1.1/whatsapp/deployments/{deploymentId}/code/confirm | 
[**create_deployment**](DeploymentApi.md#create_deployment) | **POST** /v1.1/whatsapp/deployments | 
[**delete_deployment**](DeploymentApi.md#delete_deployment) | **DELETE** /v1.1/whatsapp/deployments/{deploymentId} | 
[**get_deployment**](DeploymentApi.md#get_deployment) | **GET** /v1.1/whatsapp/deployments/{deploymentId} | 
[**list_deployments**](DeploymentApi.md#list_deployments) | **GET** /v1.1/whatsapp/deployments | 


# **activate_phone_number**
> DeploymentResponse activate_phone_number(deployment_id, deployment_activate_phone_number_body)



Activate a phone number on the specified deployment.

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
api_instance = smooch.DeploymentApi()
deployment_id = 'deployment_id_example' # str | Identifies the deployment.
deployment_activate_phone_number_body = smooch.DeploymentActivatePhoneNumber() # DeploymentActivatePhoneNumber | Body for an activatePhoneNumber request. 

try:
    api_response = api_instance.activate_phone_number(deployment_id, deployment_activate_phone_number_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->activate_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Identifies the deployment. | 
 **deployment_activate_phone_number_body** | [**DeploymentActivatePhoneNumber**](DeploymentActivatePhoneNumber.md)| Body for an activatePhoneNumber request.  | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_code**
> DeploymentResponse confirm_code(deployment_id, deployment_confirm_code)



Confirm code to complete phone number activation.

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
api_instance = smooch.DeploymentApi()
deployment_id = 'deployment_id_example' # str | Identifies the deployment.
deployment_confirm_code = smooch.DeploymentConfirmCode() # DeploymentConfirmCode | Body for a confirmCode request. 

try:
    api_response = api_instance.confirm_code(deployment_id, deployment_confirm_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->confirm_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Identifies the deployment. | 
 **deployment_confirm_code** | [**DeploymentConfirmCode**](DeploymentConfirmCode.md)| Body for a confirmCode request.  | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment**
> DeploymentResponse create_deployment(deployment_create_body)



Create a WhatsApp deployment.

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
api_instance = smooch.DeploymentApi()
deployment_create_body = smooch.DeploymentCreate() # DeploymentCreate | Body for a createDeployment request. 

try:
    api_response = api_instance.create_deployment(deployment_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_create_body** | [**DeploymentCreate**](DeploymentCreate.md)| Body for a createDeployment request.  | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment**
> delete_deployment(deployment_id)



Delete the specified deployment.

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
api_instance = smooch.DeploymentApi()
deployment_id = 'deployment_id_example' # str | Identifies the deployment.

try:
    api_instance.delete_deployment(deployment_id)
except ApiException as e:
    print("Exception when calling DeploymentApi->delete_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Identifies the deployment. | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> DeploymentResponse get_deployment(deployment_id)



Get the specified deployment.

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
api_instance = smooch.DeploymentApi()
deployment_id = 'deployment_id_example' # str | Identifies the deployment.

try:
    api_response = api_instance.get_deployment(deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| Identifies the deployment. | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> ListDeploymentsResponse list_deployments()



List owned WhatsApp deployments.

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
api_instance = smooch.DeploymentApi()

try:
    api_response = api_instance.list_deployments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->list_deployments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDeploymentsResponse**](ListDeploymentsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

