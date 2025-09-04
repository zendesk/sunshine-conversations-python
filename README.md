# sunshine-conversations-client
# Introduction

<aside class=\"notice\"><strong>Note:</strong> The documentation below applies to v2 of the API. For users wanting to access v1, please proceed <a href=\"https://docs.smooch.io/rest/v1\">here</a> instead.
</aside>

Welcome to the Sunshine Conversations API. The API allows you to craft entirely unique messaging experiences for your app and website as well as talk to any backend or external service.

The Sunshine Conversations API is designed according to REST principles. The API accepts JSON in request bodies and requires that the `content-type: application/json` header be specified for
all such requests. The API will always respond with an object. Depending on context, resources may be returned as single objects or as arrays of objects, nested within the response object.

## Regions

Licensed Zendesk customers should use the following API host for all API requests, unless otherwise specified:

```
https://{subdomain}.zendesk.com/sc
```

For legacy Sunshine Conversations customers, see [regions](https://docs.smooch.io/guide/regions/) for the list of supported base URLs.

<aside class=\"notice\"><strong>Note:</strong> When configuring an API host, make sure to always use <code>https</code>. Some API clients can have unexpected behaviour when following redirects from <code>http</code> to <code>https</code>.</aside>

## Errors

Sunshine Conversations uses standard HTTP status codes to communicate errors. In general, a `2xx` status code indicates success while `4xx` indicates an error, in which case, the response body includes a JSON object which includes an array of errors, with a text `code` and `title` containing more details. Multiple errors can only be included in a `400 Bad Request`. A `5xx` status code indicates that something went wrong on our end.

```javascript
{
   \"errors\":  [
    {
        \"code\": \"unauthorized\",
        \"title\": \"Authorization is required\"
    }
   ]
}
```

## API Version

The latest version of the API is v2. Version v1.1 is still supported and you can continue using it but we encourage you to upgrade to the latest version. To learn more about API versioning at Sunshine Conversations, including instructions on how to upgrade to the latest version, [visit our docs](https://developer.zendesk.com/documentation/conversations/references/api-versioning/).

## API Pagination and Records Limits

All paginated endpoints support cursor-based pagination.

### Cursor Pagination

Cursor-based pagination is a common pagination strategy that avoids many of the pitfalls of offset–limit pagination. It works by returning a pointer to a specific item in the dataset. On subsequent requests, the server returns results after the given pointer.

A `page[after]` or `page[before]` query string parameter may be provided, they are cursors pointing to a record id.

The `page[after]` cursor indicates that only records **subsequent** to it should be returned.

The `page[before]` cursor indicates that only records **preceding** it should be returned.

**Only one** of `page[after]` or `page[before]` may be provided in a query, not both.

In most endpoints, an optional `page[size]` query parameter may be passed to control the number of records returned by the request.

## API Libraries

Sunshine Conversations provides an official API library for [Java](https://github.com/zendesk/sunshine-conversations-java), with more languages to come. These helpful libraries wrap calls to the API and can make interfacing with Sunshine Conversations easier.

## Postman Collection

<a style=\"display:inline-block;background:url(https://run.pstmn.io/button.svg);height:30px;width: 123px;\" href=\"https://docs.smooch.io/sunco-openapi/postman_collection.json\"></a>

In addition to API libraries, Sunshine Conversations also has a Postman collection that can be used for development or testing purposes. See the [guide](https://developer.zendesk.com/documentation/conversations/references/openapi-specification/) for information on how to install and use the collection in your Postman client.

## Rate Limits

Sunshine Conversations APIs are subject to rate limiting. If the rate limit is exceeded a `429 Too Many Requests` HTTP status code may be returned. We apply rate limits to prevent abuse, spam, denial-of-service attacks, and similar issues. Our goal is to keep the limits high enough so that any application using the platform as intended will not encounter them. However usage spikes do occur and encountering a rate limit may be unavoidable. In order to avoid production outages, you should implement `429` retry logic using exponential backoff and jitter.

## Conversation Size Limits

Conversations are limited to 30,000 messages. Once you reach this maximum, a `423 Locked` HTTP status code is returned when trying to post a new message. To allow more messages to be sent to the affected conversation, you must [delete all messages](https://developer.zendesk.com/api-reference/conversations/#operation/DeleteAllMessages) to make room.

## Request Size Limits

The Sunshine Conversations API imposes the following size limits on HTTP requests:

| Request Type | Limit |
| ------------ | ----- |
| JSON         | 100kb |
| File upload  | 50mb  |

## Authorization

This is an overview of how authorization works with the Sunshine Conversations API. Sunshine Conversations allows basic authentication or JSON Web Tokens (JWTs) as authentication methods for server-to-server calls. [See below](#section/Introduction/Authentication) for more details.

There are three authorization scopes available for the v2 API: `integration`, `app`, and `account`.

| Scope       | Availability                                | Authorized Methods                              |
| ----------- | ------------------------------------------- | ----------------------------------------------- |
| account     | Sunshine Conversations direct accounts only | All methods                                     |
| app         | All account types                           | All methods besides Account Provisioning        |
| integration | All account types                           | Users, Conversations, Attachments, and Webhooks |

<aside class=\"notice\"><strong>Note:</strong> An additional scope of <code>user</code> is used for <a href=\"https://developer.zendesk.com/documentation/conversations/messaging-platform/users/authenticating-users/\">authenticating users</a> on the Zendesk Messaging SDKs. This scope, however, cannot be used with the v2 API.</aside>

## Authentication

To authenticate requests to the API, you will need an API key, composed of a key id and a secret.
For an overview of how authentication works in Sunshine Conversations and instructions on how to generate an API key, see [API authentication](https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/).

API requests can be authenticated in two ways:

- With Basic authentication you can make requests using an API key directly.
- With JSON Web Tokens (JWTs) you sign tokens with an API key, which are then used to authenticate with the API. See [When to Use JWTs](https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/#when-to-use-jwts) to learn if JWTs are relevant for your usage.
- Before using an API key in production, make sure to familiarize yourself with best practices on how to [securely handle credentials](https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/#secure-credential-handling).

### Basic Authentication

API requests can be authenticated with [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) using an API key. The key id is used as the username and the secret as the password. The scope of access is determined by the owner of the API key. See the [guide](https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/#access-scopes) for more details.

### JWTs

JSON Web Tokens (JWTs) are an industry standard authentication method. The full specification is described [here](https://tools.ietf.org/html/rfc7519), and a set of supported JWT libraries for a variety of languages and platforms can be found at http://jwt.io. To summarize, a JWT is composed of a header, a payload, and a signature. The payload contains information called claims which describe the subject to whom the token was issued.
The JWT itself is transmitted via the HTTP `authorization` header. The token should be prefixed with “Bearer” followed by a space. For example: `Bearer your-jwt`.
To generate a JWT, you need an API key, which is composed of a key ID and a secret. The key ID is included in a JWT’s header, as the `kid` property, while the secret is used to sign the JWT.
For more in-depth coverage, see the [guide](https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/#jwt-authentication).

#### Header

The JWT header must contain the key id (kid) of the API key that is used to sign it. The algorithm (alg) used should be HS256. Unsigned JWTs are not accepted.

```javascript
{
    \"alg\": \"HS256\",
    \"typ\": \"JWT\",
    \"kid\": \"act_5963ceb97cde542d000dbdb1\"
}
```

#### Payload

The JWT payload must include a scope claim which specifies the caller’s scope of access.

- account-scoped JWTs must be generated with an API key associated with a Sunshine Conversations account (act*) or service account (svc*).

```javascript
{
    \"scope\": \"account\"
}
```

- app-scoped JWTs can be generated with an API key associated with an app (app\\_).

```javascript
{
   \"scope\": \"app\"
}
```


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 17.0.0
- Package version: 17.0.1
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sunshine_conversations_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sunshine_conversations_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sunshine_conversations_client
from sunshine_conversations_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.smooch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sunshine_conversations_client.Configuration(
    host = "https://api.smooch.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = sunshine_conversations_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = sunshine_conversations_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with sunshine_conversations_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sunshine_conversations_client.ActivitiesApi(api_client)
    app_id = '5d8cff3cd55b040010928b5b' # str | Identifies the app.
    conversation_id = '029c31f25a21b47effd7be90' # str | Identifies the conversation.
    activity_post = {"author":{"type":"user","userId":"5963c0d619a30a2e00de36b8"},"type":"conversation:read"} # ActivityPost | 

    try:
        # Post Activity
        api_response = api_instance.post_activity(app_id, conversation_id, activity_post)
        print("The response of ActivitiesApi->post_activity:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivitiesApi->post_activity: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.smooch.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivitiesApi* | [**post_activity**](docs/ActivitiesApi.md#post_activity) | **POST** /v2/apps/{appId}/conversations/{conversationId}/activity | Post Activity
*AppKeysApi* | [**create_app_key**](docs/AppKeysApi.md#create_app_key) | **POST** /v2/apps/{appId}/keys | Create App Key
*AppKeysApi* | [**delete_app_key**](docs/AppKeysApi.md#delete_app_key) | **DELETE** /v2/apps/{appId}/keys/{keyId} | Delete App Key
*AppKeysApi* | [**get_app_key**](docs/AppKeysApi.md#get_app_key) | **GET** /v2/apps/{appId}/keys/{keyId} | Get App Key
*AppKeysApi* | [**list_app_keys**](docs/AppKeysApi.md#list_app_keys) | **GET** /v2/apps/{appId}/keys | List App Keys
*AppsApi* | [**create_app**](docs/AppsApi.md#create_app) | **POST** /v2/apps | Create App
*AppsApi* | [**delete_app**](docs/AppsApi.md#delete_app) | **DELETE** /v2/apps/{appId} | Delete App
*AppsApi* | [**get_app**](docs/AppsApi.md#get_app) | **GET** /v2/apps/{appId} | Get App
*AppsApi* | [**list_apps**](docs/AppsApi.md#list_apps) | **GET** /v2/apps | List Apps
*AppsApi* | [**update_app**](docs/AppsApi.md#update_app) | **PATCH** /v2/apps/{appId} | Update App
*AttachmentsApi* | [**delete_attachment**](docs/AttachmentsApi.md#delete_attachment) | **POST** /v2/apps/{appId}/attachments/remove | Delete Attachment
*AttachmentsApi* | [**upload_attachment**](docs/AttachmentsApi.md#upload_attachment) | **POST** /v2/apps/{appId}/attachments | Upload Attachment
*ClientsApi* | [**create_client**](docs/ClientsApi.md#create_client) | **POST** /v2/apps/{appId}/users/{userIdOrExternalId}/clients | Create Client
*ClientsApi* | [**list_clients**](docs/ClientsApi.md#list_clients) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/clients | List Clients
*ClientsApi* | [**remove_client**](docs/ClientsApi.md#remove_client) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId}/clients/{clientId} | Remove Client
*ConversationsApi* | [**create_conversation**](docs/ConversationsApi.md#create_conversation) | **POST** /v2/apps/{appId}/conversations | Create Conversation
*ConversationsApi* | [**delete_conversation**](docs/ConversationsApi.md#delete_conversation) | **DELETE** /v2/apps/{appId}/conversations/{conversationId} | Delete Conversation
*ConversationsApi* | [**download_message_ref**](docs/ConversationsApi.md#download_message_ref) | **POST** /v2/apps/{appId}/conversations/{conversationId}/download | Download Message Ref
*ConversationsApi* | [**get_conversation**](docs/ConversationsApi.md#get_conversation) | **GET** /v2/apps/{appId}/conversations/{conversationId} | Get Conversation
*ConversationsApi* | [**list_conversations**](docs/ConversationsApi.md#list_conversations) | **GET** /v2/apps/{appId}/conversations | List Conversations
*ConversationsApi* | [**post_conversion_events**](docs/ConversationsApi.md#post_conversion_events) | **POST** /v2/apps/{appId}/conversations/{conversationId}/conversionEvents | Post Conversion Events
*ConversationsApi* | [**update_conversation**](docs/ConversationsApi.md#update_conversation) | **PATCH** /v2/apps/{appId}/conversations/{conversationId} | Update Conversation
*CustomIntegrationApiKeysApi* | [**create_custom_integration_key**](docs/CustomIntegrationApiKeysApi.md#create_custom_integration_key) | **POST** /v2/apps/{appId}/integrations/{integrationId}/keys | Create Integration Key
*CustomIntegrationApiKeysApi* | [**delete_custom_integration_key**](docs/CustomIntegrationApiKeysApi.md#delete_custom_integration_key) | **DELETE** /v2/apps/{appId}/integrations/{integrationId}/keys/{keyId} | Delete Integration Key
*CustomIntegrationApiKeysApi* | [**get_custom_integration_key**](docs/CustomIntegrationApiKeysApi.md#get_custom_integration_key) | **GET** /v2/apps/{appId}/integrations/{integrationId}/keys/{keyId} | Get Integration Key
*CustomIntegrationApiKeysApi* | [**list_custom_integration_keys**](docs/CustomIntegrationApiKeysApi.md#list_custom_integration_keys) | **GET** /v2/apps/{appId}/integrations/{integrationId}/keys | List Integration Keys
*DevicesApi* | [**get_device**](docs/DevicesApi.md#get_device) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/devices/{deviceId} | Get Device
*DevicesApi* | [**list_devices**](docs/DevicesApi.md#list_devices) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/devices | List Devices
*IntegrationsApi* | [**create_integration**](docs/IntegrationsApi.md#create_integration) | **POST** /v2/apps/{appId}/integrations | Create Integration
*IntegrationsApi* | [**delete_integration**](docs/IntegrationsApi.md#delete_integration) | **DELETE** /v2/apps/{appId}/integrations/{integrationId} | Delete Integration
*IntegrationsApi* | [**get_integration**](docs/IntegrationsApi.md#get_integration) | **GET** /v2/apps/{appId}/integrations/{integrationId} | Get Integration
*IntegrationsApi* | [**list_integrations**](docs/IntegrationsApi.md#list_integrations) | **GET** /v2/apps/{appId}/integrations | List Integrations
*IntegrationsApi* | [**update_integration**](docs/IntegrationsApi.md#update_integration) | **PATCH** /v2/apps/{appId}/integrations/{integrationId} | Update Integration
*MessagesApi* | [**delete_all_messages**](docs/MessagesApi.md#delete_all_messages) | **DELETE** /v2/apps/{appId}/conversations/{conversationId}/messages | Delete All Messages
*MessagesApi* | [**delete_message**](docs/MessagesApi.md#delete_message) | **DELETE** /v2/apps/{appId}/conversations/{conversationId}/messages/{messageId} | Delete Message
*MessagesApi* | [**list_messages**](docs/MessagesApi.md#list_messages) | **GET** /v2/apps/{appId}/conversations/{conversationId}/messages | List Messages
*MessagesApi* | [**post_message**](docs/MessagesApi.md#post_message) | **POST** /v2/apps/{appId}/conversations/{conversationId}/messages | Post Message
*OAuthEndpointsApi* | [**authorize**](docs/OAuthEndpointsApi.md#authorize) | **GET** /oauth/authorize | Authorize
*OAuthEndpointsApi* | [**get_token**](docs/OAuthEndpointsApi.md#get_token) | **POST** /oauth/token | Get Token
*OAuthEndpointsApi* | [**get_token_info**](docs/OAuthEndpointsApi.md#get_token_info) | **GET** /v2/tokenInfo | Get Token Info
*OAuthEndpointsApi* | [**revoke_access**](docs/OAuthEndpointsApi.md#revoke_access) | **DELETE** /oauth/authorization | Revoke Access
*ParticipantsApi* | [**join_conversation**](docs/ParticipantsApi.md#join_conversation) | **POST** /v2/apps/{appId}/conversations/{conversationId}/join | Join Conversation
*ParticipantsApi* | [**leave_conversation**](docs/ParticipantsApi.md#leave_conversation) | **POST** /v2/apps/{appId}/conversations/{conversationId}/leave | Leave Conversation
*ParticipantsApi* | [**list_participants**](docs/ParticipantsApi.md#list_participants) | **GET** /v2/apps/{appId}/conversations/{conversationId}/participants | List Participants
*SwitchboardActionsApi* | [**accept_control**](docs/SwitchboardActionsApi.md#accept_control) | **POST** /v2/apps/{appId}/conversations/{conversationId}/acceptControl | Accept Control
*SwitchboardActionsApi* | [**offer_control**](docs/SwitchboardActionsApi.md#offer_control) | **POST** /v2/apps/{appId}/conversations/{conversationId}/offerControl | Offer Control
*SwitchboardActionsApi* | [**pass_control**](docs/SwitchboardActionsApi.md#pass_control) | **POST** /v2/apps/{appId}/conversations/{conversationId}/passControl | Pass Control
*SwitchboardActionsApi* | [**release_control**](docs/SwitchboardActionsApi.md#release_control) | **POST** /v2/apps/{appId}/conversations/{conversationId}/releaseControl | Release Control
*SwitchboardIntegrationsApi* | [**create_switchboard_integration**](docs/SwitchboardIntegrationsApi.md#create_switchboard_integration) | **POST** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations | Create Switchboard Integration
*SwitchboardIntegrationsApi* | [**delete_switchboard_integration**](docs/SwitchboardIntegrationsApi.md#delete_switchboard_integration) | **DELETE** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations/{switchboardIntegrationId} | Delete Switchboard Integration
*SwitchboardIntegrationsApi* | [**list_switchboard_integrations**](docs/SwitchboardIntegrationsApi.md#list_switchboard_integrations) | **GET** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations | List Switchboard Integrations
*SwitchboardIntegrationsApi* | [**update_switchboard_integration**](docs/SwitchboardIntegrationsApi.md#update_switchboard_integration) | **PATCH** /v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations/{switchboardIntegrationId} | Update Switchboard Integration
*SwitchboardsApi* | [**create_switchboard**](docs/SwitchboardsApi.md#create_switchboard) | **POST** /v2/apps/{appId}/switchboards | Create Switchboard
*SwitchboardsApi* | [**delete_switchboard**](docs/SwitchboardsApi.md#delete_switchboard) | **DELETE** /v2/apps/{appId}/switchboards/{switchboardId} | Delete Switchboard
*SwitchboardsApi* | [**list_switchboards**](docs/SwitchboardsApi.md#list_switchboards) | **GET** /v2/apps/{appId}/switchboards | List Switchboards
*SwitchboardsApi* | [**update_switchboard**](docs/SwitchboardsApi.md#update_switchboard) | **PATCH** /v2/apps/{appId}/switchboards/{switchboardId} | Update Switchboard
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /v2/apps/{appId}/users | Create User
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId} | Delete User
*UsersApi* | [**delete_user_personal_information**](docs/UsersApi.md#delete_user_personal_information) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId}/personalinformation | Delete User Personal Information
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId} | Get User
*UsersApi* | [**sync_user**](docs/UsersApi.md#sync_user) | **POST** /v2/apps/{appId}/users/{zendeskId}/sync | Synchronize User
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PATCH** /v2/apps/{appId}/users/{userIdOrExternalId} | Update User
*WebhooksApi* | [**create_webhook**](docs/WebhooksApi.md#create_webhook) | **POST** /v2/apps/{appId}/integrations/{integrationId}/webhooks | Create Webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId} | Delete Webhook
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId} | Get Webhook
*WebhooksApi* | [**list_webhooks**](docs/WebhooksApi.md#list_webhooks) | **GET** /v2/apps/{appId}/integrations/{integrationId}/webhooks | List Webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PATCH** /v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId} | Update Webhook


## Documentation For Models

 - [AcceptControlBody](docs/AcceptControlBody.md)
 - [Action](docs/Action.md)
 - [ActionSubset](docs/ActionSubset.md)
 - [Activity](docs/Activity.md)
 - [ActivityMessage](docs/ActivityMessage.md)
 - [ActivityPost](docs/ActivityPost.md)
 - [ActivityTypes](docs/ActivityTypes.md)
 - [Android](docs/Android.md)
 - [AndroidUpdate](docs/AndroidUpdate.md)
 - [ApiKey](docs/ApiKey.md)
 - [App](docs/App.md)
 - [AppCreateBody](docs/AppCreateBody.md)
 - [AppKey](docs/AppKey.md)
 - [AppKeyCreateBody](docs/AppKeyCreateBody.md)
 - [AppKeyListResponse](docs/AppKeyListResponse.md)
 - [AppKeyResponse](docs/AppKeyResponse.md)
 - [AppListFilter](docs/AppListFilter.md)
 - [AppListResponse](docs/AppListResponse.md)
 - [AppResponse](docs/AppResponse.md)
 - [AppSettings](docs/AppSettings.md)
 - [AppSubSchema](docs/AppSubSchema.md)
 - [AppUpdateBody](docs/AppUpdateBody.md)
 - [Apple](docs/Apple.md)
 - [AppleMessageOverridePayload](docs/AppleMessageOverridePayload.md)
 - [AppleUpdate](docs/AppleUpdate.md)
 - [AttachmentDeleteBody](docs/AttachmentDeleteBody.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [AttachmentSchema](docs/AttachmentSchema.md)
 - [Author](docs/Author.md)
 - [AuthorWebhook](docs/AuthorWebhook.md)
 - [Buy](docs/Buy.md)
 - [Campaign](docs/Campaign.md)
 - [CarouselMessage](docs/CarouselMessage.md)
 - [CarouselMessageDisplaySettings](docs/CarouselMessageDisplaySettings.md)
 - [Client](docs/Client.md)
 - [ClientAddEvent](docs/ClientAddEvent.md)
 - [ClientAddEventAllOfPayload](docs/ClientAddEventAllOfPayload.md)
 - [ClientAssociation](docs/ClientAssociation.md)
 - [ClientCreate](docs/ClientCreate.md)
 - [ClientListResponse](docs/ClientListResponse.md)
 - [ClientRemoveEvent](docs/ClientRemoveEvent.md)
 - [ClientRemoveEventAllOfPayload](docs/ClientRemoveEventAllOfPayload.md)
 - [ClientResponse](docs/ClientResponse.md)
 - [ClientType](docs/ClientType.md)
 - [ClientUpdateEvent](docs/ClientUpdateEvent.md)
 - [ClientUpdateEventAllOfPayload](docs/ClientUpdateEventAllOfPayload.md)
 - [Confirmation](docs/Confirmation.md)
 - [Content](docs/Content.md)
 - [Conversation](docs/Conversation.md)
 - [ConversationCreateBody](docs/ConversationCreateBody.md)
 - [ConversationCreateEvent](docs/ConversationCreateEvent.md)
 - [ConversationCreateEventAllOfPayload](docs/ConversationCreateEventAllOfPayload.md)
 - [ConversationJoinEvent](docs/ConversationJoinEvent.md)
 - [ConversationJoinEventAllOfPayload](docs/ConversationJoinEventAllOfPayload.md)
 - [ConversationLeaveEvent](docs/ConversationLeaveEvent.md)
 - [ConversationLeaveEventAllOfPayload](docs/ConversationLeaveEventAllOfPayload.md)
 - [ConversationListFilter](docs/ConversationListFilter.md)
 - [ConversationListResponse](docs/ConversationListResponse.md)
 - [ConversationMessageDeliveryChannelEvent](docs/ConversationMessageDeliveryChannelEvent.md)
 - [ConversationMessageDeliveryFailureEvent](docs/ConversationMessageDeliveryFailureEvent.md)
 - [ConversationMessageDeliveryFailureEventAllOfPayload](docs/ConversationMessageDeliveryFailureEventAllOfPayload.md)
 - [ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError](docs/ConversationMessageDeliveryFailureEventAllOfPayloadAllOfError.md)
 - [ConversationMessageDeliveryPayload](docs/ConversationMessageDeliveryPayload.md)
 - [ConversationMessageDeliveryPayloadDestination](docs/ConversationMessageDeliveryPayloadDestination.md)
 - [ConversationMessageDeliveryPayloadExternalMessagesInner](docs/ConversationMessageDeliveryPayloadExternalMessagesInner.md)
 - [ConversationMessageDeliveryPayloadMessage](docs/ConversationMessageDeliveryPayloadMessage.md)
 - [ConversationMessageDeliveryUserEvent](docs/ConversationMessageDeliveryUserEvent.md)
 - [ConversationMessageEvent](docs/ConversationMessageEvent.md)
 - [ConversationMessageEventAllOfPayload](docs/ConversationMessageEventAllOfPayload.md)
 - [ConversationPostbackEvent](docs/ConversationPostbackEvent.md)
 - [ConversationPostbackEventAllOfPayload](docs/ConversationPostbackEventAllOfPayload.md)
 - [ConversationReadEvent](docs/ConversationReadEvent.md)
 - [ConversationReadEventAllOfPayload](docs/ConversationReadEventAllOfPayload.md)
 - [ConversationReadEventAllOfPayloadActivity](docs/ConversationReadEventAllOfPayloadActivity.md)
 - [ConversationReferralEvent](docs/ConversationReferralEvent.md)
 - [ConversationReferralEventAllOfPayload](docs/ConversationReferralEventAllOfPayload.md)
 - [ConversationRemoveEvent](docs/ConversationRemoveEvent.md)
 - [ConversationRemoveEventAllOfPayload](docs/ConversationRemoveEventAllOfPayload.md)
 - [ConversationResponse](docs/ConversationResponse.md)
 - [ConversationTruncated](docs/ConversationTruncated.md)
 - [ConversationType](docs/ConversationType.md)
 - [ConversationTypingEvent](docs/ConversationTypingEvent.md)
 - [ConversationTypingEventAllOfPayload](docs/ConversationTypingEventAllOfPayload.md)
 - [ConversationTypingEventAllOfPayloadActivity](docs/ConversationTypingEventAllOfPayloadActivity.md)
 - [ConversationUpdateBody](docs/ConversationUpdateBody.md)
 - [ConversionEventsBody](docs/ConversionEventsBody.md)
 - [Custom](docs/Custom.md)
 - [CustomUpdate](docs/CustomUpdate.md)
 - [DefaultResponder](docs/DefaultResponder.md)
 - [DefaultResponderDefaultResponder](docs/DefaultResponderDefaultResponder.md)
 - [DefaultResponderId](docs/DefaultResponderId.md)
 - [Destination](docs/Destination.md)
 - [Device](docs/Device.md)
 - [DeviceListResponse](docs/DeviceListResponse.md)
 - [DeviceResponse](docs/DeviceResponse.md)
 - [DownloadMessageRefBody](docs/DownloadMessageRefBody.md)
 - [DownloadMessageRefBodyAllOfApple](docs/DownloadMessageRefBodyAllOfApple.md)
 - [DownloadMessageRefBodyAllOfAppleInteractiveDataRef](docs/DownloadMessageRefBodyAllOfAppleInteractiveDataRef.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventSubSchema](docs/EventSubSchema.md)
 - [ExtraChannelOptions](docs/ExtraChannelOptions.md)
 - [ExtraChannelOptionsMessenger](docs/ExtraChannelOptionsMessenger.md)
 - [FileMessage](docs/FileMessage.md)
 - [FormMessage](docs/FormMessage.md)
 - [FormMessageField](docs/FormMessageField.md)
 - [FormOptionsInner](docs/FormOptionsInner.md)
 - [FormResponseMessage](docs/FormResponseMessage.md)
 - [FormResponseMessageField](docs/FormResponseMessageField.md)
 - [GetToken200Response](docs/GetToken200Response.md)
 - [GetTokenRequest](docs/GetTokenRequest.md)
 - [Identity](docs/Identity.md)
 - [ImageMessage](docs/ImageMessage.md)
 - [Instagram](docs/Instagram.md)
 - [InstagramConversionEventsBody](docs/InstagramConversionEventsBody.md)
 - [InstagramUpdate](docs/InstagramUpdate.md)
 - [Integration](docs/Integration.md)
 - [IntegrationApiKey](docs/IntegrationApiKey.md)
 - [IntegrationApiKeyListResponse](docs/IntegrationApiKeyListResponse.md)
 - [IntegrationApiKeyResponse](docs/IntegrationApiKeyResponse.md)
 - [IntegrationId](docs/IntegrationId.md)
 - [IntegrationListFilter](docs/IntegrationListFilter.md)
 - [IntegrationListResponse](docs/IntegrationListResponse.md)
 - [IntegrationResponse](docs/IntegrationResponse.md)
 - [IntegrationType](docs/IntegrationType.md)
 - [IntegrationUpdate](docs/IntegrationUpdate.md)
 - [IntegrationUpdateBase](docs/IntegrationUpdateBase.md)
 - [Ios](docs/Ios.md)
 - [IosUpdate](docs/IosUpdate.md)
 - [Item](docs/Item.md)
 - [Line](docs/Line.md)
 - [LineUpdate](docs/LineUpdate.md)
 - [Link](docs/Link.md)
 - [Links](docs/Links.md)
 - [ListMessage](docs/ListMessage.md)
 - [LocationMessage](docs/LocationMessage.md)
 - [LocationMessageCoordinates](docs/LocationMessageCoordinates.md)
 - [LocationMessageLocation](docs/LocationMessageLocation.md)
 - [LocationRequest](docs/LocationRequest.md)
 - [Mailgun](docs/Mailgun.md)
 - [MailgunUpdate](docs/MailgunUpdate.md)
 - [MatchCriteria](docs/MatchCriteria.md)
 - [MatchCriteriaBase](docs/MatchCriteriaBase.md)
 - [MatchCriteriaMailgun](docs/MatchCriteriaMailgun.md)
 - [MatchCriteriaMessagebird](docs/MatchCriteriaMessagebird.md)
 - [MatchCriteriaTwilio](docs/MatchCriteriaTwilio.md)
 - [MatchCriteriaWhatsapp](docs/MatchCriteriaWhatsapp.md)
 - [Message](docs/Message.md)
 - [MessageBirdUpdate](docs/MessageBirdUpdate.md)
 - [MessageListResponse](docs/MessageListResponse.md)
 - [MessageOverride](docs/MessageOverride.md)
 - [MessageOverrideApple](docs/MessageOverrideApple.md)
 - [MessageOverrideLine](docs/MessageOverrideLine.md)
 - [MessageOverrideMessenger](docs/MessageOverrideMessenger.md)
 - [MessageOverridePayload](docs/MessageOverridePayload.md)
 - [MessageOverrideWhatsapp](docs/MessageOverrideWhatsapp.md)
 - [MessagePost](docs/MessagePost.md)
 - [MessagePostResponse](docs/MessagePostResponse.md)
 - [MessageWebhook](docs/MessageWebhook.md)
 - [MessageWebhookSource](docs/MessageWebhookSource.md)
 - [Messagebird](docs/Messagebird.md)
 - [Messenger](docs/Messenger.md)
 - [MessengerConversionEventsBody](docs/MessengerConversionEventsBody.md)
 - [MessengerUpdate](docs/MessengerUpdate.md)
 - [Meta](docs/Meta.md)
 - [MetaConversionEvent](docs/MetaConversionEvent.md)
 - [MetaConversionEventPayload](docs/MetaConversionEventPayload.md)
 - [ModelField](docs/ModelField.md)
 - [OfferControlBody](docs/OfferControlBody.md)
 - [Page](docs/Page.md)
 - [Participant](docs/Participant.md)
 - [ParticipantJoinBody](docs/ParticipantJoinBody.md)
 - [ParticipantLeaveBody](docs/ParticipantLeaveBody.md)
 - [ParticipantLeaveBodyParticipantId](docs/ParticipantLeaveBodyParticipantId.md)
 - [ParticipantLeaveBodyUserExternalId](docs/ParticipantLeaveBodyUserExternalId.md)
 - [ParticipantLeaveBodyUserId](docs/ParticipantLeaveBodyUserId.md)
 - [ParticipantListResponse](docs/ParticipantListResponse.md)
 - [ParticipantResponse](docs/ParticipantResponse.md)
 - [ParticipantSubSchema](docs/ParticipantSubSchema.md)
 - [ParticipantWithUserExternalId](docs/ParticipantWithUserExternalId.md)
 - [ParticipantWithUserId](docs/ParticipantWithUserId.md)
 - [PassControlBody](docs/PassControlBody.md)
 - [Postback](docs/Postback.md)
 - [PostbackWebhook](docs/PostbackWebhook.md)
 - [PrechatCapture](docs/PrechatCapture.md)
 - [Profile](docs/Profile.md)
 - [QuotedMessage](docs/QuotedMessage.md)
 - [QuotedMessageExternalMessageId](docs/QuotedMessageExternalMessageId.md)
 - [QuotedMessageMessage](docs/QuotedMessageMessage.md)
 - [Referral](docs/Referral.md)
 - [ReferralDetails](docs/ReferralDetails.md)
 - [ReleaseControlBody](docs/ReleaseControlBody.md)
 - [Reply](docs/Reply.md)
 - [Source](docs/Source.md)
 - [SourceWebhook](docs/SourceWebhook.md)
 - [SourceWithCampaignWebhook](docs/SourceWithCampaignWebhook.md)
 - [Status](docs/Status.md)
 - [Switchboard](docs/Switchboard.md)
 - [SwitchboardAcceptControl](docs/SwitchboardAcceptControl.md)
 - [SwitchboardAcceptControlAllOfPayload](docs/SwitchboardAcceptControlAllOfPayload.md)
 - [SwitchboardAcceptControlFailure](docs/SwitchboardAcceptControlFailure.md)
 - [SwitchboardAcceptControlFailureAllOfPayload](docs/SwitchboardAcceptControlFailureAllOfPayload.md)
 - [SwitchboardIntegration](docs/SwitchboardIntegration.md)
 - [SwitchboardIntegrationCreateBody](docs/SwitchboardIntegrationCreateBody.md)
 - [SwitchboardIntegrationListResponse](docs/SwitchboardIntegrationListResponse.md)
 - [SwitchboardIntegrationResponse](docs/SwitchboardIntegrationResponse.md)
 - [SwitchboardIntegrationUpdateBody](docs/SwitchboardIntegrationUpdateBody.md)
 - [SwitchboardIntegrationWebhook](docs/SwitchboardIntegrationWebhook.md)
 - [SwitchboardListResponse](docs/SwitchboardListResponse.md)
 - [SwitchboardOfferControl](docs/SwitchboardOfferControl.md)
 - [SwitchboardOfferControlAllOfPayload](docs/SwitchboardOfferControlAllOfPayload.md)
 - [SwitchboardOfferControlFailure](docs/SwitchboardOfferControlFailure.md)
 - [SwitchboardPassControl](docs/SwitchboardPassControl.md)
 - [SwitchboardPassControlAllOfPayload](docs/SwitchboardPassControlAllOfPayload.md)
 - [SwitchboardPassControlFailure](docs/SwitchboardPassControlFailure.md)
 - [SwitchboardReleaseControl](docs/SwitchboardReleaseControl.md)
 - [SwitchboardReleaseControlAllOfPayload](docs/SwitchboardReleaseControlAllOfPayload.md)
 - [SwitchboardResponse](docs/SwitchboardResponse.md)
 - [SwitchboardUpdateBody](docs/SwitchboardUpdateBody.md)
 - [SyncUserBody](docs/SyncUserBody.md)
 - [Target](docs/Target.md)
 - [Telegram](docs/Telegram.md)
 - [TelegramUpdate](docs/TelegramUpdate.md)
 - [TemplateMessage](docs/TemplateMessage.md)
 - [TextMessage](docs/TextMessage.md)
 - [TicketClosed](docs/TicketClosed.md)
 - [TransferToEmail](docs/TransferToEmail.md)
 - [Twilio](docs/Twilio.md)
 - [TwilioUpdate](docs/TwilioUpdate.md)
 - [Twitter](docs/Twitter.md)
 - [TwitterUpdate](docs/TwitterUpdate.md)
 - [Unity](docs/Unity.md)
 - [UnityUpdate](docs/UnityUpdate.md)
 - [User](docs/User.md)
 - [UserCreateBody](docs/UserCreateBody.md)
 - [UserMergeEvent](docs/UserMergeEvent.md)
 - [UserMergeEventAllOfPayload](docs/UserMergeEventAllOfPayload.md)
 - [UserMergeEventAllOfPayloadMergedClients](docs/UserMergeEventAllOfPayloadMergedClients.md)
 - [UserMergeEventAllOfPayloadMergedConversations](docs/UserMergeEventAllOfPayloadMergedConversations.md)
 - [UserMergeEventAllOfPayloadMergedUsers](docs/UserMergeEventAllOfPayloadMergedUsers.md)
 - [UserRemoveEvent](docs/UserRemoveEvent.md)
 - [UserRemoveEventAllOfPayload](docs/UserRemoveEventAllOfPayload.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserTruncated](docs/UserTruncated.md)
 - [UserUpdateBody](docs/UserUpdateBody.md)
 - [UserUpdateEvent](docs/UserUpdateEvent.md)
 - [UserUpdateEventAllOfPayload](docs/UserUpdateEventAllOfPayload.md)
 - [Viber](docs/Viber.md)
 - [ViberUpdate](docs/ViberUpdate.md)
 - [Web](docs/Web.md)
 - [WebUpdate](docs/WebUpdate.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookBody](docs/WebhookBody.md)
 - [WebhookCreateBody](docs/WebhookCreateBody.md)
 - [WebhookListResponse](docs/WebhookListResponse.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookSubSchema](docs/WebhookSubSchema.md)
 - [Webview](docs/Webview.md)
 - [WhatsAppConversionEventsBody](docs/WhatsAppConversionEventsBody.md)
 - [WhatsAppUpdate](docs/WhatsAppUpdate.md)
 - [Whatsapp](docs/Whatsapp.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)

<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication


## Author




