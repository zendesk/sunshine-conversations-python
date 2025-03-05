# OfferControlBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switchboard_integration** | **str** | The id or the name of the switchboard integration that will become pending. Also supports the &#x60;next&#x60; keyword to offer control to the next switchboard integration designated in the switchboard hierarchy configuration. This cannot match the active switchboard integration. | 
**metadata** | **dict** | Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the &#x60;switchboard:offerControl&#x60; and &#x60;switchboard:offerControl:failure&#x60; webhooks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


