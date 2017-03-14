# Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action type. Supported values: *link*, *buy*, *postback*, *reply* and *locationRequest*.  | 
**text** | **str** | The button text. | 
**payload** | **str** | Required for *postback* and *reply* actions. | [optional] 
**metadata** | **object** | Flat JSON object containing any custom properties associated with the action. | [optional] 
**amount** | **str** | The amount being charged. It needs to be specified in cents and is an integer. Required for *buy* actions.  | [optional] 
**currency** | **str** | The currency of the amount being charged (USD, CAD, etc.). | [optional] 
**default** | **bool** | Flag indicating the message action is the default for a message item in Facebook Messenger. | [optional] 
**icon_url** | **str** | An icon to render next to the reply option (Facebook Messenger and Web Messenger only). | [optional] 
**uri** | **str** | The action URI. This is the link that will be used in the clients when clicking the button. Required for *link* actions.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


