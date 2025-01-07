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


class ActivityMessage(object):
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
        'data': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data'
    }

    nulls = set()

    discriminator_value_class_map = {
    }

    def __init__(self, type='transferToEmail', data=None, local_vars_configuration=None):  # noqa: E501
        """ActivityMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._data = None
        self.discriminator = 'type'

        self.type = type
        if data is not None:
            self.data = data

    @property
    def type(self):
        """Gets the type of this ActivityMessage.  # noqa: E501

        The type of system activity that generated the message. The value of this field determines the dynamic content that is rendered to the end-user / agent when viewing this message. Each `type` value will have a set of pre-defined, localized strings that describe the activity.  # noqa: E501

        :return: The type of this ActivityMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ActivityMessage.

        The type of system activity that generated the message. The value of this field determines the dynamic content that is rendered to the end-user / agent when viewing this message. Each `type` value will have a set of pre-defined, localized strings that describe the activity.  # noqa: E501

        :param type: The type of this ActivityMessage.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def data(self):
        """Gets the data of this ActivityMessage.  # noqa: E501

        No additional data is supplied with the \"transferToEmail\" activity type at this time.  # noqa: E501

        :return: The data of this ActivityMessage.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ActivityMessage.

        No additional data is supplied with the \"transferToEmail\" activity type at this time.  # noqa: E501

        :param data: The data of this ActivityMessage.  # noqa: E501
        :type: dict(str, object)
        """

        self._data = data

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        if self.discriminator is None:
            return
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, ActivityMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActivityMessage):
            return True

        return self.to_dict() != other.to_dict()