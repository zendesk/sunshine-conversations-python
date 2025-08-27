# ConversationReferralEventAllOfPayload

The payload of the event. The contents of this object depend on the type of event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ConversationTruncated**](ConversationTruncated.md) | The conversation a user lands in after being referred. See the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/conversation-referrals/\&quot;&gt;conversation referrals&lt;/a&gt; guide for more details. | [optional] 
**user** | [**User**](User.md) | The user associated with the conversation. | [optional] 
**source** | [**SourceWithCampaignWebhook**](SourceWithCampaignWebhook.md) | The source of the referral. | [optional] 
**referral** | [**Referral**](Referral.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_referral_event_all_of_payload import ConversationReferralEventAllOfPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationReferralEventAllOfPayload from a JSON string
conversation_referral_event_all_of_payload_instance = ConversationReferralEventAllOfPayload.from_json(json)
# print the JSON string representation of the object
print(ConversationReferralEventAllOfPayload.to_json())

# convert the object into a dict
conversation_referral_event_all_of_payload_dict = conversation_referral_event_all_of_payload_instance.to_dict()
# create an instance of ConversationReferralEventAllOfPayload from a dict
conversation_referral_event_all_of_payload_from_dict = ConversationReferralEventAllOfPayload.from_dict(conversation_referral_event_all_of_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


