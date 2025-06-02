# Twitter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | To set up a Twitter integration, please follow the steps outlined in the [Twitter Setup Guide](https://docs.smooch.io/guide/twitter/#setup).  | [optional] [default to 'twitter']
**tier** | **str** | Your Twitter app&#39;s tier. Only \&quot;enterprise\&quot; is supported for new integrations. | 
**env_name** | **str** | The Twitter dev environments label. Only required / used for sandbox and premium tiers. | [optional] [readonly] 
**consumer_key** | **str** | The consumer key for your Twitter app. | 
**consumer_secret** | **str** | The consumer key secret for your Twitter app. | 
**access_token_key** | **str** | The access token key obtained from your user via oauth. | 
**access_token_secret** | **str** | The access token secret obtained from your user via oauth. | 
**default_responder_id** | **str** | The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the &lt;a href&#x3D;\&quot;https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\&quot;&gt;Switchboard guide&lt;/a&gt;.  | [optional] 
**default_responder** | [**DefaultResponderDefaultResponder**](DefaultResponderDefaultResponder.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


