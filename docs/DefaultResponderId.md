# DefaultResponderId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 

## Example

```python
from sunshine_conversations_client.model.default_responder_id import DefaultResponderId

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultResponderId from a JSON string
default_responder_id_instance = DefaultResponderId.from_json(json)
# print the JSON string representation of the object
print(DefaultResponderId.to_json())

# convert the object into a dict
default_responder_id_dict = default_responder_id_instance.to_dict()
# create an instance of DefaultResponderId from a dict
default_responder_id_from_dict = DefaultResponderId.from_dict(default_responder_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


