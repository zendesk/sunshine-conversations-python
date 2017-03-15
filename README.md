# smooch
The Smooch API is a unified interface for powering messaging in your customers' experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our official documentation.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.2.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import smooch 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import smooch
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import smooch
from smooch.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
smooch.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = smooch.AppApi()
app_create_body = smooch.AppCreate() # AppCreate | Body for a createApp request.

try:
    api_response = api_instance.create_app(app_create_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->create_app: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.smooch.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppApi* | [**create_app**](docs/AppApi.md#create_app) | **POST** /apps | 
*AppApi* | [**create_secret_key**](docs/AppApi.md#create_secret_key) | **POST** /apps/{appId}/keys | 
*AppApi* | [**delete_app**](docs/AppApi.md#delete_app) | **DELETE** /apps/{appId} | 
*AppApi* | [**delete_integration**](docs/AppApi.md#delete_integration) | **DELETE** /apps/{appId}/integrations/{integrationId} | 
*AppApi* | [**delete_secret_key**](docs/AppApi.md#delete_secret_key) | **DELETE** /apps/{appId}/keys/{keyId} | 
*AppApi* | [**get_app**](docs/AppApi.md#get_app) | **GET** /apps/{appId} | 
*AppApi* | [**get_app_jwt**](docs/AppApi.md#get_app_jwt) | **GET** /apps/{appId}/keys/{keyId}/jwt | 
*AppApi* | [**get_integration**](docs/AppApi.md#get_integration) | **GET** /apps/{appId}/integrations/{integrationId} | 
*AppApi* | [**get_secret_key**](docs/AppApi.md#get_secret_key) | **GET** /apps/{appId}/keys/{keyId} | 
*AppApi* | [**list_apps**](docs/AppApi.md#list_apps) | **GET** /apps | 
*AppApi* | [**list_secret_keys**](docs/AppApi.md#list_secret_keys) | **GET** /apps/{appId}/keys | 
*AppUserApi* | [**app_user_device_update**](docs/AppUserApi.md#app_user_device_update) | **PUT** /appusers/{userId}/devices/{deviceId} | 
*AppUserApi* | [**delete_app_user_profile**](docs/AppUserApi.md#delete_app_user_profile) | **DELETE** /appusers/{userId}/profile | 
*AppUserApi* | [**get_app_user**](docs/AppUserApi.md#get_app_user) | **GET** /appusers/{userId} | 
*AppUserApi* | [**get_app_user_entity_ids**](docs/AppUserApi.md#get_app_user_entity_ids) | **GET** /appusers/{userId}/channels | 
*AppUserApi* | [**link_app_user**](docs/AppUserApi.md#link_app_user) | **POST** /appusers/{userId}/channels | 
*AppUserApi* | [**post_image_message**](docs/AppUserApi.md#post_image_message) | **POST** /appusers/{userId}/images | 
*AppUserApi* | [**pre_create_app_user**](docs/AppUserApi.md#pre_create_app_user) | **POST** /appusers | 
*AppUserApi* | [**track_event**](docs/AppUserApi.md#track_event) | **POST** /appusers/{userId}/events | 
*AppUserApi* | [**unlink_app_user**](docs/AppUserApi.md#unlink_app_user) | **DELETE** /appusers/{userId}/channels/{channel} | 
*AppUserApi* | [**update_app_user**](docs/AppUserApi.md#update_app_user) | **PUT** /appusers/{userId} | 
*ConversationApi* | [**delete_messages**](docs/ConversationApi.md#delete_messages) | **DELETE** /appusers/{userId}/messages | 
*ConversationApi* | [**get_messages**](docs/ConversationApi.md#get_messages) | **GET** /appusers/{userId}/messages | 
*ConversationApi* | [**post_message**](docs/ConversationApi.md#post_message) | **POST** /appusers/{userId}/messages | 
*ConversationApi* | [**reset_unread_count**](docs/ConversationApi.md#reset_unread_count) | **POST** /appusers/{userId}/conversation/read | 
*ConversationApi* | [**trigger_typing_activity**](docs/ConversationApi.md#trigger_typing_activity) | **POST** /appusers/{userId}/conversation/activity | 
*InitApi* | [**init**](docs/InitApi.md#init) | **POST** /init | 
*IntegrationApi* | [**create_integration**](docs/IntegrationApi.md#create_integration) | **POST** /apps/{appId}/integrations | 
*IntegrationApi* | [**list_integrations**](docs/IntegrationApi.md#list_integrations) | **GET** /apps/{appId}/integrations | 
*MenuApi* | [**delete_menu**](docs/MenuApi.md#delete_menu) | **DELETE** /menu | 
*MenuApi* | [**get_menu**](docs/MenuApi.md#get_menu) | **GET** /menu | 
*MenuApi* | [**update_menu**](docs/MenuApi.md#update_menu) | **PUT** /menu | 
*WebhookApi* | [**create_webhook**](docs/WebhookApi.md#create_webhook) | **POST** /apps/{appId}/webhooks | 
*WebhookApi* | [**delete_webhook**](docs/WebhookApi.md#delete_webhook) | **DELETE** /apps/{appId}/webhooks/{webhookId} | 
*WebhookApi* | [**get_webhook**](docs/WebhookApi.md#get_webhook) | **GET** /apps/{appId}/webhooks/{webhookId} | 
*WebhookApi* | [**list_webhooks**](docs/WebhookApi.md#list_webhooks) | **GET** /apps/{appId}/webhooks | 
*WebhookApi* | [**update_webhook**](docs/WebhookApi.md#update_webhook) | **PUT** /apps/{appId}/webhooks/{webhookId} | 


## Documentation For Models

 - [Action](docs/Action.md)
 - [App](docs/App.md)
 - [AppCreate](docs/AppCreate.md)
 - [AppResponse](docs/AppResponse.md)
 - [AppUser](docs/AppUser.md)
 - [AppUserLink](docs/AppUserLink.md)
 - [AppUserPreCreate](docs/AppUserPreCreate.md)
 - [AppUserResponse](docs/AppUserResponse.md)
 - [AppUserUpdate](docs/AppUserUpdate.md)
 - [Client](docs/Client.md)
 - [ClientInfo](docs/ClientInfo.md)
 - [ClientResponse](docs/ClientResponse.md)
 - [Conversation](docs/Conversation.md)
 - [Destination](docs/Destination.md)
 - [DeviceInit](docs/DeviceInit.md)
 - [DeviceUpdate](docs/DeviceUpdate.md)
 - [DisplaySettings](docs/DisplaySettings.md)
 - [Event](docs/Event.md)
 - [GetMessagesResponse](docs/GetMessagesResponse.md)
 - [Init](docs/Init.md)
 - [InitResponse](docs/InitResponse.md)
 - [Integration](docs/Integration.md)
 - [IntegrationCreate](docs/IntegrationCreate.md)
 - [IntegrationResponse](docs/IntegrationResponse.md)
 - [JwtResponse](docs/JwtResponse.md)
 - [ListAppsResponse](docs/ListAppsResponse.md)
 - [ListIntegrationsResponse](docs/ListIntegrationsResponse.md)
 - [ListSecretKeysResponse](docs/ListSecretKeysResponse.md)
 - [ListWebhooksResponse](docs/ListWebhooksResponse.md)
 - [Menu](docs/Menu.md)
 - [MenuItem](docs/MenuItem.md)
 - [MenuResponse](docs/MenuResponse.md)
 - [Message](docs/Message.md)
 - [MessageItem](docs/MessageItem.md)
 - [MessagePost](docs/MessagePost.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [PostMessagesResponse](docs/PostMessagesResponse.md)
 - [SecretKey](docs/SecretKey.md)
 - [SecretKeyCreate](docs/SecretKeyCreate.md)
 - [SecretKeyResponse](docs/SecretKeyResponse.md)
 - [TrackEventResponse](docs/TrackEventResponse.md)
 - [TypingActivityTrigger](docs/TypingActivityTrigger.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookCreate](docs/WebhookCreate.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookUpdate](docs/WebhookUpdate.md)


## Documentation For Authorization


## jwt

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



