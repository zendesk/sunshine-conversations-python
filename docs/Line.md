# Line

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | For LINE, each of your customers will need to manually configure a webhook in their LINE configuration page that will point to Sunshine Conversations servers. You must instruct your customers how to configure this manually on their LINE bot page. Once you’ve acquired all the required information, call the Create Integration endpoint. Then, using the returned integration _id, your customer must set the Callback URL field in their LINE Business Center page. The URL should look like the following: &#x60;https://app.smooch.io:443/api/line/webhooks/{appId}/{integrationId}&#x60;.  | [optional] [default to 'line']
**channel_id** | **str** | LINE Channel ID. Can be omitted along with &#x60;channelSecret&#x60; to integrate LINE to setup a webhook before receiving the &#x60;channelId&#x60; and &#x60;channelSecret&#x60; back from LINE. | [optional] 
**channel_secret** | **str** | LINE Channel Secret. Can be omitted along with &#x60;channelId&#x60; to integrate LINE to setup a webhook before receiving the &#x60;channelId&#x60; and &#x60;channelSecret&#x60; back from LINE. | [optional] 
**channel_access_token** | **str** | LINE Channel Access Token. | [optional] 
**service_code** | **str** | LINE Service Code. | [optional] 
**switcher_secret** | **str** | LINE Switcher Secret. | [optional] 
**qr_code_url** | **str** | URL provided by LINE in the [Developer Console](https://developers.line.biz/console/). | [optional] 
**line_id** | **str** | LINE Basic ID. Is automatically set when qrCodeUrl is updated. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


