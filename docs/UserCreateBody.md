# UserCreateBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | A unique identifier for the user. The &#x60;externalId&#x60; can be used to link a user to the same conversation [across multiple devices](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/authenticating-users/).  | 
**signed_up_at** | **str** | The date at which the user signed up. Must be ISO 8601 time format &#x60;YYYY-MM-DDThh:mm:ss.sssZ&#x60;. | [optional] 
**to_be_retained** | **bool** | Flag indicating whether a user should be retained after they have passed their inactive expiry. See [creating deletion schedules for bot-only conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154) for more information. | [optional] 
**profile** | [**Profile**](Profile.md) |  | [optional] 
**metadata** | **dict(str, object)** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


