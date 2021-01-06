# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ConversationCreateEventAllOfPayload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'conversation': 'ConversationTruncated',
        'creation_reason': 'str',
        'source': 'SourceWebhook',
        'user': 'User',
        'referral': 'Referral'
    }

    attribute_map = {
        'conversation': 'conversation',
        'creation_reason': 'creationReason',
        'source': 'source',
        'user': 'user',
        'referral': 'referral'
    }

    nulls = set()

    def __init__(self, conversation=None, creation_reason=None, source=None, user=Undefined(), referral=Undefined(), local_vars_configuration=None):  # noqa: E501
        """ConversationCreateEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation = None
        self._creation_reason = None
        self._source = None
        self._user = None
        self._referral = None
        self.discriminator = None

        if conversation is not None:
            self.conversation = conversation
        if creation_reason is not None:
            self.creation_reason = creation_reason
        if source is not None:
            self.source = source
        self.user = user
        self.referral = referral

    @property
    def conversation(self):
        """Gets the conversation of this ConversationCreateEventAllOfPayload.  # noqa: E501

        The conversation that was created.  # noqa: E501

        :return: The conversation of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ConversationCreateEventAllOfPayload.

        The conversation that was created.  # noqa: E501

        :param conversation: The conversation of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def creation_reason(self):
        """Gets the creation_reason of this ConversationCreateEventAllOfPayload.  # noqa: E501

        The reason why the conversation was created, if applicable. * `linkRequest` - The conversation was created in order to generate a link request to transfer the user to a different channel. * `message` - The conversation was created because a message was sent. * `none` - The conversation was not created for a specific purpose. Used primarily when a conversation is created via the Create Conversation API. * `notification` - The conversation was created by a call to the Notification API. * `prechatCapture` - The conversation was created because the user completed a prechat capture form in the Web Messenger. * `startConversation` - The conversation was created because of a call to the startConversation API on one of the SDK integrations, or a start conversation event was triggered from a messaging channel.   # noqa: E501

        :return: The creation_reason of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :rtype: str
        """
        return self._creation_reason

    @creation_reason.setter
    def creation_reason(self, creation_reason):
        """Sets the creation_reason of this ConversationCreateEventAllOfPayload.

        The reason why the conversation was created, if applicable. * `linkRequest` - The conversation was created in order to generate a link request to transfer the user to a different channel. * `message` - The conversation was created because a message was sent. * `none` - The conversation was not created for a specific purpose. Used primarily when a conversation is created via the Create Conversation API. * `notification` - The conversation was created by a call to the Notification API. * `prechatCapture` - The conversation was created because the user completed a prechat capture form in the Web Messenger. * `startConversation` - The conversation was created because of a call to the startConversation API on one of the SDK integrations, or a start conversation event was triggered from a messaging channel.   # noqa: E501

        :param creation_reason: The creation_reason of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["linkRequest", "message", "none", "notification", "prechatCapture", "startConversation"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and creation_reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `creation_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(creation_reason, allowed_values)
            )

        self._creation_reason = creation_reason

    @property
    def source(self):
        """Gets the source of this ConversationCreateEventAllOfPayload.  # noqa: E501

        The source of the creation.  # noqa: E501

        :return: The source of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :rtype: SourceWebhook
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ConversationCreateEventAllOfPayload.

        The source of the creation.  # noqa: E501

        :param source: The source of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :type: SourceWebhook
        """

        self._source = source

    @property
    def user(self):
        """Gets the user of this ConversationCreateEventAllOfPayload.  # noqa: E501

        The user associated with the conversation. Only present if the created conversation was of type personal. For sdkGroup conversations, the list of participants can be fetched using the List Participants API, if required.  # noqa: E501

        :return: The user of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ConversationCreateEventAllOfPayload.

        The user associated with the conversation. Only present if the created conversation was of type personal. For sdkGroup conversations, the list of participants can be fetched using the List Participants API, if required.  # noqa: E501

        :param user: The user of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :type: User
        """
        if type(user) is Undefined:
            user = None
            self.nulls.discard("user")
        elif user is None:
            self.nulls.add("user")
        else:
            self.nulls.discard("user")

        self._user = user

    @property
    def referral(self):
        """Gets the referral of this ConversationCreateEventAllOfPayload.  # noqa: E501

        Referral information, if applicable.  # noqa: E501

        :return: The referral of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :rtype: Referral
        """
        return self._referral

    @referral.setter
    def referral(self, referral):
        """Sets the referral of this ConversationCreateEventAllOfPayload.

        Referral information, if applicable.  # noqa: E501

        :param referral: The referral of this ConversationCreateEventAllOfPayload.  # noqa: E501
        :type: Referral
        """
        if type(referral) is Undefined:
            referral = None
            self.nulls.discard("referral")
        elif referral is None:
            self.nulls.add("referral")
        else:
            self.nulls.discard("referral")

        self._referral = referral

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConversationCreateEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationCreateEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
