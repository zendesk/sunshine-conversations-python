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


class ViberAllOf(object):
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
        'token': 'str',
        'uri': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'token': 'token',
        'uri': 'uri',
        'account_id': 'accountId'
    }

    nulls = set()

    def __init__(self, type='viber', token=Undefined(), uri=None, account_id=None, local_vars_configuration=None):  # noqa: E501
        """ViberAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._token = None
        self._uri = None
        self._account_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if token is not None:
            self.token = token
        if uri is not None:
            self.uri = uri
        if account_id is not None:
            self.account_id = account_id

    @property
    def type(self):
        """Gets the type of this ViberAllOf.  # noqa: E501

        To configure a Viber integration, acquire the Viber Public Account token from the user and call the Create Integration endpoint.   # noqa: E501

        :return: The type of this ViberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ViberAllOf.

        To configure a Viber integration, acquire the Viber Public Account token from the user and call the Create Integration endpoint.   # noqa: E501

        :param type: The type of this ViberAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def token(self):
        """Gets the token of this ViberAllOf.  # noqa: E501

        Viber Public Account token.  # noqa: E501

        :return: The token of this ViberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ViberAllOf.

        Viber Public Account token.  # noqa: E501

        :param token: The token of this ViberAllOf.  # noqa: E501
        :type: str
        """
        if type(token) is Undefined:
            token = None
            self.nulls.discard("token")
        elif token is None:
            self.nulls.add("token")
        else:
            self.nulls.discard("token")
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) < 1):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

    @property
    def uri(self):
        """Gets the uri of this ViberAllOf.  # noqa: E501

        Unique URI of the Viber account.  # noqa: E501

        :return: The uri of this ViberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ViberAllOf.

        Unique URI of the Viber account.  # noqa: E501

        :param uri: The uri of this ViberAllOf.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def account_id(self):
        """Gets the account_id of this ViberAllOf.  # noqa: E501

        Unique ID of the Viber account.  # noqa: E501

        :return: The account_id of this ViberAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ViberAllOf.

        Unique ID of the Viber account.  # noqa: E501

        :param account_id: The account_id of this ViberAllOf.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

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
        if not isinstance(other, ViberAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ViberAllOf):
            return True

        return self.to_dict() != other.to_dict()
