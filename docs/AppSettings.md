# AppSettings

Customizable app settings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_retention_seconds** | **int** | Number of seconds of inactivity before a conversation’s messages  will be automatically deleted. See  [Conversation Retention Seconds](https://docs.smooch.io/guide/creating-and-managing-apps/#conversation-retention-seconds) for more information.  | [optional] 
**mask_credit_card_numbers** | **bool** | A boolean specifying whether credit card numbers should be masked  when sent through Sunshine Conversations.  | [optional] 
**use_animal_names** | **bool** | A boolean specifying whether animal names should be used for  unnamed users. See the  [user naming guide](https://docs.smooch.io/guide/receiving-messages/#message-author-name) for details.  | [optional] 
**echo_postback** | **bool** | A boolean specifying whether a message should be added to the conversation  history when a postback button is clicked. See  [Echo Postbacks](https://docs.smooch.io/guide/creating-and-managing-apps/#echo-postbacks) for more information.  | [optional] 
**ignore_auto_conversation_start** | **bool** | A boolean specifying whether a non message event coming from a channel will  trigger a  [start conversation](https://docs.smooch.io/rest/#section/Webhook-Triggers) event and count as a monthly active user (MAU). &lt;aside class&#x3D;\&quot;notice\&quot;&gt;Calling &lt;code&gt;startConversation()&lt;/code&gt; (or equivalent) from the Android,  iOS or Web SDK will count as a MAU, regardless of the value of this setting.&lt;/aside&gt;  | [optional] 
**multi_convo_enabled** | **bool** | A boolean specifying whether users are allowed to be part of several conversations. Enabling &#x60;multiConvo&#x60; is **irreversible**.  | [optional] 
**attachments_access** | **str** | A string specifying whether attachments should be stored in a publicly or privately accessible cloud storage. attachmentsAccess is set to public by default but can be modified to private. See &lt;a href&#x3D;\&quot;https://docs.smooch.io/guide/private-attachments/\&quot;&gt;Private Attachments&lt;/a&gt; for more information.  | [optional] 
**attachments_token_expiration_seconds** | **int** | Number of seconds representing the expiration time of the generated media tokens for private attachments. The JWT will be valid for 2 hours by default. See See &lt;a href&#x3D;\&quot;https://docs.smooch.io/guide/private-attachments/\&quot;&gt;Private Attachments&lt;/a&gt; for more information.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


