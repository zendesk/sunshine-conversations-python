# Apple


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | To configure an Apple Messages for Business integration, acquire the required information and call the Create Integration endpoint.  | [optional] [default to 'apple']
**business_id** | **str** | Apple Messages for Business ID. | 
**api_secret** | **str** | Your Apple API secret which is tied to your Messaging Service Provider. | 
**msp_id** | **str** | Your Messaging Service Provider ID. | 
**authentication_message_secret** | **str** | A secret used to create the state value when sending Apple authentication 2.0 messages | [optional] 

## Example

```python
from sunshine_conversations_client.model.apple import Apple

# TODO update the JSON string below
json = "{}"
# create an instance of Apple from a JSON string
apple_instance = Apple.from_json(json)
# print the JSON string representation of the object
print(Apple.to_json())

# convert the object into a dict
apple_dict = apple_instance.to_dict()
# create an instance of Apple from a dict
apple_from_dict = Apple.from_dict(apple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


