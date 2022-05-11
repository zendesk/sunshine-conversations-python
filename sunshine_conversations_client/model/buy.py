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


class Buy(object):
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
        'amount': 'int',
        'currency': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'amount': 'amount',
        'currency': 'currency',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, type='buy', text=None, amount=None, currency=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Buy - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._amount = None
        self._currency = None
        self._metadata = None
        self.discriminator = None

        self.type = type
        self.text = text
        self.amount = amount
        if currency is not None:
            self.currency = currency
        self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this Buy.  # noqa: E501

        The type of action.  # noqa: E501

        :return: The type of this Buy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Buy.

        The type of action.  # noqa: E501

        :param type: The type of this Buy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def text(self):
        """Gets the text of this Buy.  # noqa: E501

        The button text.  # noqa: E501

        :return: The text of this Buy.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Buy.

        The button text.  # noqa: E501

        :param text: The text of this Buy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def amount(self):
        """Gets the amount of this Buy.  # noqa: E501

        The amount being charged. It needs to be specified in cents and is an integer (9.99$ -> 999).  # noqa: E501

        :return: The amount of this Buy.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Buy.

        The amount being charged. It needs to be specified in cents and is an integer (9.99$ -> 999).  # noqa: E501

        :param amount: The amount of this Buy.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Buy.  # noqa: E501

        An ISO 4217 standard currency code in lowercase. Used for actions of type buy.  # noqa: E501

        :return: The currency of this Buy.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Buy.

        An ISO 4217 standard currency code in lowercase. Used for actions of type buy.  # noqa: E501

        :param currency: The currency of this Buy.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def metadata(self):
        """Gets the metadata of this Buy.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this Buy.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Buy.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this Buy.  # noqa: E501
        :type: object
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

        self._metadata = metadata

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
        if not isinstance(other, Buy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Buy):
            return True

        return self.to_dict() != other.to_dict()
