# TwitterUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human-friendly name used to identify the integration. &#x60;displayName&#x60; can be unset by changing it to &#x60;null&#x60;. | [optional] 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.twitter_update import TwitterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterUpdate from a JSON string
twitter_update_instance = TwitterUpdate.from_json(json)
# print the JSON string representation of the object
print(TwitterUpdate.to_json())

# convert the object into a dict
twitter_update_dict = twitter_update_instance.to_dict()
# create an instance of TwitterUpdate from a dict
twitter_update_from_dict = TwitterUpdate.from_dict(twitter_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


