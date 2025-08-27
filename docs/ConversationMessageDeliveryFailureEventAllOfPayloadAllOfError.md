# ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError

A nested object representing the error associated with the delivery failure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A string representing the error code associated with the error. | [optional] 
**message** | **str** | The description associated with the error. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_message_delivery_failure_event_all_of_payload_all_of_error import ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError from a JSON string
conversation_message_delivery_failure_event_all_of_payload_all_of_error_instance = ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError.to_json())

# convert the object into a dict
conversation_message_delivery_failure_event_all_of_payload_all_of_error_dict = conversation_message_delivery_failure_event_all_of_payload_all_of_error_instance.to_dict()
# create an instance of ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError from a dict
conversation_message_delivery_failure_event_all_of_payload_all_of_error_from_dict = ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError.from_dict(conversation_message_delivery_failure_event_all_of_payload_all_of_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


