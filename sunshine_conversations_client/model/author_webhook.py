# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class AuthorWebhook(object):
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
        'user_id': 'str',
        'user': 'User'
    }

    attribute_map = {
        'type': 'type',
        'user_id': 'userId',
        'user': 'user'
    }

    nulls = set()

    def __init__(self, type=None, user_id=None, user=None, local_vars_configuration=None):  # noqa: E501
        """AuthorWebhook - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._user_id = None
        self._user = None
        self.discriminator = None

        self.type = type
        if user_id is not None:
            self.user_id = user_id
        if user is not None:
            self.user = user

    @property
    def type(self):
        """Gets the type of this AuthorWebhook.  # noqa: E501

        The `type` of the author.  # noqa: E501

        :return: The type of this AuthorWebhook.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthorWebhook.

        The `type` of the author.  # noqa: E501

        :param type: The type of this AuthorWebhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["business", "user"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this AuthorWebhook.  # noqa: E501

        The id of the user. Only supported when author `type` is `user`.  # noqa: E501

        :return: The user_id of this AuthorWebhook.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuthorWebhook.

        The id of the user. Only supported when author `type` is `user`.  # noqa: E501

        :param user_id: The user_id of this AuthorWebhook.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user(self):
        """Gets the user of this AuthorWebhook.  # noqa: E501

        The user that authored the message or activity. `profile` is included in the payload if the `includeFullUser` option is enabled.  # noqa: E501

        :return: The user of this AuthorWebhook.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AuthorWebhook.

        The user that authored the message or activity. `profile` is included in the payload if the `includeFullUser` option is enabled.  # noqa: E501

        :param user: The user of this AuthorWebhook.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if not isinstance(other, AuthorWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthorWebhook):
            return True

        return self.to_dict() != other.to_dict()