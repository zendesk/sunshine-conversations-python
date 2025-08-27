# PrechatCapture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** | Sets the URL of the avatar to use for the automatic reply to the prechat capture messages. | [optional] [default to 'undefined']
**enabled** | **bool** | If true, enables the Prechat Capture add-on when the Web Messenger is initialized. | [optional] [default to False]
**enable_email_linking** | **bool** | f true and Mailgun is integrated, will automatically link submitted emails. | [optional] [default to False]
**fields** | [**List[ModelField]**](ModelField.md) | Array of Fields. Overrides the default Prechat Capture fields to define a custom form. | [optional] 

## Example

```python
from sunshine_conversations_client.model.prechat_capture import PrechatCapture

# TODO update the JSON string below
json = "{}"
# create an instance of PrechatCapture from a JSON string
prechat_capture_instance = PrechatCapture.from_json(json)
# print the JSON string representation of the object
print(PrechatCapture.to_json())

# convert the object into a dict
prechat_capture_dict = prechat_capture_instance.to_dict()
# create an instance of PrechatCapture from a dict
prechat_capture_from_dict = PrechatCapture.from_dict(prechat_capture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


