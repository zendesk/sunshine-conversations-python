# Web

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | To configure a Web Messenger integration, acquire the required information and call the Create Integration endpoint.  | [optional] [default to 'web']
**brand_color** | **str** | This color will be used in the messenger header and the button or tab in idle state. Must be a 3 or 6-character hexadecimal color. | [optional] [default to '65758e']
**fixed_intro_pane** | **bool** | When true, the introduction pane will be pinned at the top of the conversation instead of scrolling with it. | [optional] [default to False]
**conversation_color** | **str** | This color will be used for customer messages, quick replies and actions in the footer. Must be a 3 or 6-character hexadecimal color. | [optional] [default to '0099ff']
**action_color** | **str** | This color will be used for call-to-actions inside your messages. Must be a 3 or 6-character hexadecimal color. | [optional] [default to '0099ff']
**display_style** | **str** | Choose how the messenger will appear on your website. Must be either button or tab. | [optional] [default to 'button']
**button_icon_url** | **str** | With the button style Web Messenger, you have the option of selecting your own button icon. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format. | [optional] 
**button_width** | **str** | With the button style Web Messenger, you have the option of specifying the button width. | [optional] [default to '58']
**button_height** | **str** | With the button style Web Messenger, you have the option of specifying the button height. | [optional] [default to '58']
**integration_order** | **list[str]** | Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed. | [optional] 
**business_name** | **str** | A custom business name for the Web Messenger. | [optional] 
**business_icon_url** | **str** | A custom business icon url for the Web Messenger. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format. | [optional] 
**background_image_url** | **str** | A background image url for the conversation. Image will be tiled to fit the window. | [optional] 
**origin_whitelist** | **list[str]** | A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454: scheme \&quot;://\&quot; host [ \&quot;:\&quot; port ], where scheme is http or https.  | [optional] 
**prechat_capture** | [**PrechatCapture**](PrechatCapture.md) | Object whose properties can be set to specify the add-on’s options. See the [guide](https://docs.smooch.io/guide/web-messenger/#prechat-capture) to learn more about Prechat Capture. | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the web messenger integration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


