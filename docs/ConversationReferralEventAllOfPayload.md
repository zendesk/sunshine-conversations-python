# ConversationReferralEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation a user lands in after being referred. See the &lt;a href&#x3D;\&quot;https://docs.smooch.io/guide/conversation-referrals/\&quot;&gt;conversation referrals&lt;/a&gt; guide for more details. | [optional] 
**user** | [**User2**](User2.md) | The user associated with the conversation. | [optional] 
**source** | [**SourceWithCampaignWebhook**](SourceWithCampaignWebhook.md) | The source of the referral. | [optional] 
**referral** | [**Referral**](Referral.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


