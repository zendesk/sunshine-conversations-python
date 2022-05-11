# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ClientUpdateEventAllOfPayload(object):
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
        'conversation': 'ConversationTruncated',
        'user': 'UserTruncated',
        'client': 'Client',
        'reason': 'str'
    }

    attribute_map = {
        'conversation': 'conversation',
        'user': 'user',
        'client': 'client',
        'reason': 'reason'
    }

    nulls = set()

    def __init__(self, conversation=None, user=None, client=None, reason=None, local_vars_configuration=None):  # noqa: E501
        """ClientUpdateEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation = None
        self._user = None
        self._client = None
        self._reason = None
        self.discriminator = None

        if conversation is not None:
            self.conversation = conversation
        if user is not None:
            self.user = user
        if client is not None:
            self.client = client
        if reason is not None:
            self.reason = reason

    @property
    def conversation(self):
        """Gets the conversation of this ClientUpdateEventAllOfPayload.  # noqa: E501

        The conversation which triggered a change in the client.  # noqa: E501

        :return: The conversation of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ClientUpdateEventAllOfPayload.

        The conversation which triggered a change in the client.  # noqa: E501

        :param conversation: The conversation of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def user(self):
        """Gets the user of this ClientUpdateEventAllOfPayload.  # noqa: E501

        The user associated with the client.  # noqa: E501

        :return: The user of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :rtype: UserTruncated
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ClientUpdateEventAllOfPayload.

        The user associated with the client.  # noqa: E501

        :param user: The user of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :type: UserTruncated
        """

        self._user = user

    @property
    def client(self):
        """Gets the client of this ClientUpdateEventAllOfPayload.  # noqa: E501

        The updated client.  # noqa: E501

        :return: The client of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :rtype: Client
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this ClientUpdateEventAllOfPayload.

        The updated client.  # noqa: E501

        :param client: The client of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :type: Client
        """

        self._client = client

    @property
    def reason(self):
        """Gets the reason of this ClientUpdateEventAllOfPayload.  # noqa: E501

        The reason for which the client was updated. * `confirmed` - The client is now active and ready to use. * `blocked` - The user has unsubscribed from the conversation. * `matched` - The channel found a user that matches the information provided.   # noqa: E501

        :return: The reason of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ClientUpdateEventAllOfPayload.

        The reason for which the client was updated. * `confirmed` - The client is now active and ready to use. * `blocked` - The user has unsubscribed from the conversation. * `matched` - The channel found a user that matches the information provided.   # noqa: E501

        :param reason: The reason of this ClientUpdateEventAllOfPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["confirmed", "blocked", "matched"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

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
        if not isinstance(other, ClientUpdateEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientUpdateEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
