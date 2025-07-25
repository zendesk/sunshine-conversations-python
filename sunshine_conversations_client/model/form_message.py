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


class FormMessage(object):
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
        'submitted': 'bool',
        'block_chat_input': 'bool',
        'fields': 'list[FormMessageField]'
    }

    attribute_map = {
        'type': 'type',
        'submitted': 'submitted',
        'block_chat_input': 'blockChatInput',
        'fields': 'fields'
    }

    nulls = set()

    def __init__(self, type='form', submitted=None, block_chat_input=None, fields=None, local_vars_configuration=None):  # noqa: E501
        """FormMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._submitted = None
        self._block_chat_input = None
        self._fields = None
        self.discriminator = None

        self.type = type
        if submitted is not None:
            self.submitted = submitted
        if block_chat_input is not None:
            self.block_chat_input = block_chat_input
        self.fields = fields

    @property
    def type(self):
        """Gets the type of this FormMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this FormMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormMessage.

        The type of message.  # noqa: E501

        :param type: The type of this FormMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def submitted(self):
        """Gets the submitted of this FormMessage.  # noqa: E501

        Flag which states whether the form is submitted.  # noqa: E501

        :return: The submitted of this FormMessage.  # noqa: E501
        :rtype: bool
        """
        return self._submitted

    @submitted.setter
    def submitted(self, submitted):
        """Sets the submitted of this FormMessage.

        Flag which states whether the form is submitted.  # noqa: E501

        :param submitted: The submitted of this FormMessage.  # noqa: E501
        :type: bool
        """

        self._submitted = submitted

    @property
    def block_chat_input(self):
        """Gets the block_chat_input of this FormMessage.  # noqa: E501

        When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user's ability to send messages in the conversation..  # noqa: E501

        :return: The block_chat_input of this FormMessage.  # noqa: E501
        :rtype: bool
        """
        return self._block_chat_input

    @block_chat_input.setter
    def block_chat_input(self, block_chat_input):
        """Sets the block_chat_input of this FormMessage.

        When set to true, the chat input will be disabled on supported client implementations when the message is the most recent one in the history. Can be used for guided flows or to temporarily disable the user's ability to send messages in the conversation..  # noqa: E501

        :param block_chat_input: The block_chat_input of this FormMessage.  # noqa: E501
        :type: bool
        """

        self._block_chat_input = block_chat_input

    @property
    def fields(self):
        """Gets the fields of this FormMessage.  # noqa: E501

        An array of objects representing fields associated with the message. Only present in form and formResponse messages.  # noqa: E501

        :return: The fields of this FormMessage.  # noqa: E501
        :rtype: list[FormMessageField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this FormMessage.

        An array of objects representing fields associated with the message. Only present in form and formResponse messages.  # noqa: E501

        :param fields: The fields of this FormMessage.  # noqa: E501
        :type: list[FormMessageField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

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
        if not isinstance(other, FormMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormMessage):
            return True

        return self.to_dict() != other.to_dict()
