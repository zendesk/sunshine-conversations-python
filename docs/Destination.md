# Destination

The destination of the message, in the case of [channel targeting](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/sending-messages/#targeting-a-specific-channel) or sending [silent messages](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/sending-messages/#silent-messages). Only applicable if the author role is `business` and the conversation is of type `personal`. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The id of the integration to deliver the message to. Will return an error if the integration does not exist or if the user does not have a client for the integration attached to the conversation.  | [optional] 
**integration_type** | **str** | The type of the integration to deliver the message to. Can be set to &#x60;none&#x60; if sending a [silent message](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/sending-messages/#silent-messages). Will return an error if the user does not have a client of that type attached to the conversation.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


