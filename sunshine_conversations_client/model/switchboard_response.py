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


class SwitchboardResponse(object):
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
        'switchboard': 'Switchboard'
    }

    attribute_map = {
        'switchboard': 'switchboard'
    }

    nulls = set()

    def __init__(self, switchboard=None, local_vars_configuration=None):  # noqa: E501
        """SwitchboardResponse - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._switchboard = None
        self.discriminator = None

        if switchboard is not None:
            self.switchboard = switchboard

    @property
    def switchboard(self):
        """Gets the switchboard of this SwitchboardResponse.  # noqa: E501

        The switchboard.  # noqa: E501

        :return: The switchboard of this SwitchboardResponse.  # noqa: E501
        :rtype: Switchboard
        """
        return self._switchboard

    @switchboard.setter
    def switchboard(self, switchboard):
        """Sets the switchboard of this SwitchboardResponse.

        The switchboard.  # noqa: E501

        :param switchboard: The switchboard of this SwitchboardResponse.  # noqa: E501
        :type: Switchboard
        """

        self._switchboard = switchboard

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
        if not isinstance(other, SwitchboardResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardResponse):
            return True

        return self.to_dict() != other.to_dict()
