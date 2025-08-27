# TicketClosed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of system activity that generated the message. The value of this field determines the dynamic content that is rendered to the end-user / agent when viewing this message. Each &#x60;type&#x60; value will have a set of pre-defined, localized strings that describe the activity. | [default to 'ticket:closed']
**data** | **Dict[str, object]** | No additional data is supplied with the \&quot;ticket:closed\&quot; activity type at this time. | [optional] 

## Example

```python
from sunshine_conversations_client.model.ticket_closed import TicketClosed

# TODO update the JSON string below
json = "{}"
# create an instance of TicketClosed from a JSON string
ticket_closed_instance = TicketClosed.from_json(json)
# print the JSON string representation of the object
print(TicketClosed.to_json())

# convert the object into a dict
ticket_closed_dict = ticket_closed_instance.to_dict()
# create an instance of TicketClosed from a dict
ticket_closed_from_dict = TicketClosed.from_dict(ticket_closed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


