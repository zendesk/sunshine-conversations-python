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


class Client(object):
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
        'type': 'ClientType',
        'status': 'str',
        'integration_id': 'str',
        'external_id': 'str',
        'last_seen': 'str',
        'linked_at': 'str',
        'display_name': 'str',
        'avatar_url': 'str',
        'info': 'object',
        'raw': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'integration_id': 'integrationId',
        'external_id': 'externalId',
        'last_seen': 'lastSeen',
        'linked_at': 'linkedAt',
        'display_name': 'displayName',
        'avatar_url': 'avatarUrl',
        'info': 'info',
        'raw': 'raw'
    }

    nulls = set()

    def __init__(self, id=None, type=None, status=None, integration_id=Undefined(), external_id=Undefined(), last_seen=Undefined(), linked_at=Undefined(), display_name=Undefined(), avatar_url=Undefined(), info=Undefined(), raw=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Client - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._status = None
        self._integration_id = None
        self._external_id = None
        self._last_seen = None
        self._linked_at = None
        self._display_name = None
        self._avatar_url = None
        self._info = None
        self._raw = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        self.integration_id = integration_id
        self.external_id = external_id
        self.last_seen = last_seen
        self.linked_at = linked_at
        self.display_name = display_name
        self.avatar_url = avatar_url
        self.info = info
        self.raw = raw

    @property
    def id(self):
        """Gets the id of this Client.  # noqa: E501

        The unique ID of the client.  # noqa: E501

        :return: The id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Client.

        The unique ID of the client.  # noqa: E501

        :param id: The id of this Client.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Client.  # noqa: E501


        :return: The type of this Client.  # noqa: E501
        :rtype: ClientType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Client.


        :param type: The type of this Client.  # noqa: E501
        :type: ClientType
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this Client.  # noqa: E501

        The client status. Indicates if the client is able to receive messages or not. Can be pending, inactive, active, or blocked.  # noqa: E501

        :return: The status of this Client.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Client.

        The client status. Indicates if the client is able to receive messages or not. Can be pending, inactive, active, or blocked.  # noqa: E501

        :param status: The status of this Client.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "blocked", "inactive", "pending"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def integration_id(self):
        """Gets the integration_id of this Client.  # noqa: E501

        The ID of the integration that the client was created for. Unused for clients of type sdk, as they incorporate multiple integrations.  # noqa: E501

        :return: The integration_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this Client.

        The ID of the integration that the client was created for. Unused for clients of type sdk, as they incorporate multiple integrations.  # noqa: E501

        :param integration_id: The integration_id of this Client.  # noqa: E501
        :type: str
        """
        if type(integration_id) is Undefined:
            integration_id = None
            self.nulls.discard("integration_id")
        elif integration_id is None:
            self.nulls.add("integration_id")
        else:
            self.nulls.discard("integration_id")

        self._integration_id = integration_id

    @property
    def external_id(self):
        """Gets the external_id of this Client.  # noqa: E501

        The ID of the user on an external channel. For example, the user’s phone number for Twilio, or their page-scoped user ID for Facebook Messenger. Applies only to non-SDK clients.  # noqa: E501

        :return: The external_id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Client.

        The ID of the user on an external channel. For example, the user’s phone number for Twilio, or their page-scoped user ID for Facebook Messenger. Applies only to non-SDK clients.  # noqa: E501

        :param external_id: The external_id of this Client.  # noqa: E501
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

    @property
    def last_seen(self):
        """Gets the last_seen of this Client.  # noqa: E501

        A datetime string with the format `YYYY-MM-DDThh:mm:ss.SSSZ` representing the last time the user interacted with this client.  # noqa: E501

        :return: The last_seen of this Client.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Client.

        A datetime string with the format `YYYY-MM-DDThh:mm:ss.SSSZ` representing the last time the user interacted with this client.  # noqa: E501

        :param last_seen: The last_seen of this Client.  # noqa: E501
        :type: str
        """
        if type(last_seen) is Undefined:
            last_seen = None
            self.nulls.discard("last_seen")
        elif last_seen is None:
            self.nulls.add("last_seen")
        else:
            self.nulls.discard("last_seen")

        self._last_seen = last_seen

    @property
    def linked_at(self):
        """Gets the linked_at of this Client.  # noqa: E501

        A timestamp signifying when the client was added to the user. Formatted as `YYYY-MM-DDThh:mm:ss.SSSZ`.  # noqa: E501

        :return: The linked_at of this Client.  # noqa: E501
        :rtype: str
        """
        return self._linked_at

    @linked_at.setter
    def linked_at(self, linked_at):
        """Sets the linked_at of this Client.

        A timestamp signifying when the client was added to the user. Formatted as `YYYY-MM-DDThh:mm:ss.SSSZ`.  # noqa: E501

        :param linked_at: The linked_at of this Client.  # noqa: E501
        :type: str
        """
        if type(linked_at) is Undefined:
            linked_at = None
            self.nulls.discard("linked_at")
        elif linked_at is None:
            self.nulls.add("linked_at")
        else:
            self.nulls.discard("linked_at")

        self._linked_at = linked_at

    @property
    def display_name(self):
        """Gets the display_name of this Client.  # noqa: E501

        The user's display name on the channel.  # noqa: E501

        :return: The display_name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Client.

        The user's display name on the channel.  # noqa: E501

        :param display_name: The display_name of this Client.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")

        self._display_name = display_name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Client.  # noqa: E501

        The URL for the user's avatar on the channel.  # noqa: E501

        :return: The avatar_url of this Client.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Client.

        The URL for the user's avatar on the channel.  # noqa: E501

        :param avatar_url: The avatar_url of this Client.  # noqa: E501
        :type: str
        """
        if type(avatar_url) is Undefined:
            avatar_url = None
            self.nulls.discard("avatar_url")
        elif avatar_url is None:
            self.nulls.add("avatar_url")
        else:
            self.nulls.discard("avatar_url")

        self._avatar_url = avatar_url

    @property
    def info(self):
        """Gets the info of this Client.  # noqa: E501

        A flat curated object with properties that vary for each client platform. All keys are optional and not guaranteed to be available.  # noqa: E501

        :return: The info of this Client.  # noqa: E501
        :rtype: object
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Client.

        A flat curated object with properties that vary for each client platform. All keys are optional and not guaranteed to be available.  # noqa: E501

        :param info: The info of this Client.  # noqa: E501
        :type: object
        """
        if type(info) is Undefined:
            info = None
            self.nulls.discard("info")
        elif info is None:
            self.nulls.add("info")
        else:
            self.nulls.discard("info")

        self._info = info

    @property
    def raw(self):
        """Gets the raw of this Client.  # noqa: E501

        An object with raw properties that vary for each client platform. All keys are optional and not guaranteed to be available.  # noqa: E501

        :return: The raw of this Client.  # noqa: E501
        :rtype: object
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this Client.

        An object with raw properties that vary for each client platform. All keys are optional and not guaranteed to be available.  # noqa: E501

        :param raw: The raw of this Client.  # noqa: E501
        :type: object
        """
        if type(raw) is Undefined:
            raw = None
            self.nulls.discard("raw")
        elif raw is None:
            self.nulls.add("raw")
        else:
            self.nulls.discard("raw")

        self._raw = raw

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
        if not isinstance(other, Client):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Client):
            return True

        return self.to_dict() != other.to_dict()
