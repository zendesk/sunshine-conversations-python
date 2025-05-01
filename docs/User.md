# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the user. | [optional] 
**authenticated** | **bool** | Whether or not the user has authenticated, either via JWT or via the Help Center | [optional] [readonly] 
**external_id** | **str** | An optional ID that can also be used to retrieve the user.  | [optional] 
**zendesk_id** | **str** | The ID that links a messaging user to its core Zendesk user counterpart. This ID can be used to fetch the core user record via the Zendesk Support API.  | [optional] 
**signed_up_at** | **str** |  | [optional] 
**to_be_retained** | **bool** |  | [optional] 
**profile** | [**Profile**](Profile.md) |  | [optional] 
**metadata** | **dict** |  | [optional] 
**identities** | [**list[Identity]**](Identity.md) | The user&#39;s connected identities. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


