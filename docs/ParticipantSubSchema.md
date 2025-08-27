# ParticipantSubSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The id of the user that will be participating in the conversation. It will return &#x60;404&#x60; if the user can’t be found. One of &#x60;userId&#x60; or &#x60;userExternalId&#x60; is required, but not both. | [optional] 
**subscribe_sdk_client** | **bool** | When passed as true, the SDK client of the concerned participant will be subscribed to the conversation. The user will start receiving push notifications for this conversation right away, without having to view the conversation on the SDK beforehand. An SDK client will be created for users that don’t already have one. This field is required if the conversation is of type &#x60;sdkGroup&#x60;. | [optional] 
**user_external_id** | **str** | The &#x60;externalId&#x60; of the user that will be participating in the conversation. It will return &#x60;404&#x60; if the user can’t be found. One of &#x60;userId&#x60; or &#x60;userExternalId&#x60; is required, but not both. | [optional] 

## Example

```python
from sunshine_conversations_client.model.participant_sub_schema import ParticipantSubSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantSubSchema from a JSON string
participant_sub_schema_instance = ParticipantSubSchema.from_json(json)
# print the JSON string representation of the object
print(ParticipantSubSchema.to_json())

# convert the object into a dict
participant_sub_schema_dict = participant_sub_schema_instance.to_dict()
# create an instance of ParticipantSubSchema from a dict
participant_sub_schema_from_dict = ParticipantSubSchema.from_dict(participant_sub_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


