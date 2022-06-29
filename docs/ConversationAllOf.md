# ConversationAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | Whether the conversation is the default conversation for the user. Will be true for the first personal conversation created for the user, and false in all other cases.  | [optional] 
**display_name** | **str** | A friendly name for the conversation, may be displayed to the business or the user.  | [optional] 
**description** | **str** | A short text describing the conversation. | [optional] 
**icon_url** | **str** | A custom conversation icon url. The image must be in either JPG, PNG, or GIF format | [optional] 
**business_last_read** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the conversation was last marked as read with role business.  | [optional] 
**last_updated_at** | **str** | A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the last message was received in the conversation, or the creation time if no messages have been received yet.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


