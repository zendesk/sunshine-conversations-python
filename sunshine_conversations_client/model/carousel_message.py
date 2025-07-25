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


class CarouselMessage(object):
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
        'text': 'str',
        'block_chat_input': 'bool',
        'items': 'list[Item]',
        'display_settings': 'CarouselMessageDisplaySettings'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'block_chat_input': 'blockChatInput',
        'items': 'items',
        'display_settings': 'displaySettings'
    }

    nulls = set()

    def __init__(self, type='carousel', text=None, block_chat_input=None, items=None, display_settings=None, local_vars_configuration=None):  # noqa: E501
        """CarouselMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._block_chat_input = None
        self._items = None
        self._display_settings = None
        self.discriminator = None

        self.type = type
        if text is not None:
            self.text = text
        if block_chat_input is not None:
            self.block_chat_input = block_chat_input
        self.items = items
        if display_settings is not None:
            self.display_settings = display_settings

    @property
    def type(self):
        """Gets the type of this CarouselMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this CarouselMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CarouselMessage.

        The type of message.  # noqa: E501

        :param type: The type of this CarouselMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def text(self):
        """Gets the text of this CarouselMessage.  # noqa: E501

        The fallback text message used when carousel messages are not supported by the channel.  # noqa: E501

        :return: The text of this CarouselMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CarouselMessage.

        The fallback text message used when carousel messages are not supported by the channel.  # noqa: E501

        :param text: The text of this CarouselMessage.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def block_chat_input(self):
        """Gets the block_chat_input of this CarouselMessage.  # noqa: E501

        When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user's ability to send messages in the conversation.  # noqa: E501

        :return: The block_chat_input of this CarouselMessage.  # noqa: E501
        :rtype: bool
        """
        return self._block_chat_input

    @block_chat_input.setter
    def block_chat_input(self, block_chat_input):
        """Sets the block_chat_input of this CarouselMessage.

        When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user's ability to send messages in the conversation.  # noqa: E501

        :param block_chat_input: The block_chat_input of this CarouselMessage.  # noqa: E501
        :type: bool
        """

        self._block_chat_input = block_chat_input

    @property
    def items(self):
        """Gets the items of this CarouselMessage.  # noqa: E501

        An array of objects representing the items associated with the message. Only present in carousel and list type messages.  # noqa: E501

        :return: The items of this CarouselMessage.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CarouselMessage.

        An array of objects representing the items associated with the message. Only present in carousel and list type messages.  # noqa: E501

        :param items: The items of this CarouselMessage.  # noqa: E501
        :type: list[Item]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def display_settings(self):
        """Gets the display_settings of this CarouselMessage.  # noqa: E501


        :return: The display_settings of this CarouselMessage.  # noqa: E501
        :rtype: CarouselMessageDisplaySettings
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        """Sets the display_settings of this CarouselMessage.


        :param display_settings: The display_settings of this CarouselMessage.  # noqa: E501
        :type: CarouselMessageDisplaySettings
        """

        self._display_settings = display_settings

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
        if not isinstance(other, CarouselMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CarouselMessage):
            return True

        return self.to_dict() != other.to_dict()
