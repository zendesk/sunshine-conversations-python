# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MatchCriteriaMailgunAllOf(object):
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
        'address': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'type': 'type',
        'address': 'address',
        'subject': 'subject'
    }

    nulls = set()

    def __init__(self, type='mailgun', address=None, subject='New message from {appName}', local_vars_configuration=None):  # noqa: E501
        """MatchCriteriaMailgunAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._address = None
        self._subject = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.address = address
        if subject is not None:
            self.subject = subject

    @property
    def type(self):
        """Gets the type of this MatchCriteriaMailgunAllOf.  # noqa: E501

        The channel type.  # noqa: E501

        :return: The type of this MatchCriteriaMailgunAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MatchCriteriaMailgunAllOf.

        The channel type.  # noqa: E501

        :param type: The type of this MatchCriteriaMailgunAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def address(self):
        """Gets the address of this MatchCriteriaMailgunAllOf.  # noqa: E501

        The user’s email address.  # noqa: E501

        :return: The address of this MatchCriteriaMailgunAllOf.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MatchCriteriaMailgunAllOf.

        The user’s email address.  # noqa: E501

        :param address: The address of this MatchCriteriaMailgunAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def subject(self):
        """Gets the subject of this MatchCriteriaMailgunAllOf.  # noqa: E501

        May be specified to set the subject for the outgoing email.  # noqa: E501

        :return: The subject of this MatchCriteriaMailgunAllOf.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MatchCriteriaMailgunAllOf.

        May be specified to set the subject for the outgoing email.  # noqa: E501

        :param subject: The subject of this MatchCriteriaMailgunAllOf.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if not isinstance(other, MatchCriteriaMailgunAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchCriteriaMailgunAllOf):
            return True

        return self.to_dict() != other.to_dict()
