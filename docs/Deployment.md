# Deployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deployment ID, generated automatically. | 
**status** | **str** | The deployment status. See [**DeploymentStatusEnum**](Enums.md#DeploymentStatusEnum) for available values. | 
**hosting** | **str** | The deployment hosting. See [**DeploymentHostingEnum**](Enums.md#DeploymentHostingEnum) for available values. | 
**base_url** | **str** | The baseUrl of the deployment. Only present for &#x60;self&#x60; hosted deployments. | [optional] 
**username** | **str** | The username of the deployment. Only present for &#x60;self&#x60; hosted deployments. | [optional] 
**phone_number** | **str** | The phoneNumber of the deployment. Only present once the deployment has been registered. | [optional] 
**callback_url** | **str** | The URL to be called by Smooch when the status of the deployment changes. | [optional] 
**callback_secret** | **str** | The secret used to secure the callback. | [optional] 
**integration_id** | **str** | The integrationId of the integration using this deployment. | [optional] 
**app_id** | **str** | The appId of the integration using this deployment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


