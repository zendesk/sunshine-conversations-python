# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MatchCriteria(object):
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
        'integration_id': 'str',
        'primary': 'bool',
        'address': 'str',
        'subject': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'integration_id': 'integrationId',
        'primary': 'primary',
        'address': 'address',
        'subject': 'subject',
        'phone_number': 'phoneNumber'
    }

    nulls = set()

    discriminator_value_class_map = {
    }

    def __init__(self, type='whatsapp', integration_id=None, primary=True, address=None, subject='New message from {appName}', phone_number=None, local_vars_configuration=None):  # noqa: E501
        """MatchCriteria - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._integration_id = None
        self._primary = None
        self._address = None
        self._subject = None
        self._phone_number = None
        self.discriminator = 'type'

        self.type = type
        self.integration_id = integration_id
        if primary is not None:
            self.primary = primary
        self.address = address
        if subject is not None:
            self.subject = subject
        self.phone_number = phone_number

    @property
    def type(self):
        """Gets the type of this MatchCriteria.  # noqa: E501

        The channel type.  # noqa: E501

        :return: The type of this MatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MatchCriteria.

        The channel type.  # noqa: E501

        :param type: The type of this MatchCriteria.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def integration_id(self):
        """Gets the integration_id of this MatchCriteria.  # noqa: E501

        The ID of the integration to link. Must match the provided type.  # noqa: E501

        :return: The integration_id of this MatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this MatchCriteria.

        The ID of the integration to link. Must match the provided type.  # noqa: E501

        :param integration_id: The integration_id of this MatchCriteria.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def primary(self):
        """Gets the primary of this MatchCriteria.  # noqa: E501

        Flag indicating whether the client will become the primary for the target conversation once linking is complete.  # noqa: E501

        :return: The primary of this MatchCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this MatchCriteria.

        Flag indicating whether the client will become the primary for the target conversation once linking is complete.  # noqa: E501

        :param primary: The primary of this MatchCriteria.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    @property
    def address(self):
        """Gets the address of this MatchCriteria.  # noqa: E501

        The user’s email address.  # noqa: E501

        :return: The address of this MatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MatchCriteria.

        The user’s email address.  # noqa: E501

        :param address: The address of this MatchCriteria.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def subject(self):
        """Gets the subject of this MatchCriteria.  # noqa: E501

        May be specified to set the subject for the outgoing email.  # noqa: E501

        :return: The subject of this MatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MatchCriteria.

        May be specified to set the subject for the outgoing email.  # noqa: E501

        :param subject: The subject of this MatchCriteria.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def phone_number(self):
        """Gets the phone_number of this MatchCriteria.  # noqa: E501

        The user’s phone number. It must contain the + prefix and the country code. Examples of valid phone numbers: +1 212-555-2368, +12125552368, +1 212 555 2368. Examples of invalid phone numbers: 212 555 2368, 1 212 555 2368.   # noqa: E501

        :return: The phone_number of this MatchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this MatchCriteria.

        The user’s phone number. It must contain the + prefix and the country code. Examples of valid phone numbers: +1 212-555-2368, +12125552368, +1 212 555 2368. Examples of invalid phone numbers: 212 555 2368, 1 212 555 2368.   # noqa: E501

        :param phone_number: The phone_number of this MatchCriteria.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

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
        if not isinstance(other, MatchCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchCriteria):
            return True

        return self.to_dict() != other.to_dict()
