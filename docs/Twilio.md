# Twilio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | To configure a Twilio integration, acquire the required information from the user and call the Create Integration endpoint.  | [optional] [default to 'twilio']
**account_sid** | **str** | Twilio Account SID. | 
**auth_token** | **str** | Twilio Auth Token. | 
**phone_number_sid** | **str** | SID for specific phone number. One of &#x60;messagingServiceSid&#x60; or &#x60;phoneNumberSid&#x60; must be provided when creating a Twilio integration. | [optional] 
**messaging_service_sid** | **str** | SID for specific messaging service. One of &#x60;messagingServiceSid&#x60; or &#x60;phoneNumberSid&#x60; must be provided when creating a Twilio integration. | [optional] 

## Example

```python
from sunshine_conversations_client.model.twilio import Twilio

# TODO update the JSON string below
json = "{}"
# create an instance of Twilio from a JSON string
twilio_instance = Twilio.from_json(json)
# print the JSON string representation of the object
print(Twilio.to_json())

# convert the object into a dict
twilio_dict = twilio_instance.to_dict()
# create an instance of Twilio from a dict
twilio_from_dict = Twilio.from_dict(twilio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


