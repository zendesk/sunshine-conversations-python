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


class LocationMessageCoordinates(object):
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
        'lat': 'float',
        'long': 'float'
    }

    attribute_map = {
        'lat': 'lat',
        'long': 'long'
    }

    nulls = set()

    def __init__(self, lat=None, long=None, local_vars_configuration=None):  # noqa: E501
        """LocationMessageCoordinates - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lat = None
        self._long = None
        self.discriminator = None

        self.lat = lat
        self.long = long

    @property
    def lat(self):
        """Gets the lat of this LocationMessageCoordinates.  # noqa: E501

        Global latitude.  # noqa: E501

        :return: The lat of this LocationMessageCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this LocationMessageCoordinates.

        Global latitude.  # noqa: E501

        :param lat: The lat of this LocationMessageCoordinates.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and lat is None:  # noqa: E501
            raise ValueError("Invalid value for `lat`, must not be `None`")  # noqa: E501

        self._lat = lat

    @property
    def long(self):
        """Gets the long of this LocationMessageCoordinates.  # noqa: E501

        Global longitude.  # noqa: E501

        :return: The long of this LocationMessageCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this LocationMessageCoordinates.

        Global longitude.  # noqa: E501

        :param long: The long of this LocationMessageCoordinates.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and long is None:  # noqa: E501
            raise ValueError("Invalid value for `long`, must not be `None`")  # noqa: E501

        self._long = long

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
        if not isinstance(other, LocationMessageCoordinates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationMessageCoordinates):
            return True

        return self.to_dict() != other.to_dict()
