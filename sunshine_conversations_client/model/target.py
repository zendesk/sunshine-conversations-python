# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.14.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Target(object):
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
        'conversation_id': 'str'
    }

    attribute_map = {
        'conversation_id': 'conversationId'
    }

    nulls = set()

    def __init__(self, conversation_id=None, local_vars_configuration=None):  # noqa: E501
        """Target - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation_id = None
        self.discriminator = None

        self.conversation_id = conversation_id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this Target.  # noqa: E501

        The conversation ID of the target conversation.  # noqa: E501

        :return: The conversation_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this Target.

        The conversation ID of the target conversation.  # noqa: E501

        :param conversation_id: The conversation_id of this Target.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and conversation_id is None:  # noqa: E501
            raise ValueError("Invalid value for `conversation_id`, must not be `None`")  # noqa: E501

        self._conversation_id = conversation_id

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
        if not isinstance(other, Target):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Target):
            return True

        return self.to_dict() != other.to_dict()
