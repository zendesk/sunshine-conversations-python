# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MailgunUpdateAllOf(object):
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
        'hide_unsubscribe_link': 'bool',
        'from_address': 'str'
    }

    attribute_map = {
        'hide_unsubscribe_link': 'hideUnsubscribeLink',
        'from_address': 'fromAddress'
    }

    nulls = set()

    def __init__(self, hide_unsubscribe_link=None, from_address=Undefined(), local_vars_configuration=None):  # noqa: E501
        """MailgunUpdateAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hide_unsubscribe_link = None
        self._from_address = None
        self.discriminator = None

        if hide_unsubscribe_link is not None:
            self.hide_unsubscribe_link = hide_unsubscribe_link
        self.from_address = from_address

    @property
    def hide_unsubscribe_link(self):
        """Gets the hide_unsubscribe_link of this MailgunUpdateAllOf.  # noqa: E501

        A boolean value indicating whether the unsubscribe link should be omitted from outgoing emails. When enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. By default, the unsubscribe link will be included in all outgoing emails.  # noqa: E501

        :return: The hide_unsubscribe_link of this MailgunUpdateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._hide_unsubscribe_link

    @hide_unsubscribe_link.setter
    def hide_unsubscribe_link(self, hide_unsubscribe_link):
        """Sets the hide_unsubscribe_link of this MailgunUpdateAllOf.

        A boolean value indicating whether the unsubscribe link should be omitted from outgoing emails. When enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. By default, the unsubscribe link will be included in all outgoing emails.  # noqa: E501

        :param hide_unsubscribe_link: The hide_unsubscribe_link of this MailgunUpdateAllOf.  # noqa: E501
        :type: bool
        """

        self._hide_unsubscribe_link = hide_unsubscribe_link

    @property
    def from_address(self):
        """Gets the from_address of this MailgunUpdateAllOf.  # noqa: E501

        Email address to use as the From and Reply-To address if it must be different from incomingAddress. Only use this option if the address that you supply is configured to forward emails to the incomingAddress, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user’s email client. May be unset with null.  # noqa: E501

        :return: The from_address of this MailgunUpdateAllOf.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this MailgunUpdateAllOf.

        Email address to use as the From and Reply-To address if it must be different from incomingAddress. Only use this option if the address that you supply is configured to forward emails to the incomingAddress, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user’s email client. May be unset with null.  # noqa: E501

        :param from_address: The from_address of this MailgunUpdateAllOf.  # noqa: E501
        :type: str
        """
        if type(from_address) is Undefined:
            from_address = None
            self.nulls.discard("from_address")
        elif from_address is None:
            self.nulls.add("from_address")
        else:
            self.nulls.discard("from_address")
        if (self.local_vars_configuration.client_side_validation and
                from_address is not None and len(from_address) < 1):
            raise ValueError("Invalid value for `from_address`, length must be greater than or equal to `1`")  # noqa: E501

        self._from_address = from_address

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
        if not isinstance(other, MailgunUpdateAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MailgunUpdateAllOf):
            return True

        return self.to_dict() != other.to_dict()
