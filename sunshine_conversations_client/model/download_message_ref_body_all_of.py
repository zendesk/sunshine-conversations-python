# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class DownloadMessageRefBodyAllOf(object):
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
        'user_id': 'str',
        'apple': 'DownloadMessageRefBodyAllOfApple'
    }

    attribute_map = {
        'user_id': 'userId',
        'apple': 'apple'
    }

    nulls = set()

    def __init__(self, user_id=None, apple=None, local_vars_configuration=None):  # noqa: E501
        """DownloadMessageRefBodyAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._apple = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if apple is not None:
            self.apple = apple

    @property
    def user_id(self):
        """Gets the user_id of this DownloadMessageRefBodyAllOf.  # noqa: E501

        The id of the user.  # noqa: E501

        :return: The user_id of this DownloadMessageRefBodyAllOf.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DownloadMessageRefBodyAllOf.

        The id of the user.  # noqa: E501

        :param user_id: The user_id of this DownloadMessageRefBodyAllOf.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def apple(self):
        """Gets the apple of this DownloadMessageRefBodyAllOf.  # noqa: E501


        :return: The apple of this DownloadMessageRefBodyAllOf.  # noqa: E501
        :rtype: DownloadMessageRefBodyAllOfApple
        """
        return self._apple

    @apple.setter
    def apple(self, apple):
        """Sets the apple of this DownloadMessageRefBodyAllOf.


        :param apple: The apple of this DownloadMessageRefBodyAllOf.  # noqa: E501
        :type: DownloadMessageRefBodyAllOfApple
        """

        self._apple = apple

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
        if not isinstance(other, DownloadMessageRefBodyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DownloadMessageRefBodyAllOf):
            return True

        return self.to_dict() != other.to_dict()
