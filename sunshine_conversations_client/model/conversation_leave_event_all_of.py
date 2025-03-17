# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ConversationLeaveEventAllOf(object):
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
        'payload': 'ConversationLeaveEventAllOfPayload'
    }

    attribute_map = {
        'payload': 'payload'
    }

    nulls = set()

    def __init__(self, payload=None, local_vars_configuration=None):  # noqa: E501
        """ConversationLeaveEventAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payload = None
        self.discriminator = None

        if payload is not None:
            self.payload = payload

    @property
    def payload(self):
        """Gets the payload of this ConversationLeaveEventAllOf.  # noqa: E501


        :return: The payload of this ConversationLeaveEventAllOf.  # noqa: E501
        :rtype: ConversationLeaveEventAllOfPayload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ConversationLeaveEventAllOf.


        :param payload: The payload of this ConversationLeaveEventAllOf.  # noqa: E501
        :type: ConversationLeaveEventAllOfPayload
        """

        self._payload = payload

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
        if not isinstance(other, ConversationLeaveEventAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationLeaveEventAllOf):
            return True

        return self.to_dict() != other.to_dict()
