# AppSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask_credit_card_numbers** | **bool** | Flag specifying whether credit card numbers will be automatically masked if sent through Smooch. | [optional] 
**use_animal_names** | **bool** | Flag specifying whether animal names should be used for anonymous users. | [optional] 
**conversation_retention_seconds** | **int** | Number of seconds of inactivity before a conversation’s messages will be automatically deleted. | [optional] 
**echo_postback** | **bool** | A boolean specifying whether a message should be added to the conversation history when a postback button is clicked. | [optional] 
**ignore_auto_conversation_start** | **bool** | A boolean specifying whether a non message event coming from a social channel will trigger a start conversation event and count as an active user conversation (AUC).&lt;br&gt;**Note:** Calling *startConversation()* (or equivalent) from the Android-, iOS- or Web-SDK will count as an AUC, regardless of the value of this setting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


