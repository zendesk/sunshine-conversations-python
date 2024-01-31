# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Page(object):
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
        'after': 'str',
        'before': 'str',
        'size': 'int'
    }

    attribute_map = {
        'after': 'after',
        'before': 'before',
        'size': 'size'
    }

    nulls = set()

    def __init__(self, after=None, before=None, size=25, local_vars_configuration=None):  # noqa: E501
        """Page - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._after = None
        self._before = None
        self._size = None
        self.discriminator = None

        if after is not None:
            self.after = after
        if before is not None:
            self.before = before
        if size is not None:
            self.size = size

    @property
    def after(self):
        """Gets the after of this Page.  # noqa: E501

        A record id. Results will only contain the records that come after the specified record.  Only one of `after` or `before` can be provided, not both.   # noqa: E501

        :return: The after of this Page.  # noqa: E501
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this Page.

        A record id. Results will only contain the records that come after the specified record.  Only one of `after` or `before` can be provided, not both.   # noqa: E501

        :param after: The after of this Page.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                after is not None and len(after) > 24):
            raise ValueError("Invalid value for `after`, length must be less than or equal to `24`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                after is not None and len(after) < 24):
            raise ValueError("Invalid value for `after`, length must be greater than or equal to `24`")  # noqa: E501

        self._after = after

    @property
    def before(self):
        """Gets the before of this Page.  # noqa: E501

        A record id. Results will only contain the records that come before the specified record. Only one of `after` or `before` can be provided, not both.   # noqa: E501

        :return: The before of this Page.  # noqa: E501
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this Page.

        A record id. Results will only contain the records that come before the specified record. Only one of `after` or `before` can be provided, not both.   # noqa: E501

        :param before: The before of this Page.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                before is not None and len(before) > 24):
            raise ValueError("Invalid value for `before`, length must be less than or equal to `24`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                before is not None and len(before) < 24):
            raise ValueError("Invalid value for `before`, length must be greater than or equal to `24`")  # noqa: E501

        self._before = before

    @property
    def size(self):
        """Gets the size of this Page.  # noqa: E501

        The number of records to return. Does not apply to the `listMessages` endpoint.  # noqa: E501

        :return: The size of this Page.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Page.

        The number of records to return. Does not apply to the `listMessages` endpoint.  # noqa: E501

        :param size: The size of this Page.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size > 100):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 1):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._size = size

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
        if not isinstance(other, Page):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Page):
            return True

        return self.to_dict() != other.to_dict()
