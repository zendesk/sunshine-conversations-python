# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class UnityAllOf(object):
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
        'type': 'str',
        'can_user_see_conversation_list': 'bool',
        'can_user_create_more_conversations': 'bool',
        'attachments_enabled': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'can_user_see_conversation_list': 'canUserSeeConversationList',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations',
        'attachments_enabled': 'attachmentsEnabled'
    }

    nulls = set()

    def __init__(self, type='unity', can_user_see_conversation_list=None, can_user_create_more_conversations=None, attachments_enabled=None, local_vars_configuration=None):  # noqa: E501
        """UnityAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._can_user_see_conversation_list = None
        self._can_user_create_more_conversations = None
        self._attachments_enabled = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if can_user_see_conversation_list is not None:
            self.can_user_see_conversation_list = can_user_see_conversation_list
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations
        if attachments_enabled is not None:
            self.attachments_enabled = attachments_enabled

    @property
    def type(self):
        """Gets the type of this UnityAllOf.  # noqa: E501

        To configure a Unity integration, create an integration with type 'unity' by calling the Create Integration endpoint.   # noqa: E501

        :return: The type of this UnityAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UnityAllOf.

        To configure a Unity integration, create an integration with type 'unity' by calling the Create Integration endpoint.   # noqa: E501

        :param type: The type of this UnityAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def can_user_see_conversation_list(self):
        """Gets the can_user_see_conversation_list of this UnityAllOf.  # noqa: E501

        Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where `settings.multiConvoEnabled` is set to `true`*.   # noqa: E501

        :return: The can_user_see_conversation_list of this UnityAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_see_conversation_list

    @can_user_see_conversation_list.setter
    def can_user_see_conversation_list(self, can_user_see_conversation_list):
        """Sets the can_user_see_conversation_list of this UnityAllOf.

        Allows users to view their list of conversations. By default, the list of conversations will be visible. *This setting only applies to apps where `settings.multiConvoEnabled` is set to `true`*.   # noqa: E501

        :param can_user_see_conversation_list: The can_user_see_conversation_list of this UnityAllOf.  # noqa: E501
        :type: bool
        """

        self._can_user_see_conversation_list = can_user_see_conversation_list

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this UnityAllOf.  # noqa: E501

        Allows users to create more than one conversation on the Unity integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this UnityAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this UnityAllOf.

        Allows users to create more than one conversation on the Unity integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this UnityAllOf.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def attachments_enabled(self):
        """Gets the attachments_enabled of this UnityAllOf.  # noqa: E501

        Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.   # noqa: E501

        :return: The attachments_enabled of this UnityAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._attachments_enabled

    @attachments_enabled.setter
    def attachments_enabled(self, attachments_enabled):
        """Sets the attachments_enabled of this UnityAllOf.

        Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.   # noqa: E501

        :param attachments_enabled: The attachments_enabled of this UnityAllOf.  # noqa: E501
        :type: bool
        """

        self._attachments_enabled = attachments_enabled

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
        if not isinstance(other, UnityAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnityAllOf):
            return True

        return self.to_dict() != other.to_dict()
