# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.8.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class LocationMessage(object):
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
        'coordinates': 'LocationMessageCoordinates',
        'location': 'LocationMessageLocation'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'coordinates': 'coordinates',
        'location': 'location'
    }

    nulls = set()

    def __init__(self, type='location', text=None, coordinates=None, location=None, local_vars_configuration=None):  # noqa: E501
        """LocationMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._coordinates = None
        self._location = None
        self.discriminator = None

        self.type = type
        if text is not None:
            self.text = text
        self.coordinates = coordinates
        if location is not None:
            self.location = location

    @property
    def type(self):
        """Gets the type of this LocationMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this LocationMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LocationMessage.

        The type of message.  # noqa: E501

        :param type: The type of this LocationMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def text(self):
        """Gets the text of this LocationMessage.  # noqa: E501

        The fallback text message used when location messages are not supported by the channel.  # noqa: E501

        :return: The text of this LocationMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this LocationMessage.

        The fallback text message used when location messages are not supported by the channel.  # noqa: E501

        :param text: The text of this LocationMessage.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def coordinates(self):
        """Gets the coordinates of this LocationMessage.  # noqa: E501


        :return: The coordinates of this LocationMessage.  # noqa: E501
        :rtype: LocationMessageCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this LocationMessage.


        :param coordinates: The coordinates of this LocationMessage.  # noqa: E501
        :type: LocationMessageCoordinates
        """
        if self.local_vars_configuration.client_side_validation and coordinates is None:  # noqa: E501
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

    @property
    def location(self):
        """Gets the location of this LocationMessage.  # noqa: E501


        :return: The location of this LocationMessage.  # noqa: E501
        :rtype: LocationMessageLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this LocationMessage.


        :param location: The location of this LocationMessage.  # noqa: E501
        :type: LocationMessageLocation
        """

        self._location = location

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
        if not isinstance(other, LocationMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationMessage):
            return True

        return self.to_dict() != other.to_dict()
