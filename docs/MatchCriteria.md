# MatchCriteria

The set of criteria used to determine the user's identity on a third-party channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The channel type. | [default to 'whatsapp']
**integration_id** | **str** | The ID of the integration to link. Must match the provided type. | 
**primary** | **bool** | Flag indicating whether the client will become the primary for the target conversation once linking is complete. | [optional] [default to True]
**address** | **str** | The user’s email address. | 
**subject** | **str** | May be specified to set the subject for the outgoing email. | [optional] [default to 'New message from {appName}']
**phone_number** | **str** | The user’s phone number. It must contain the + prefix and the country code. Examples of valid phone numbers: +1 212-555-2368, +12125552368, +1 212 555 2368. Examples of invalid phone numbers: 212 555 2368, 1 212 555 2368.  | 

## Example

```python
from sunshine_conversations_client.model.match_criteria import MatchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCriteria from a JSON string
match_criteria_instance = MatchCriteria.from_json(json)
# print the JSON string representation of the object
print(MatchCriteria.to_json())

# convert the object into a dict
match_criteria_dict = match_criteria_instance.to_dict()
# create an instance of MatchCriteria from a dict
match_criteria_from_dict = MatchCriteria.from_dict(match_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


