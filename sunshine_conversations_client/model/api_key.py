# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ApiKey(object):
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
        'id': 'str',
        'display_name': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'secret': 'secret'
    }

    nulls = set()

    def __init__(self, id=None, display_name=None, secret=None, local_vars_configuration=None):  # noqa: E501
        """ApiKey - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._secret = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if secret is not None:
            self.secret = secret

    @property
    def id(self):
        """Gets the id of this ApiKey.  # noqa: E501

        The unique ID of the API key, used when signing JWTs or accessing the API using Basic Authentication.  # noqa: E501

        :return: The id of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiKey.

        The unique ID of the API key, used when signing JWTs or accessing the API using Basic Authentication.  # noqa: E501

        :param id: The id of this ApiKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this ApiKey.  # noqa: E501

        The name of the API key.  # noqa: E501

        :return: The display_name of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ApiKey.

        The name of the API key.  # noqa: E501

        :param display_name: The display_name of this ApiKey.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def secret(self):
        """Gets the secret of this ApiKey.  # noqa: E501

        The secret of the API key, used when signing JWTs or accessing the API using Basic Authentication  # noqa: E501

        :return: The secret of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ApiKey.

        The secret of the API key, used when signing JWTs or accessing the API using Basic Authentication  # noqa: E501

        :param secret: The secret of this ApiKey.  # noqa: E501
        :type: str
        """

        self._secret = secret

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
        if not isinstance(other, ApiKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiKey):
            return True

        return self.to_dict() != other.to_dict()
