# FormMessageField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The field type. | 
**name** | **str** | The name of the field. Must be unique per form or formResponse. | 
**label** | **str** | The label of the field. What the field is displayed as on Web Messenger. | 
**text** | **str** | Specifies the response for a text field. | [optional] 
**email** | **str** | Specifies the response for a email field. | [optional] 
**select** | **list[object]** | Array of objects representing the response for a field of type select. Form and formResponse messages only. | [optional] 
**placeholder** | **str** | Placeholder text for the field. Form message only. | [optional] 
**min_size** | **int** | The minimum allowed length for the response for a field of type text. Form message only. | [optional] [default to 1]
**max_size** | **int** | The maximum allowed length for the response for a field of type text. Form message only. | [optional] [default to 128]
**options** | **list[object]** | Array of objects representing options for a field of type select. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


