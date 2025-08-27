# MatchCriteriaTwilio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The channel type. | [default to 'twilio']
**integration_id** | **str** | The ID of the integration to link. Must match the provided type. | 
**primary** | **bool** | Flag indicating whether the client will become the primary for the target conversation once linking is complete. | [optional] [default to True]
**phone_number** | **str** | The user’s phone number. It must contain the + prefix and the country code. Examples of valid phone numbers: +1 212-555-2368, +12125552368, +1 212 555 2368. Examples of invalid phone numbers: 212 555 2368, 1 212 555 2368.  | 

## Example

```python
from sunshine_conversations_client.model.match_criteria_twilio import MatchCriteriaTwilio

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCriteriaTwilio from a JSON string
match_criteria_twilio_instance = MatchCriteriaTwilio.from_json(json)
# print the JSON string representation of the object
print(MatchCriteriaTwilio.to_json())

# convert the object into a dict
match_criteria_twilio_dict = match_criteria_twilio_instance.to_dict()
# create an instance of MatchCriteriaTwilio from a dict
match_criteria_twilio_from_dict = MatchCriteriaTwilio.from_dict(match_criteria_twilio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


