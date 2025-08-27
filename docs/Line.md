# Line


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 
**type** | **str** | For LINE, each of your customers will need to manually configure a webhook in their LINE configuration page that will point to Sunshine Conversations servers. You must instruct your customers how to configure this manually on their LINE bot page. Once you’ve acquired all the required information, call the Create Integration endpoint. Then, using the returned integration _id, your customer must set the Callback URL field in their LINE Business Center page. The URL should look like the following: &#x60;https://app.smooch.io:443/api/line/webhooks/{appId}/{integrationId}&#x60;.  | [optional] [default to 'line']
**channel_id** | **str** | LINE Channel ID. Can be omitted along with &#x60;channelSecret&#x60; to integrate LINE to setup a webhook before receiving the &#x60;channelId&#x60; and &#x60;channelSecret&#x60; back from LINE. | [optional] 
**channel_secret** | **str** | LINE Channel Secret. Can be omitted along with &#x60;channelId&#x60; to integrate LINE to setup a webhook before receiving the &#x60;channelId&#x60; and &#x60;channelSecret&#x60; back from LINE. | [optional] 
**channel_access_token** | **str** | LINE Channel Access Token. | [optional] 
**service_code** | **str** | LINE Service Code. | [optional] 
**switcher_secret** | **str** | LINE Switcher Secret. | [optional] 
**qr_code_url** | **str** | URL provided by LINE in the [Developer Console](https://developers.line.biz/console/). | [optional] 
**line_id** | **str** | LINE Basic ID. Is automatically set when qrCodeUrl is updated. | [optional] [readonly] 

## Example

```python
from sunshine_conversations_client.model.line import Line

# TODO update the JSON string below
json = "{}"
# create an instance of Line from a JSON string
line_instance = Line.from_json(json)
# print the JSON string representation of the object
print(Line.to_json())

# convert the object into a dict
line_dict = line_instance.to_dict()
# create an instance of Line from a dict
line_from_dict = Line.from_dict(line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


