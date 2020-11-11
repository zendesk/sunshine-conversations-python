# MessagebirdAllOf

To configure a MessageBird integration, acquire the accessKey, the signingKey and the MessageBird number you would like to use, then call the Create Integration endpoint. The response will include the integration’s _id and webhookSecret, which must be used to configure the webhook in MessageBird. In the Flow Builder for the MessageBird number you’ve used to integrate, add a new step with the following settings: * Create a new Call HTTP endpoint with SMS flow. * Select your desired SMS number for Incoming SMS. * Click on Forward to URL and set its method to POST. * Then, using the integration _id and webhookSecret returned from the create integration call, enter the following into the URL field:  `https://app.smooch.io/api/messagebird/webhooks/{appId}/{integrationId}/{webhookSecret}` * Select application/json for the Set Content-Type header field. * Save and publish your changes. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of integration. | [optional] [default to 'messagebird']
**access_key** | **str** | The public API key of your MessageBird account. | 
**signing_key** | **str** | The signing key of your MessageBird account. Used to validate the webhooks&#39; origin. | 
**originator** | **str** | Sunshine Conversations will receive all messages sent to this phone number. | 
**webhook_secret** | **str** | The secret that is used to configure webhooks in MessageBird. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


