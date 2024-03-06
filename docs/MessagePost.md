# MessagePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**AuthorMessages**](AuthorMessages.md) | The author of the message. | 
**content** | [**Content**](Content.md) | The content of the message. | 
**destination** | [**Destination**](Destination.md) |  | [optional] 
**metadata** | [**object**](.md) | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**override** | [**MessageOverride**](MessageOverride.md) |  | [optional] 
**schema** | **str** | When &#x60;schema&#x60; is set to &#x60;\&quot;whatsapp\&quot;&#x60;, the &#x60;content&#x60; key is expected to conform to the [native WhatsApp schema](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates) for sending message templates. For more details, consult the documentation for [sending message templates on WhatsApp](https://docs.smooch.io/guide/whatsapp/#sending-message-templates).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


