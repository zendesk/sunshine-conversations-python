# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class UserMergeEventAllOfPayload(object):
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
        'merged_users': 'UserMergeEventAllOfPayloadMergedUsers',
        'merged_conversations': 'UserMergeEventAllOfPayloadMergedConversations',
        'merged_clients': 'UserMergeEventAllOfPayloadMergedClients',
        'discarded_metadata': 'dict',
        'reason': 'str'
    }

    attribute_map = {
        'merged_users': 'mergedUsers',
        'merged_conversations': 'mergedConversations',
        'merged_clients': 'mergedClients',
        'discarded_metadata': 'discardedMetadata',
        'reason': 'reason'
    }

    nulls = set()

    def __init__(self, merged_users=None, merged_conversations=Undefined(), merged_clients=Undefined(), discarded_metadata=Undefined(), reason=None, local_vars_configuration=None):  # noqa: E501
        """UserMergeEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._merged_users = None
        self._merged_conversations = None
        self._merged_clients = None
        self._discarded_metadata = None
        self._reason = None
        self.discriminator = None

        if merged_users is not None:
            self.merged_users = merged_users
        self.merged_conversations = merged_conversations
        self.merged_clients = merged_clients
        self.discarded_metadata = discarded_metadata
        if reason is not None:
            self.reason = reason

    @property
    def merged_users(self):
        """Gets the merged_users of this UserMergeEventAllOfPayload.  # noqa: E501


        :return: The merged_users of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: UserMergeEventAllOfPayloadMergedUsers
        """
        return self._merged_users

    @merged_users.setter
    def merged_users(self, merged_users):
        """Sets the merged_users of this UserMergeEventAllOfPayload.


        :param merged_users: The merged_users of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: UserMergeEventAllOfPayloadMergedUsers
        """

        self._merged_users = merged_users

    @property
    def merged_conversations(self):
        """Gets the merged_conversations of this UserMergeEventAllOfPayload.  # noqa: E501


        :return: The merged_conversations of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: UserMergeEventAllOfPayloadMergedConversations
        """
        return self._merged_conversations

    @merged_conversations.setter
    def merged_conversations(self, merged_conversations):
        """Sets the merged_conversations of this UserMergeEventAllOfPayload.


        :param merged_conversations: The merged_conversations of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: UserMergeEventAllOfPayloadMergedConversations
        """
        if type(merged_conversations) is Undefined:
            merged_conversations = None
            self.nulls.discard("merged_conversations")
        elif merged_conversations is None:
            self.nulls.add("merged_conversations")
        else:
            self.nulls.discard("merged_conversations")

        self._merged_conversations = merged_conversations

    @property
    def merged_clients(self):
        """Gets the merged_clients of this UserMergeEventAllOfPayload.  # noqa: E501


        :return: The merged_clients of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: UserMergeEventAllOfPayloadMergedClients
        """
        return self._merged_clients

    @merged_clients.setter
    def merged_clients(self, merged_clients):
        """Sets the merged_clients of this UserMergeEventAllOfPayload.


        :param merged_clients: The merged_clients of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: UserMergeEventAllOfPayloadMergedClients
        """
        if type(merged_clients) is Undefined:
            merged_clients = None
            self.nulls.discard("merged_clients")
        elif merged_clients is None:
            self.nulls.add("merged_clients")
        else:
            self.nulls.discard("merged_clients")

        self._merged_clients = merged_clients

    @property
    def discarded_metadata(self):
        """Gets the discarded_metadata of this UserMergeEventAllOfPayload.  # noqa: E501

        A flat object with the set of metadata properties that were discarded when merging the two users. This should contain values only if the combined metadata fields exceed the 4KB limit.  # noqa: E501

        :return: The discarded_metadata of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: dict
        """
        return self._discarded_metadata

    @discarded_metadata.setter
    def discarded_metadata(self, discarded_metadata):
        """Sets the discarded_metadata of this UserMergeEventAllOfPayload.

        A flat object with the set of metadata properties that were discarded when merging the two users. This should contain values only if the combined metadata fields exceed the 4KB limit.  # noqa: E501

        :param discarded_metadata: The discarded_metadata of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: dict
        """
        if type(discarded_metadata) is Undefined:
            discarded_metadata = None
            self.nulls.discard("discarded_metadata")
        elif discarded_metadata is None:
            self.nulls.add("discarded_metadata")
        else:
            self.nulls.discard("discarded_metadata")

        self._discarded_metadata = discarded_metadata

    @property
    def reason(self):
        """Gets the reason of this UserMergeEventAllOfPayload.  # noqa: E501

        The reason for which the users merged. * `api` - The users were merged using the API. * `channelLinking` - The users were merged as a result of initiating a channel link. * `sdkLogin` - The users were merged as a result of logging into an SDK device.   # noqa: E501

        :return: The reason of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UserMergeEventAllOfPayload.

        The reason for which the users merged. * `api` - The users were merged using the API. * `channelLinking` - The users were merged as a result of initiating a channel link. * `sdkLogin` - The users were merged as a result of logging into an SDK device.   # noqa: E501

        :param reason: The reason of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["api", "channelLinking", "sdkLogin"]  # noqa: E501
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
        if not isinstance(other, UserMergeEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMergeEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
