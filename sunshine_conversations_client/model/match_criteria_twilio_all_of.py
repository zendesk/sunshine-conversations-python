# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MatchCriteriaTwilioAllOf(object):
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
        'phone_number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'phone_number': 'phoneNumber'
    }

    nulls = set()

    def __init__(self, type='twilio', phone_number=None, local_vars_configuration=None):  # noqa: E501
        """MatchCriteriaTwilioAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._phone_number = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.phone_number = phone_number

    @property
    def type(self):
        """Gets the type of this MatchCriteriaTwilioAllOf.  # noqa: E501

        The channel type.  # noqa: E501

        :return: The type of this MatchCriteriaTwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MatchCriteriaTwilioAllOf.

        The channel type.  # noqa: E501

        :param type: The type of this MatchCriteriaTwilioAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def phone_number(self):
        """Gets the phone_number of this MatchCriteriaTwilioAllOf.  # noqa: E501

        The user’s phone number. It must contain the + prefix and the country code. Examples of valid phone numbers: +1 212-555-2368, +12125552368, +1 212 555 2368. Examples of invalid phone numbers: 212 555 2368, 1 212 555 2368.   # noqa: E501

        :return: The phone_number of this MatchCriteriaTwilioAllOf.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this MatchCriteriaTwilioAllOf.

        The user’s phone number. It must contain the + prefix and the country code. Examples of valid phone numbers: +1 212-555-2368, +12125552368, +1 212 555 2368. Examples of invalid phone numbers: 212 555 2368, 1 212 555 2368.   # noqa: E501

        :param phone_number: The phone_number of this MatchCriteriaTwilioAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

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
        if not isinstance(other, MatchCriteriaTwilioAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchCriteriaTwilioAllOf):
            return True

        return self.to_dict() != other.to_dict()
