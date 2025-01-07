# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ConversationPostbackEventAllOfPayload(object):
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
        'postback': 'PostbackWebhook',
        'conversation': 'ConversationTruncated',
        'user': 'User',
        'source': 'SourceWithCampaignWebhook'
    }

    attribute_map = {
        'postback': 'postback',
        'conversation': 'conversation',
        'user': 'user',
        'source': 'source'
    }

    nulls = set()

    def __init__(self, postback=None, conversation=None, user=None, source=None, local_vars_configuration=None):  # noqa: E501
        """ConversationPostbackEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._postback = None
        self._conversation = None
        self._user = None
        self._source = None
        self.discriminator = None

        if postback is not None:
            self.postback = postback
        if conversation is not None:
            self.conversation = conversation
        if user is not None:
            self.user = user
        if source is not None:
            self.source = source

    @property
    def postback(self):
        """Gets the postback of this ConversationPostbackEventAllOfPayload.  # noqa: E501

        The postback associated with the event.  # noqa: E501

        :return: The postback of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :rtype: PostbackWebhook
        """
        return self._postback

    @postback.setter
    def postback(self, postback):
        """Sets the postback of this ConversationPostbackEventAllOfPayload.

        The postback associated with the event.  # noqa: E501

        :param postback: The postback of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :type: PostbackWebhook
        """

        self._postback = postback

    @property
    def conversation(self):
        """Gets the conversation of this ConversationPostbackEventAllOfPayload.  # noqa: E501

        The conversation linked to the postback.  # noqa: E501

        :return: The conversation of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ConversationPostbackEventAllOfPayload.

        The conversation linked to the postback.  # noqa: E501

        :param conversation: The conversation of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def user(self):
        """Gets the user of this ConversationPostbackEventAllOfPayload.  # noqa: E501

        The user that triggered the postback.  # noqa: E501

        :return: The user of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ConversationPostbackEventAllOfPayload.

        The user that triggered the postback.  # noqa: E501

        :param user: The user of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def source(self):
        """Gets the source of this ConversationPostbackEventAllOfPayload.  # noqa: E501

        The source of the postback.  # noqa: E501

        :return: The source of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :rtype: SourceWithCampaignWebhook
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ConversationPostbackEventAllOfPayload.

        The source of the postback.  # noqa: E501

        :param source: The source of this ConversationPostbackEventAllOfPayload.  # noqa: E501
        :type: SourceWithCampaignWebhook
        """

        self._source = source

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
        if not isinstance(other, ConversationPostbackEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationPostbackEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
