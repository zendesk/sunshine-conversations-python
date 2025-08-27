# Whatsapp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | To configure a WhatsApp integration, use your WhatsApp API Client connection information. Sunshine Conversations can provide WhatsApp API Client hosting for approved brands. See our [WhatsApp guide](https://docs.smooch.io/guide/whatsapp/#whatsapp-api-client) for more details on WhatsApp API Client hosting.  | [optional] [default to 'whatsapp']
**hsm_fallback_language** | **str** | Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info. | [optional] [default to 'en_US']
**account_id** | **str** | The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction. | [optional] 
**account_management_access_token** | **str** | An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction. | [optional] 
**phone_number** | **str** | The phone number that is associated with the deployment of this integration, if one exists. | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.whatsapp import Whatsapp

# TODO update the JSON string below
json = "{}"
# create an instance of Whatsapp from a JSON string
whatsapp_instance = Whatsapp.from_json(json)
# print the JSON string representation of the object
print(Whatsapp.to_json())

# convert the object into a dict
whatsapp_dict = whatsapp_instance.to_dict()
# create an instance of Whatsapp from a dict
whatsapp_from_dict = Whatsapp.from_dict(whatsapp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


