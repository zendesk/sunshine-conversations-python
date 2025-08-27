# TransferToEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of system activity that generated the message. The value of this field determines the dynamic content that is rendered to the end-user / agent when viewing this message. Each &#x60;type&#x60; value will have a set of pre-defined, localized strings that describe the activity. | [default to 'ticket:transfer:email']
**data** | **Dict[str, object]** | No additional data is supplied with the \&quot;ticket:transfer:email\&quot; activity type at this time. | [optional] 

## Example

```python
from sunshine_conversations_client.model.transfer_to_email import TransferToEmail

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToEmail from a JSON string
transfer_to_email_instance = TransferToEmail.from_json(json)
# print the JSON string representation of the object
print(TransferToEmail.to_json())

# convert the object into a dict
transfer_to_email_dict = transfer_to_email_instance.to_dict()
# create an instance of TransferToEmail from a dict
transfer_to_email_from_dict = TransferToEmail.from_dict(transfer_to_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


