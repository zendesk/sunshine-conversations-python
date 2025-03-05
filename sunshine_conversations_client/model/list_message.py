# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ListMessage(object):
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
        'items': 'list[Item]',
        'actions': 'list[ActionSubset]'
    }

    attribute_map = {
        'type': 'type',
        'items': 'items',
        'actions': 'actions'
    }

    nulls = set()

    def __init__(self, type='list', items=None, actions=None, local_vars_configuration=None):  # noqa: E501
        """ListMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._items = None
        self._actions = None
        self.discriminator = None

        self.type = type
        self.items = items
        if actions is not None:
            self.actions = actions

    @property
    def type(self):
        """Gets the type of this ListMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this ListMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListMessage.

        The type of message.  # noqa: E501

        :param type: The type of this ListMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def items(self):
        """Gets the items of this ListMessage.  # noqa: E501

        An array of objects representing the items associated with the message. Only present in carousel and list type messages.  # noqa: E501

        :return: The items of this ListMessage.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListMessage.

        An array of objects representing the items associated with the message. Only present in carousel and list type messages.  # noqa: E501

        :param items: The items of this ListMessage.  # noqa: E501
        :type: list[Item]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def actions(self):
        """Gets the actions of this ListMessage.  # noqa: E501

        An array of objects representing the actions associated with the message. The array length is limited by the third party channel.  # noqa: E501

        :return: The actions of this ListMessage.  # noqa: E501
        :rtype: list[ActionSubset]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListMessage.

        An array of objects representing the actions associated with the message. The array length is limited by the third party channel.  # noqa: E501

        :param actions: The actions of this ListMessage.  # noqa: E501
        :type: list[ActionSubset]
        """

        self._actions = actions

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
        if not isinstance(other, ListMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListMessage):
            return True

        return self.to_dict() != other.to_dict()
