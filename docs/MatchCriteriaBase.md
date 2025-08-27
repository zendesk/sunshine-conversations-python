# MatchCriteriaBase

The set of criteria used to determine the user's identity on a third-party channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The channel type. | 
**integration_id** | **str** | The ID of the integration to link. Must match the provided type. | 
**primary** | **bool** | Flag indicating whether the client will become the primary for the target conversation once linking is complete. | [optional] [default to True]

## Example

```python
from sunshine_conversations_client.model.match_criteria_base import MatchCriteriaBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatchCriteriaBase from a JSON string
match_criteria_base_instance = MatchCriteriaBase.from_json(json)
# print the JSON string representation of the object
print(MatchCriteriaBase.to_json())

# convert the object into a dict
match_criteria_base_dict = match_criteria_base_instance.to_dict()
# create an instance of MatchCriteriaBase from a dict
match_criteria_base_from_dict = MatchCriteriaBase.from_dict(match_criteria_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


