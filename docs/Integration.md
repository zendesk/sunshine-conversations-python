# Integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The integration ID, generated automatically. | 
**type** | **str** | The integration type. | 
**page_access_token** | **str** | Facebook Page Access Token. Required for *messenger* integrations.  | [optional] 
**app_id** | **str** | Facebook App ID OR WeChat App ID. Required for *messenger* and *wechat* integrations.  | [optional] 
**app_secret** | **str** | Facebook Page App Secret OR WeChat App Secret. Required for *messenger* and *wechat* integrations.  | [optional] 
**webhook_secret** | **str** | Secret to verify webhooks. Returned on successful *wechat* and *messagebird* integrations.  | [optional] 
**page_id** | **str** | Facebook Page App ID. Returned on successful *messenger* integrations.  | [optional] 
**account_sid** | **str** | Twilio Account SID. Required for *twilio* integrations.  | [optional] 
**auth_token** | **str** | Twilio Auth Token. Required for *twilio* integrations.  | [optional] 
**phone_number_sid** | **str** | SID for specific phone number. Required for *twilio* integrations.  | [optional] 
**phone_number** | **str** | Smooch will receive all messages sent to this phone number. Returned on successful *twilio* integrations.  | [optional] 
**name** | **str** | Name on the account. Returned on successful *twilio* integrations.  | [optional] 
**token** | **str** | Telegram Bot Token OR Viber Public Account token. Required for *twilio* and *viber* integrations.  | [optional] 
**uri** | **str** | The viber URI to find the account. Returned on successful *viber* integrations.  | [optional] 
**channel_access_token** | **str** | LINE Channel Access Token. Required for *line* integrations.  | [optional] 
**bot_name** | **str** | The bot&#39;s name. Returned on successful *line* integrations.  | [optional] 
**encoding_aes_key** | **str** | AES Encoding Key. (Optional) Used for *wechat* integrations.  | [optional] 
**from_address** | **str** | Email will display as coming from this address. (Optional) Used for *frontendEmail* integrations.  | [optional] 
**certificate** | **str** | The binary of your APN certificate base64 encoded. Required for *apn* integrations.  | [optional] 
**password** | **str** | The password for your APN certificate. (Optional) Used for *apn* integrations.  | [optional] 
**auto_update_badge** | **bool** | Use the unread count of the conversation as the application badge. (Optional) Used for *apn* integrations.  | [optional] 
**production** | **bool** | Flag specifying whether the certificate is production. Returned on successful *apn* integrations.  | [optional] 
**server_key** | **str** | Your server key from the fcm console. Required for *fcm* integrations.  | [optional] 
**sender_id** | **str** | Your sender id from the fcm console. Required for *fcm* integrations.  | [optional] 
**consumer_key** | **str** | The consumer key for your Twitter app. Required for *twitter* integrations.  | [optional] 
**consumer_secret** | **str** | The consumer secret for your Twitter app. Required for *twitter* integrations.  | [optional] 
**access_token_key** | **str** | The access token key obtained from your user via oauth. Required for *twitter* integrations.  | [optional] 
**access_token_secret** | **str** | The access token secret obtained from your user via oauth. Required for *twitter* integrations.  | [optional] 
**user_id** | **str** | The twitter userId. Returned on successful *twitter* integrations.  | [optional] 
**username** | **str** | The username for the account. Returned on successful *twitter* and *telegram* integrations.  | [optional] 
**api_key** | **str** | The public API key of your Mailgun account. Required for *mailgun* integrations.  | [optional] 
**domain** | **str** | The domain used to relay email. Required for *mailgun* integrations.  | [optional] 
**incoming_address** | **str** | Smooch will receive all emails sent to this address. Required for *mailgun* integrations.  | [optional] 
**access_key** | **str** | The public API key of your MessageBird account. Required for *messagebird* integrations.  | [optional] 
**originator** | **str** | Smooch will receive all messages sent to this phone number. Required for *messagebird* integrations.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


