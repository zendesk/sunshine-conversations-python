# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Activity(object):
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
        'source': 'SourceWebhook',
        'author': 'AuthorWebhook'
    }

    attribute_map = {
        'type': 'type',
        'source': 'source',
        'author': 'author'
    }

    nulls = set()

    def __init__(self, type=None, source=None, author=None, local_vars_configuration=None):  # noqa: E501
        """Activity - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._source = None
        self._author = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if source is not None:
            self.source = source
        if author is not None:
            self.author = author

    @property
    def type(self):
        """Gets the type of this Activity.  # noqa: E501

        If the author type is `user`, only `conversation:read` is supported.  # noqa: E501

        :return: The type of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Activity.

        If the author type is `user`, only `conversation:read` is supported.  # noqa: E501

        :param type: The type of this Activity.  # noqa: E501
        :type: str
        """
        allowed_values = ["conversation:read", "typing:start", "typing:stop"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def source(self):
        """Gets the source of this Activity.  # noqa: E501

        The source of the activity.  # noqa: E501

        :return: The source of this Activity.  # noqa: E501
        :rtype: SourceWebhook
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Activity.

        The source of the activity.  # noqa: E501

        :param source: The source of this Activity.  # noqa: E501
        :type: SourceWebhook
        """

        self._source = source

    @property
    def author(self):
        """Gets the author of this Activity.  # noqa: E501


        :return: The author of this Activity.  # noqa: E501
        :rtype: AuthorWebhook
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Activity.


        :param author: The author of this Activity.  # noqa: E501
        :type: AuthorWebhook
        """

        self._author = author

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
        if not isinstance(other, Activity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Activity):
            return True

        return self.to_dict() != other.to_dict()
