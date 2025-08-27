# ConversationListFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s id. One of &#x60;userId&#x60; or &#x60;userExternalId&#x60; is required, but not both. | [optional] 
**user_external_id** | **str** | The external Id of the user. One of &#x60;userId&#x60; or &#x60;userExternalId&#x60; is required, but not both. | [optional] 

## Example

```python
from sunshine_conversations_client.model.conversation_list_filter import ConversationListFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationListFilter from a JSON string
conversation_list_filter_instance = ConversationListFilter.from_json(json)
# print the JSON string representation of the object
print(ConversationListFilter.to_json())

# convert the object into a dict
conversation_list_filter_dict = conversation_list_filter_instance.to_dict()
# create an instance of ConversationListFilter from a dict
conversation_list_filter_from_dict = ConversationListFilter.from_dict(conversation_list_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


