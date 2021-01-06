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


class ConversationMessageEventAllOfPayload(object):
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
        'message': 'MessageWebhook',
        'recent_notifications': 'list[MessageWebhook]'
    }

    attribute_map = {
        'conversation': 'conversation',
        'message': 'message',
        'recent_notifications': 'recentNotifications'
    }

    nulls = set()

    def __init__(self, conversation=None, message=None, recent_notifications=None, local_vars_configuration=None):  # noqa: E501
        """ConversationMessageEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation = None
        self._message = None
        self._recent_notifications = None
        self.discriminator = None

        if conversation is not None:
            self.conversation = conversation
        if message is not None:
            self.message = message
        if recent_notifications is not None:
            self.recent_notifications = recent_notifications

    @property
    def conversation(self):
        """Gets the conversation of this ConversationMessageEventAllOfPayload.  # noqa: E501

        The conversation in which the message was sent.  # noqa: E501

        :return: The conversation of this ConversationMessageEventAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ConversationMessageEventAllOfPayload.

        The conversation in which the message was sent.  # noqa: E501

        :param conversation: The conversation of this ConversationMessageEventAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def message(self):
        """Gets the message of this ConversationMessageEventAllOfPayload.  # noqa: E501

        The message that was sent.  # noqa: E501

        :return: The message of this ConversationMessageEventAllOfPayload.  # noqa: E501
        :rtype: MessageWebhook
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConversationMessageEventAllOfPayload.

        The message that was sent.  # noqa: E501

        :param message: The message of this ConversationMessageEventAllOfPayload.  # noqa: E501
        :type: MessageWebhook
        """

        self._message = message

    @property
    def recent_notifications(self):
        """Gets the recent_notifications of this ConversationMessageEventAllOfPayload.  # noqa: E501

        Messages sent with the Notification API since the last user message.  # noqa: E501

        :return: The recent_notifications of this ConversationMessageEventAllOfPayload.  # noqa: E501
        :rtype: list[MessageWebhook]
        """
        return self._recent_notifications

    @recent_notifications.setter
    def recent_notifications(self, recent_notifications):
        """Sets the recent_notifications of this ConversationMessageEventAllOfPayload.

        Messages sent with the Notification API since the last user message.  # noqa: E501

        :param recent_notifications: The recent_notifications of this ConversationMessageEventAllOfPayload.  # noqa: E501
        :type: list[MessageWebhook]
        """

        self._recent_notifications = recent_notifications

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
        if not isinstance(other, ConversationMessageEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationMessageEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
