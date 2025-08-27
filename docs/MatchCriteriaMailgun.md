# MatchCriteriaMailgun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The channel type. | [default to 'mailgun']
**integration_id** | **str** | The ID of the integration to link. Must match the provided type. | 
**primary** | **bool** | Flag indicating whether the client will become the primary for the target conversation once linking is complete. | [optional] [default to True]
**address** | **str** | The user’s email address. | 
**subject** | **str** | May be specified to set the subject for the outgoing email. | [optional] [default to 'New message from {appName}']

## Example

```python
from sunshine_conversations_client.model.match_criteria_mailgun import MatchCriteriaMailgun

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCriteriaMailgun from a JSON string
match_criteria_mailgun_instance = MatchCriteriaMailgun.from_json(json)
# print the JSON string representation of the object
print(MatchCriteriaMailgun.to_json())

# convert the object into a dict
match_criteria_mailgun_dict = match_criteria_mailgun_instance.to_dict()
# create an instance of MatchCriteriaMailgun from a dict
match_criteria_mailgun_from_dict = MatchCriteriaMailgun.from_dict(match_criteria_mailgun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


