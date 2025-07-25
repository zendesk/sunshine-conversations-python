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


class FormResponseMessage(object):
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
        'fields': 'list[FormResponseMessageField]',
        'text_fallback': 'str'
    }

    attribute_map = {
        'type': 'type',
        'fields': 'fields',
        'text_fallback': 'textFallback'
    }

    nulls = set()

    def __init__(self, type='formResponse', fields=None, text_fallback=None, local_vars_configuration=None):  # noqa: E501
        """FormResponseMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fields = None
        self._text_fallback = None
        self.discriminator = None

        self.type = type
        self.fields = fields
        if text_fallback is not None:
            self.text_fallback = text_fallback

    @property
    def type(self):
        """Gets the type of this FormResponseMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this FormResponseMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormResponseMessage.

        The type of message.  # noqa: E501

        :param type: The type of this FormResponseMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fields(self):
        """Gets the fields of this FormResponseMessage.  # noqa: E501

        Array of field objects that contain the submitted fields.  # noqa: E501

        :return: The fields of this FormResponseMessage.  # noqa: E501
        :rtype: list[FormResponseMessageField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this FormResponseMessage.

        Array of field objects that contain the submitted fields.  # noqa: E501

        :param fields: The fields of this FormResponseMessage.  # noqa: E501
        :type: list[FormResponseMessageField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def text_fallback(self):
        """Gets the text_fallback of this FormResponseMessage.  # noqa: E501

        A string containing the `label: value` of all fields, each separated by a newline character.  # noqa: E501

        :return: The text_fallback of this FormResponseMessage.  # noqa: E501
        :rtype: str
        """
        return self._text_fallback

    @text_fallback.setter
    def text_fallback(self, text_fallback):
        """Sets the text_fallback of this FormResponseMessage.

        A string containing the `label: value` of all fields, each separated by a newline character.  # noqa: E501

        :param text_fallback: The text_fallback of this FormResponseMessage.  # noqa: E501
        :type: str
        """

        self._text_fallback = text_fallback

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
        if not isinstance(other, FormResponseMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormResponseMessage):
            return True

        return self.to_dict() != other.to_dict()
