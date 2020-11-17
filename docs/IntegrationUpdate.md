# IntegrationUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The integration display name. Used to map a human-friendly name to an integration.  | [optional] 
**brand_color** | **str** | This color will be used in the messenger header and the button or tab in idle state. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**fixed_intro_pane** | **bool** | When &#x60;true&#x60;, the introduction pane will be pinned at the top of the conversation instead of scrolling with it. The default value is &#x60;false&#x60;. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**conversation_color** | **str** | This color will be used for customer messages, quick replies and actions in the footer. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**action_color** | **str** | This color will be used for call-to-actions inside your messages. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**display_style** | **str** | Choose how the messenger will appear on your website. Must be either button or tab. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**button_icon_url** | **str** | With the button style Web Messenger, you have the option of selecting your own button icon. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**button_width** | **str** | With the button style Web Messenger, you have the option of specifying its width. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**button_height** | **str** | With the button style Web Messenger, you have the option of specifying its height. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**integration_order** | **list[str]** | Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed (Optional) Used for *Web Messenger* integrations.  | [optional] 
**business_name** | **str** | A custom business name for the Web Messenger or Instagram Business account name. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**business_icon_url** | **str** | A custom business icon url for the Web Messenger. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**background_image_url** | **str** | A custom background url for the Web Messenger. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**origin_whitelist** | **list[str]** | A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454 &#x60;scheme \&quot;://\&quot; host [ \&quot;:\&quot; port ]&#x60;, where scheme is &#x60;http&#x60; or &#x60;https&#x60;. (Optional) Used for *Web Messenger* integrations.  | [optional] 
**channel_id** | **str** | LINE Channel ID. Required for *line* integrations.  | [optional] 
**channel_secret** | **str** | LINE Channel Secret. Required for *line* integrations.  | [optional] 
**service_code** | **str** | LINE Service Code.  | [optional] 
**switcher_secret** | **str** | LINE Switcher Secret.  | [optional] 
**hsm_fallback_language** | **str** | Specification of a fallback language. (Optional) Used for *WhatsApp* integrations.  | [optional] 
**qr_code_url** | **str** | URL provided by LINE in the [Developer Console](https://developers.line.biz/console/).  | [optional] 
**hide_unsubscribe_link** | **bool** | When &#x60;true&#x60;, unsubscribe links will not be included in outbound emails. If this setting is enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. (Optional) Used for *mailgun* integrations.  | [optional] 
**from_address** | **str** | Email address to use as the &#x60;From&#x60; and &#x60;Reply-To&#x60; address if it must be different from &#x60;incomingAddress&#x60;. Only use this option if the address that you supply is configured to forward emails to the &#x60;incomingAddress&#x60;, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user&#39;s email client.  (Optional) Used for *mailgun* integrations.  | [optional] 
**production** | **bool** | Flag specifying the APN environment to connect to (&#x60;production&#x60; if true, &#x60;sandbox&#x60; otherwise). Defaults to value inferred from certificate if not specified. (Optional) Used for *apn* integrations.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


