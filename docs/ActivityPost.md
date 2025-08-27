# ActivityPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | If the author type is &#x60;user&#x60;, only &#x60;conversation:read&#x60; is supported. | 
**author** | [**Author**](Author.md) | The author of the activity. | 

## Example

```python
from sunshine_conversations_client.model.activity_post import ActivityPost

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPost from a JSON string
activity_post_instance = ActivityPost.from_json(json)
# print the JSON string representation of the object
print(ActivityPost.to_json())

# convert the object into a dict
activity_post_dict = activity_post_instance.to_dict()
# create an instance of ActivityPost from a dict
activity_post_from_dict = ActivityPost.from_dict(activity_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


