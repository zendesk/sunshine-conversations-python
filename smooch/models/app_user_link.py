# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customers' experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our official documentation.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppUserLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, skip_confirmation=None):
        """
        AppUserLink - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'skip_confirmation': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'skip_confirmation': 'skipConfirmation'
        }

        self._type = type
        self._skip_confirmation = skip_confirmation

    @property
    def type(self):
        """
        Gets the type of this AppUserLink.

        :return: The type of this AppUserLink.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppUserLink.

        :param type: The type of this AppUserLink.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def skip_confirmation(self):
        """
        Gets the skip_confirmation of this AppUserLink.

        :return: The skip_confirmation of this AppUserLink.
        :rtype: bool
        """
        return self._skip_confirmation

    @skip_confirmation.setter
    def skip_confirmation(self, skip_confirmation):
        """
        Sets the skip_confirmation of this AppUserLink.

        :param skip_confirmation: The skip_confirmation of this AppUserLink.
        :type: bool
        """

        self._skip_confirmation = skip_confirmation

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AppUserLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
