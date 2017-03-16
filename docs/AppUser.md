# AppUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The app user&#39;s ID, generated automatically. | 
**user_id** | **str** | The app user&#39;s userId. This ID is specified by the appMaker.  | [optional] 
**given_name** | **str** | The app user&#39;s given name. | [optional] 
**surname** | **str** | The app user&#39;s surname. | [optional] 
**email** | **str** | The app user&#39;s email. | [optional] 
**signed_up_at** | **str** | A datetime string with the format *yyyy-mm-ddThh:mm:ssZ* representing the moment an appUser was created. | [optional] 
**properties** | **object** | Custom properties for the app user. | 
**conversation_started** | **bool** | Flag indicating if the conversation has started for the app user. | 
**credential_required** | **bool** | Flag indicating if the appUser is secured by a JSON Web Token or not. | [optional] 
**clients** | [**list[Client]**](Client.md) | List of clients associated with the app user. | [optional] 
**pending_clients** | [**list[Client]**](Client.md) | As clients, but containing linked clients which have not been confirmed yet (i.e. Twilio SMS). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


