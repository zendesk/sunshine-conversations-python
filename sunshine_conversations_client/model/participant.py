# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Participant(object):
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
        'user_id': 'str',
        'unread_count': 'int',
        'client_associations': 'list[ClientAssociation]',
        'user_external_id': 'str',
        'last_read': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'unread_count': 'unreadCount',
        'client_associations': 'clientAssociations',
        'user_external_id': 'userExternalId',
        'last_read': 'lastRead'
    }

    nulls = set()

    def __init__(self, id=None, user_id=None, unread_count=None, client_associations=None, user_external_id=Undefined(), last_read=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Participant - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._unread_count = None
        self._client_associations = None
        self._user_external_id = None
        self._last_read = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if unread_count is not None:
            self.unread_count = unread_count
        if client_associations is not None:
            self.client_associations = client_associations
        self.user_external_id = user_external_id
        self.last_read = last_read

    @property
    def id(self):
        """Gets the id of this Participant.  # noqa: E501

        The unique ID of the participant.  # noqa: E501

        :return: The id of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Participant.

        The unique ID of the participant.  # noqa: E501

        :param id: The id of this Participant.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this Participant.  # noqa: E501

        The id of the associated user.  # noqa: E501

        :return: The user_id of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Participant.

        The id of the associated user.  # noqa: E501

        :param user_id: The user_id of this Participant.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def unread_count(self):
        """Gets the unread_count of this Participant.  # noqa: E501

        Number of messages the user has not yet read.  # noqa: E501

        :return: The unread_count of this Participant.  # noqa: E501
        :rtype: int
        """
        return self._unread_count

    @unread_count.setter
    def unread_count(self, unread_count):
        """Sets the unread_count of this Participant.

        Number of messages the user has not yet read.  # noqa: E501

        :param unread_count: The unread_count of this Participant.  # noqa: E501
        :type: int
        """

        self._unread_count = unread_count

    @property
    def client_associations(self):
        """Gets the client_associations of this Participant.  # noqa: E501

        Represents the clients that are active in the conversation for a particular user. A participant can have multiple clientAssociations in the case of channel transfer, business initiated conversations, or identified users. The order of the array indicates how recently a client has interacted with the conversation, with the most recent client first. The first item in the array is considered to be the user's primary client for that conversation, and will be selected first for message delivery.   # noqa: E501

        :return: The client_associations of this Participant.  # noqa: E501
        :rtype: list[ClientAssociation]
        """
        return self._client_associations

    @client_associations.setter
    def client_associations(self, client_associations):
        """Sets the client_associations of this Participant.

        Represents the clients that are active in the conversation for a particular user. A participant can have multiple clientAssociations in the case of channel transfer, business initiated conversations, or identified users. The order of the array indicates how recently a client has interacted with the conversation, with the most recent client first. The first item in the array is considered to be the user's primary client for that conversation, and will be selected first for message delivery.   # noqa: E501

        :param client_associations: The client_associations of this Participant.  # noqa: E501
        :type: list[ClientAssociation]
        """

        self._client_associations = client_associations

    @property
    def user_external_id(self):
        """Gets the user_external_id of this Participant.  # noqa: E501

        The externalId of the associated user.  # noqa: E501

        :return: The user_external_id of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._user_external_id

    @user_external_id.setter
    def user_external_id(self, user_external_id):
        """Sets the user_external_id of this Participant.

        The externalId of the associated user.  # noqa: E501

        :param user_external_id: The user_external_id of this Participant.  # noqa: E501
        :type: str
        """
        if type(user_external_id) is Undefined:
            user_external_id = None
            self.nulls.discard("user_external_id")
        elif user_external_id is None:
            self.nulls.add("user_external_id")
        else:
            self.nulls.discard("user_external_id")

        self._user_external_id = user_external_id

    @property
    def last_read(self):
        """Gets the last_read of this Participant.  # noqa: E501

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the latest message the user has read.  # noqa: E501

        :return: The last_read of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._last_read

    @last_read.setter
    def last_read(self, last_read):
        """Sets the last_read of this Participant.

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the latest message the user has read.  # noqa: E501

        :param last_read: The last_read of this Participant.  # noqa: E501
        :type: str
        """
        if type(last_read) is Undefined:
            last_read = None
            self.nulls.discard("last_read")
        elif last_read is None:
            self.nulls.add("last_read")
        else:
            self.nulls.discard("last_read")

        self._last_read = last_read

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
        if not isinstance(other, Participant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Participant):
            return True

        return self.to_dict() != other.to_dict()
