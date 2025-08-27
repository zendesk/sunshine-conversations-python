# Referral

Data representing a referral object when a user is referred to a conversation. See the <a href=\"https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/conversation-referrals/\">conversation referrals</a> guide for more details. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The referral’s identifier. | [optional] 
**details** | [**ReferralDetails**](ReferralDetails.md) |  | [optional] 

## Example

```python
from sunshine_conversations_client.model.referral import Referral

# TODO update the JSON string below
json = "{}"
# create an instance of Referral from a JSON string
referral_instance = Referral.from_json(json)
# print the JSON string representation of the object
print(Referral.to_json())

# convert the object into a dict
referral_dict = referral_instance.to_dict()
# create an instance of Referral from a dict
referral_from_dict = Referral.from_dict(referral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


