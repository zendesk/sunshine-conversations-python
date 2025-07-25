# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class UnityUpdateAllOf(object):
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
        'can_user_see_conversation_list': 'bool',
        'can_user_create_more_conversations': 'bool'
    }

    attribute_map = {
        'can_user_see_conversation_list': 'canUserSeeConversationList',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations'
    }

    nulls = set()

    def __init__(self, can_user_see_conversation_list=None, can_user_create_more_conversations=None, local_vars_configuration=None):  # noqa: E501
        """UnityUpdateAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._can_user_see_conversation_list = None
        self._can_user_create_more_conversations = None
        self.discriminator = None

        if can_user_see_conversation_list is not None:
            self.can_user_see_conversation_list = can_user_see_conversation_list
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def can_user_see_conversation_list(self):
        """Gets the can_user_see_conversation_list of this UnityUpdateAllOf.  # noqa: E501

        Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where `settings.multiConvoEnabled` is set to `true`*.   # noqa: E501

        :return: The can_user_see_conversation_list of this UnityUpdateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_see_conversation_list

    @can_user_see_conversation_list.setter
    def can_user_see_conversation_list(self, can_user_see_conversation_list):
        """Sets the can_user_see_conversation_list of this UnityUpdateAllOf.

        Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where `settings.multiConvoEnabled` is set to `true`*.   # noqa: E501

        :param can_user_see_conversation_list: The can_user_see_conversation_list of this UnityUpdateAllOf.  # noqa: E501
        :type: bool
        """

        self._can_user_see_conversation_list = can_user_see_conversation_list

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this UnityUpdateAllOf.  # noqa: E501

        Allows users to create more than one conversation on the Unity integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this UnityUpdateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this UnityUpdateAllOf.

        Allows users to create more than one conversation on the Unity integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this UnityUpdateAllOf.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

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
        if not isinstance(other, UnityUpdateAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnityUpdateAllOf):
            return True

        return self.to_dict() != other.to_dict()
