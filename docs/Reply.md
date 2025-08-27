# Reply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of action. | 
**text** | **str** | The button text. We recommend a non-empty value because some channels may not support empty ones. Text longer than 20 characters will be truncated on Facebook Messenger, and longer than 40 characters will be truncated on Web Messenger, iOS, and Android. | 
**payload** | **str** | A string payload to help you identify the action context. Used when posting the reply. You can also use metadata for more complex needs. | 
**metadata** | **Dict[str, object]** | Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.  | [optional] 
**icon_url** | **str** | An icon to render next to the reply option. | [optional] 

## Example

```python
from sunshine_conversations_client.model.reply import Reply

# TODO update the JSON string below
json = "{}"
# create an instance of Reply from a JSON string
reply_instance = Reply.from_json(json)
# print the JSON string representation of the object
print(Reply.to_json())

# convert the object into a dict
reply_dict = reply_instance.to_dict()
# create an instance of Reply from a dict
reply_from_dict = Reply.from_dict(reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


