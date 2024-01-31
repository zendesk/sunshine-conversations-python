# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class AndroidUpdate(object):
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
        'display_name': 'str',
        'server_key': 'str',
        'sender_id': 'str',
        'can_user_create_more_conversations': 'bool'
    }

    attribute_map = {
        'display_name': 'displayName',
        'server_key': 'serverKey',
        'sender_id': 'senderId',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations'
    }

    nulls = set()

    def __init__(self, display_name=Undefined(), server_key=Undefined(), sender_id=Undefined(), can_user_create_more_conversations=None, local_vars_configuration=None):  # noqa: E501
        """AndroidUpdate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._server_key = None
        self._sender_id = None
        self._can_user_create_more_conversations = None
        self.discriminator = None

        self.display_name = display_name
        self.server_key = server_key
        self.sender_id = sender_id
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def display_name(self):
        """Gets the display_name of this AndroidUpdate.  # noqa: E501

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :return: The display_name of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AndroidUpdate.

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :param display_name: The display_name of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 100):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def server_key(self):
        """Gets the server_key of this AndroidUpdate.  # noqa: E501

        Your server key from the fcm console.  # noqa: E501

        :return: The server_key of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """Sets the server_key of this AndroidUpdate.

        Your server key from the fcm console.  # noqa: E501

        :param server_key: The server_key of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(server_key) is Undefined:
            server_key = None
            self.nulls.discard("server_key")
        elif server_key is None:
            self.nulls.add("server_key")
        else:
            self.nulls.discard("server_key")
        if (self.local_vars_configuration.client_side_validation and
                server_key is not None and len(server_key) < 1):
            raise ValueError("Invalid value for `server_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_key = server_key

    @property
    def sender_id(self):
        """Gets the sender_id of this AndroidUpdate.  # noqa: E501

        Your sender id from the fcm console.  # noqa: E501

        :return: The sender_id of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this AndroidUpdate.

        Your sender id from the fcm console.  # noqa: E501

        :param sender_id: The sender_id of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(sender_id) is Undefined:
            sender_id = None
            self.nulls.discard("sender_id")
        elif sender_id is None:
            self.nulls.add("sender_id")
        else:
            self.nulls.discard("sender_id")
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and len(sender_id) < 1):
            raise ValueError("Invalid value for `sender_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this AndroidUpdate.  # noqa: E501

        Allows users to create more than one conversation on the android integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this AndroidUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this AndroidUpdate.

        Allows users to create more than one conversation on the android integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this AndroidUpdate.  # noqa: E501
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
        if not isinstance(other, AndroidUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidUpdate):
            return True

        return self.to_dict() != other.to_dict()
