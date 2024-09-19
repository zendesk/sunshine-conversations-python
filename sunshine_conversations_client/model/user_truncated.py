# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 13.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class UserTruncated(object):
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
        'external_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId'
    }

    nulls = set()

    def __init__(self, id=None, external_id=Undefined(), local_vars_configuration=None):  # noqa: E501
        """UserTruncated - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._external_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.external_id = external_id

    @property
    def id(self):
        """Gets the id of this UserTruncated.  # noqa: E501

        The unique ID of the user.  # noqa: E501

        :return: The id of this UserTruncated.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserTruncated.

        The unique ID of the user.  # noqa: E501

        :param id: The id of this UserTruncated.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this UserTruncated.  # noqa: E501

        An optional ID that can also be used to retrieve the user.   # noqa: E501

        :return: The external_id of this UserTruncated.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserTruncated.

        An optional ID that can also be used to retrieve the user.   # noqa: E501

        :param external_id: The external_id of this UserTruncated.  # noqa: E501
        :type: str
        """
        if type(external_id) is Undefined:
            external_id = None
            self.nulls.discard("external_id")
        elif external_id is None:
            self.nulls.add("external_id")
        else:
            self.nulls.discard("external_id")

        self._external_id = external_id

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
        if not isinstance(other, UserTruncated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserTruncated):
            return True

        return self.to_dict() != other.to_dict()
