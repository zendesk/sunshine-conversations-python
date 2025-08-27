# ReferralDetails

Nested object containing additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The source of the referral - MESSENGER_CODE, ADS etc… | [optional] 
**type** | **str** | The type of referral, typically OPEN-THREAD. | [optional] 
**ad_id** | **str** | If the referral came from an ad, this field will be present with the ad’s Id. | [optional] 

## Example

```python
from sunshine_conversations_client.model.referral_details import ReferralDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReferralDetails from a JSON string
referral_details_instance = ReferralDetails.from_json(json)
# print the JSON string representation of the object
print(ReferralDetails.to_json())

# convert the object into a dict
referral_details_dict = referral_details_instance.to_dict()
# create an instance of ReferralDetails from a dict
referral_details_from_dict = ReferralDetails.from_dict(referral_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


