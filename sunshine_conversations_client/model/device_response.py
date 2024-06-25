# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class DeviceResponse(object):
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
        'device': 'Device'
    }

    attribute_map = {
        'device': 'device'
    }

    nulls = set()

    def __init__(self, device=None, local_vars_configuration=None):  # noqa: E501
        """DeviceResponse - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device = None
        self.discriminator = None

        if device is not None:
            self.device = device

    @property
    def device(self):
        """Gets the device of this DeviceResponse.  # noqa: E501

        The device.  # noqa: E501

        :return: The device of this DeviceResponse.  # noqa: E501
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceResponse.

        The device.  # noqa: E501

        :param device: The device of this DeviceResponse.  # noqa: E501
        :type: Device
        """

        self._device = device

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
        if not isinstance(other, DeviceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceResponse):
            return True

        return self.to_dict() != other.to_dict()
