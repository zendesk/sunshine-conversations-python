# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class InlineObject(object):
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
        'code': 'str',
        'grant_type': 'str',
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'code': 'code',
        'grant_type': 'grant_type',
        'client_id': 'client_id',
        'client_secret': 'client_secret'
    }

    nulls = set()

    def __init__(self, code=None, grant_type=None, client_id=None, client_secret=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._grant_type = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None

        self.code = code
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret

    @property
    def code(self):
        """Gets the code of this InlineObject.  # noqa: E501

        The authorization code received via /oauth/authorize  # noqa: E501

        :return: The code of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineObject.

        The authorization code received via /oauth/authorize  # noqa: E501

        :param code: The code of this InlineObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def grant_type(self):
        """Gets the grant_type of this InlineObject.  # noqa: E501

        Must be set to the string `authorization_code`  # noqa: E501

        :return: The grant_type of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this InlineObject.

        Must be set to the string `authorization_code`  # noqa: E501

        :param grant_type: The grant_type of this InlineObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and grant_type is None:  # noqa: E501
            raise ValueError("Invalid value for `grant_type`, must not be `None`")  # noqa: E501

        self._grant_type = grant_type

    @property
    def client_id(self):
        """Gets the client_id of this InlineObject.  # noqa: E501

        Your integration’s unique identifier  # noqa: E501

        :return: The client_id of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this InlineObject.

        Your integration’s unique identifier  # noqa: E501

        :param client_id: The client_id of this InlineObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this InlineObject.  # noqa: E501

        Your integration’s secret  # noqa: E501

        :return: The client_secret of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this InlineObject.

        Your integration’s secret  # noqa: E501

        :param client_secret: The client_secret of this InlineObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

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
        if not isinstance(other, InlineObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject):
            return True

        return self.to_dict() != other.to_dict()
