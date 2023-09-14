# sunshine-conversations-client

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 10.0.1
- Package version: 10.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

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
### Region

Sunshine Conversations is available in the following [regions](https://docs.smooch.io/rest/#section/Introduction/Regions). The US region will be used by default. To target any other region, specify the region's API host in `Configuration`. For example:

```python
configuration = .Configuration(
    host = "https://api.smooch.io"
)
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
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
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Configure Bearer authorization (JWT): bearerAuth
# Uncomment this if you want to use JWTs
#configuration.access_token = 'YOUR_BEARER_TOKEN'


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
*AttachmentsApi* | [**generate_media_json_web_token**](docs/AttachmentsApi.md#generate_media_json_web_token) | **POST** /v2/apps/{appId}/attachments/token | Generate Media Token
*AttachmentsApi* | [**set_cookie**](docs/AttachmentsApi.md#set_cookie) | **GET** /v2/apps/{appId}/attachments/cookie | Set Cookie
*AttachmentsApi* | [**upload_attachment**](docs/AttachmentsApi.md#upload_attachment) | **POST** /v2/apps/{appId}/attachments | Upload Attachment
*ClientsApi* | [**create_client**](docs/ClientsApi.md#create_client) | **POST** /v2/apps/{appId}/users/{userIdOrExternalId}/clients | Create Client
*ClientsApi* | [**list_clients**](docs/ClientsApi.md#list_clients) | **GET** /v2/apps/{appId}/users/{userIdOrExternalId}/clients | List Clients
*ClientsApi* | [**remove_client**](docs/ClientsApi.md#remove_client) | **DELETE** /v2/apps/{appId}/users/{userIdOrExternalId}/clients/{clientId} | Remove Client
*ConversationsApi* | [**create_conversation**](docs/ConversationsApi.md#create_conversation) | **POST** /v2/apps/{appId}/conversations | Create Conversation
*ConversationsApi* | [**delete_conversation**](docs/ConversationsApi.md#delete_conversation) | **DELETE** /v2/apps/{appId}/conversations/{conversationId} | Delete Conversation
*ConversationsApi* | [**get_conversation**](docs/ConversationsApi.md#get_conversation) | **GET** /v2/apps/{appId}/conversations/{conversationId} | Get Conversation
*ConversationsApi* | [**list_conversations**](docs/ConversationsApi.md#list_conversations) | **GET** /v2/apps/{appId}/conversations | List Conversations
*ConversationsApi* | [**update_conversation**](docs/ConversationsApi.md#update_conversation) | **PATCH** /v2/apps/{appId}/conversations/{conversationId} | Update Conversation
*CustomIntegrationApiKeysApi* | [**create_custom_integration_key**](docs/CustomIntegrationApiKeysApi.md#create_custom_integration_key) | **POST** /v2/apps/{appId}/integrations/{integrationId}/keys | Create Integration Key
*CustomIntegrationApiKeysApi* | [**delete_custom_integration_key**](docs/CustomIntegrationApiKeysApi.md#delete_custom_integration_key) | **DELETE** /v2/apps/{appId}/integrations/{integrationId}/keys/{keyId} | Delete Integration Key
*CustomIntegrationApiKeysApi* | [**get_custom_integration_key**](docs/CustomIntegrationApiKeysApi.md#get_custom_integration_key) | **GET** /v2/apps/{appId}/integrations/{integrationId}/keys/{keyId} | Get Integration Key
*CustomIntegrationApiKeysApi* | [**list_custom_integration_keys**](docs/CustomIntegrationApiKeysApi.md#list_custom_integration_keys) | **GET** /v2/apps/{appId}/integrations/{integrationId}/keys | List Integration Keys
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
 - [ActivityAllOf](docs/ActivityAllOf.md)
 - [ActivityPost](docs/ActivityPost.md)
 - [ActivityPostAllOf](docs/ActivityPostAllOf.md)
 - [ActivityTypes](docs/ActivityTypes.md)
 - [Android](docs/Android.md)
 - [AndroidAllOf](docs/AndroidAllOf.md)
 - [AndroidUpdate](docs/AndroidUpdate.md)
 - [AndroidUpdateAllOf](docs/AndroidUpdateAllOf.md)
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
 - [AppleAllOf](docs/AppleAllOf.md)
 - [AppleUpdate](docs/AppleUpdate.md)
 - [AttachmentDeleteBody](docs/AttachmentDeleteBody.md)
 - [AttachmentMediaTokenBody](docs/AttachmentMediaTokenBody.md)
 - [AttachmentMediaTokenResponse](docs/AttachmentMediaTokenResponse.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [AttachmentSchema](docs/AttachmentSchema.md)
 - [AttachmentUploadBody](docs/AttachmentUploadBody.md)
 - [Author](docs/Author.md)
 - [AuthorWebhook](docs/AuthorWebhook.md)
 - [Buy](docs/Buy.md)
 - [Campaign](docs/Campaign.md)
 - [CarouselMessage](docs/CarouselMessage.md)
 - [CarouselMessageDisplaySettings](docs/CarouselMessageDisplaySettings.md)
 - [Client](docs/Client.md)
 - [ClientAddEvent](docs/ClientAddEvent.md)
 - [ClientAddEventAllOf](docs/ClientAddEventAllOf.md)
 - [ClientAddEventAllOfPayload](docs/ClientAddEventAllOfPayload.md)
 - [ClientAssociation](docs/ClientAssociation.md)
 - [ClientCreate](docs/ClientCreate.md)
 - [ClientListResponse](docs/ClientListResponse.md)
 - [ClientRemoveEvent](docs/ClientRemoveEvent.md)
 - [ClientRemoveEventAllOf](docs/ClientRemoveEventAllOf.md)
 - [ClientRemoveEventAllOfPayload](docs/ClientRemoveEventAllOfPayload.md)
 - [ClientResponse](docs/ClientResponse.md)
 - [ClientType](docs/ClientType.md)
 - [ClientUpdateEvent](docs/ClientUpdateEvent.md)
 - [ClientUpdateEventAllOf](docs/ClientUpdateEventAllOf.md)
 - [ClientUpdateEventAllOfPayload](docs/ClientUpdateEventAllOfPayload.md)
 - [Confirmation](docs/Confirmation.md)
 - [Content](docs/Content.md)
 - [Conversation](docs/Conversation.md)
 - [ConversationAllOf](docs/ConversationAllOf.md)
 - [ConversationCreateBody](docs/ConversationCreateBody.md)
 - [ConversationCreateEvent](docs/ConversationCreateEvent.md)
 - [ConversationCreateEventAllOf](docs/ConversationCreateEventAllOf.md)
 - [ConversationCreateEventAllOfPayload](docs/ConversationCreateEventAllOfPayload.md)
 - [ConversationJoinEvent](docs/ConversationJoinEvent.md)
 - [ConversationJoinEventAllOf](docs/ConversationJoinEventAllOf.md)
 - [ConversationJoinEventAllOfPayload](docs/ConversationJoinEventAllOfPayload.md)
 - [ConversationLeaveEvent](docs/ConversationLeaveEvent.md)
 - [ConversationLeaveEventAllOf](docs/ConversationLeaveEventAllOf.md)
 - [ConversationLeaveEventAllOfPayload](docs/ConversationLeaveEventAllOfPayload.md)
 - [ConversationListFilter](docs/ConversationListFilter.md)
 - [ConversationListResponse](docs/ConversationListResponse.md)
 - [ConversationMessageDeliveryChannelEvent](docs/ConversationMessageDeliveryChannelEvent.md)
 - [ConversationMessageDeliveryChannelEventAllOf](docs/ConversationMessageDeliveryChannelEventAllOf.md)
 - [ConversationMessageDeliveryFailureEvent](docs/ConversationMessageDeliveryFailureEvent.md)
 - [ConversationMessageDeliveryFailureEventAllOf](docs/ConversationMessageDeliveryFailureEventAllOf.md)
 - [ConversationMessageDeliveryPayload](docs/ConversationMessageDeliveryPayload.md)
 - [ConversationMessageDeliveryPayloadDestination](docs/ConversationMessageDeliveryPayloadDestination.md)
 - [ConversationMessageDeliveryPayloadExternalMessages](docs/ConversationMessageDeliveryPayloadExternalMessages.md)
 - [ConversationMessageDeliveryPayloadMessage](docs/ConversationMessageDeliveryPayloadMessage.md)
 - [ConversationMessageDeliveryUserEvent](docs/ConversationMessageDeliveryUserEvent.md)
 - [ConversationMessageEvent](docs/ConversationMessageEvent.md)
 - [ConversationMessageEventAllOf](docs/ConversationMessageEventAllOf.md)
 - [ConversationMessageEventAllOfPayload](docs/ConversationMessageEventAllOfPayload.md)
 - [ConversationPostbackEvent](docs/ConversationPostbackEvent.md)
 - [ConversationPostbackEventAllOf](docs/ConversationPostbackEventAllOf.md)
 - [ConversationPostbackEventAllOfPayload](docs/ConversationPostbackEventAllOfPayload.md)
 - [ConversationReadEvent](docs/ConversationReadEvent.md)
 - [ConversationReadEventAllOf](docs/ConversationReadEventAllOf.md)
 - [ConversationReadEventAllOfPayload](docs/ConversationReadEventAllOfPayload.md)
 - [ConversationReferralEvent](docs/ConversationReferralEvent.md)
 - [ConversationReferralEventAllOf](docs/ConversationReferralEventAllOf.md)
 - [ConversationReferralEventAllOfPayload](docs/ConversationReferralEventAllOfPayload.md)
 - [ConversationRemoveEvent](docs/ConversationRemoveEvent.md)
 - [ConversationRemoveEventAllOf](docs/ConversationRemoveEventAllOf.md)
 - [ConversationRemoveEventAllOfPayload](docs/ConversationRemoveEventAllOfPayload.md)
 - [ConversationResponse](docs/ConversationResponse.md)
 - [ConversationTruncated](docs/ConversationTruncated.md)
 - [ConversationType](docs/ConversationType.md)
 - [ConversationTypingEvent](docs/ConversationTypingEvent.md)
 - [ConversationTypingEventAllOf](docs/ConversationTypingEventAllOf.md)
 - [ConversationTypingEventAllOfPayload](docs/ConversationTypingEventAllOfPayload.md)
 - [ConversationUpdateBody](docs/ConversationUpdateBody.md)
 - [Custom](docs/Custom.md)
 - [CustomAllOf](docs/CustomAllOf.md)
 - [CustomUpdate](docs/CustomUpdate.md)
 - [Destination](docs/Destination.md)
 - [Device](docs/Device.md)
 - [EventSubSchema](docs/EventSubSchema.md)
 - [ExtraChannelOptions](docs/ExtraChannelOptions.md)
 - [ExtraChannelOptionsMessenger](docs/ExtraChannelOptionsMessenger.md)
 - [Field](docs/Field.md)
 - [FileMessage](docs/FileMessage.md)
 - [FormMessage](docs/FormMessage.md)
 - [FormResponseMessage](docs/FormResponseMessage.md)
 - [Identity](docs/Identity.md)
 - [ImageMessage](docs/ImageMessage.md)
 - [InlineObject](docs/InlineObject.md)
 - [Instagram](docs/Instagram.md)
 - [InstagramAllOf](docs/InstagramAllOf.md)
 - [InstagramUpdate](docs/InstagramUpdate.md)
 - [InstagramUpdateAllOf](docs/InstagramUpdateAllOf.md)
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
 - [IosAllOf](docs/IosAllOf.md)
 - [IosUpdate](docs/IosUpdate.md)
 - [IosUpdateAllOf](docs/IosUpdateAllOf.md)
 - [Item](docs/Item.md)
 - [Line](docs/Line.md)
 - [LineAllOf](docs/LineAllOf.md)
 - [LineUpdate](docs/LineUpdate.md)
 - [Link](docs/Link.md)
 - [Links](docs/Links.md)
 - [ListMessage](docs/ListMessage.md)
 - [LocationMessage](docs/LocationMessage.md)
 - [LocationMessageCoordinates](docs/LocationMessageCoordinates.md)
 - [LocationMessageLocation](docs/LocationMessageLocation.md)
 - [LocationRequest](docs/LocationRequest.md)
 - [Mailgun](docs/Mailgun.md)
 - [MailgunAllOf](docs/MailgunAllOf.md)
 - [MailgunUpdate](docs/MailgunUpdate.md)
 - [MailgunUpdateAllOf](docs/MailgunUpdateAllOf.md)
 - [MatchCriteria](docs/MatchCriteria.md)
 - [MatchCriteriaBase](docs/MatchCriteriaBase.md)
 - [MatchCriteriaMailgun](docs/MatchCriteriaMailgun.md)
 - [MatchCriteriaMailgunAllOf](docs/MatchCriteriaMailgunAllOf.md)
 - [MatchCriteriaMessagebird](docs/MatchCriteriaMessagebird.md)
 - [MatchCriteriaMessagebirdAllOf](docs/MatchCriteriaMessagebirdAllOf.md)
 - [MatchCriteriaTwilio](docs/MatchCriteriaTwilio.md)
 - [MatchCriteriaTwilioAllOf](docs/MatchCriteriaTwilioAllOf.md)
 - [MatchCriteriaWhatsapp](docs/MatchCriteriaWhatsapp.md)
 - [MatchCriteriaWhatsappAllOf](docs/MatchCriteriaWhatsappAllOf.md)
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
 - [Messagebird](docs/Messagebird.md)
 - [MessagebirdAllOf](docs/MessagebirdAllOf.md)
 - [Messenger](docs/Messenger.md)
 - [MessengerAllOf](docs/MessengerAllOf.md)
 - [MessengerUpdate](docs/MessengerUpdate.md)
 - [Meta](docs/Meta.md)
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
 - [Reply](docs/Reply.md)
 - [Source](docs/Source.md)
 - [SourceWebhook](docs/SourceWebhook.md)
 - [SourceWithCampaignWebhook](docs/SourceWithCampaignWebhook.md)
 - [SourceWithCampaignWebhookAllOf](docs/SourceWithCampaignWebhookAllOf.md)
 - [Status](docs/Status.md)
 - [Switchboard](docs/Switchboard.md)
 - [SwitchboardAcceptControl](docs/SwitchboardAcceptControl.md)
 - [SwitchboardAcceptControlAllOf](docs/SwitchboardAcceptControlAllOf.md)
 - [SwitchboardAcceptControlAllOfPayload](docs/SwitchboardAcceptControlAllOfPayload.md)
 - [SwitchboardAcceptControlFailure](docs/SwitchboardAcceptControlFailure.md)
 - [SwitchboardAcceptControlFailureAllOf](docs/SwitchboardAcceptControlFailureAllOf.md)
 - [SwitchboardAcceptControlFailureAllOfPayload](docs/SwitchboardAcceptControlFailureAllOfPayload.md)
 - [SwitchboardIntegration](docs/SwitchboardIntegration.md)
 - [SwitchboardIntegrationCreateBody](docs/SwitchboardIntegrationCreateBody.md)
 - [SwitchboardIntegrationListResponse](docs/SwitchboardIntegrationListResponse.md)
 - [SwitchboardIntegrationResponse](docs/SwitchboardIntegrationResponse.md)
 - [SwitchboardIntegrationUpdateBody](docs/SwitchboardIntegrationUpdateBody.md)
 - [SwitchboardIntegrationWebhook](docs/SwitchboardIntegrationWebhook.md)
 - [SwitchboardListResponse](docs/SwitchboardListResponse.md)
 - [SwitchboardOfferControl](docs/SwitchboardOfferControl.md)
 - [SwitchboardOfferControlAllOf](docs/SwitchboardOfferControlAllOf.md)
 - [SwitchboardOfferControlAllOfPayload](docs/SwitchboardOfferControlAllOfPayload.md)
 - [SwitchboardOfferControlFailure](docs/SwitchboardOfferControlFailure.md)
 - [SwitchboardPassControl](docs/SwitchboardPassControl.md)
 - [SwitchboardPassControlAllOf](docs/SwitchboardPassControlAllOf.md)
 - [SwitchboardPassControlAllOfPayload](docs/SwitchboardPassControlAllOfPayload.md)
 - [SwitchboardPassControlFailure](docs/SwitchboardPassControlFailure.md)
 - [SwitchboardResponse](docs/SwitchboardResponse.md)
 - [SwitchboardUpdateBody](docs/SwitchboardUpdateBody.md)
 - [Target](docs/Target.md)
 - [Telegram](docs/Telegram.md)
 - [TelegramAllOf](docs/TelegramAllOf.md)
 - [TelegramUpdate](docs/TelegramUpdate.md)
 - [TemplateMessage](docs/TemplateMessage.md)
 - [TextMessage](docs/TextMessage.md)
 - [Twilio](docs/Twilio.md)
 - [TwilioAllOf](docs/TwilioAllOf.md)
 - [TwilioUpdate](docs/TwilioUpdate.md)
 - [Twitter](docs/Twitter.md)
 - [TwitterAllOf](docs/TwitterAllOf.md)
 - [TwitterUpdate](docs/TwitterUpdate.md)
 - [User](docs/User.md)
 - [UserAllOf](docs/UserAllOf.md)
 - [UserCreateBody](docs/UserCreateBody.md)
 - [UserMergeEvent](docs/UserMergeEvent.md)
 - [UserMergeEventAllOf](docs/UserMergeEventAllOf.md)
 - [UserMergeEventAllOfPayload](docs/UserMergeEventAllOfPayload.md)
 - [UserMergeEventAllOfPayloadMergedClients](docs/UserMergeEventAllOfPayloadMergedClients.md)
 - [UserMergeEventAllOfPayloadMergedConversations](docs/UserMergeEventAllOfPayloadMergedConversations.md)
 - [UserMergeEventAllOfPayloadMergedUsers](docs/UserMergeEventAllOfPayloadMergedUsers.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserTruncated](docs/UserTruncated.md)
 - [UserUpdateBody](docs/UserUpdateBody.md)
 - [UserUpdateEvent](docs/UserUpdateEvent.md)
 - [UserUpdateEventAllOf](docs/UserUpdateEventAllOf.md)
 - [UserUpdateEventAllOfPayload](docs/UserUpdateEventAllOfPayload.md)
 - [Viber](docs/Viber.md)
 - [ViberAllOf](docs/ViberAllOf.md)
 - [ViberUpdate](docs/ViberUpdate.md)
 - [Web](docs/Web.md)
 - [WebAllOf](docs/WebAllOf.md)
 - [WebUpdate](docs/WebUpdate.md)
 - [WebUpdateAllOf](docs/WebUpdateAllOf.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookBody](docs/WebhookBody.md)
 - [WebhookCreateBody](docs/WebhookCreateBody.md)
 - [WebhookListResponse](docs/WebhookListResponse.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookSubSchema](docs/WebhookSubSchema.md)
 - [Webview](docs/Webview.md)
 - [WhatsAppUpdate](docs/WhatsAppUpdate.md)
 - [WhatsAppUpdateAllOf](docs/WhatsAppUpdateAllOf.md)
 - [Whatsapp](docs/Whatsapp.md)
 - [WhatsappAllOf](docs/WhatsappAllOf.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author



