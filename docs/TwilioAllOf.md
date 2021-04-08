# TwilioAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | To configure a Twilio integration, acquire the required information from the user and call the Create Integration endpoint.  | [optional] [default to 'twilio']
**account_sid** | **str** | Twilio Account SID. | 
**auth_token** | **str** | Twilio Auth Token. | 
**phone_number_sid** | **str** | SID for specific phone number. One of &#x60;messagingServiceSid&#x60; or &#x60;phoneNumberSid&#x60; must be provided when creating a Twilio integration. | [optional] 
**messaging_service_sid** | **str** | SID for specific messaging service. One of &#x60;messagingServiceSid&#x60; or &#x60;phoneNumberSid&#x60; must be provided when creating a Twilio integration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


