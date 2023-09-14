# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 10.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class SwitchboardIntegration(object):
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
        'name': 'str',
        'integration_id': 'str',
        'integration_type': 'str',
        'deliver_standby_events': 'bool',
        'next_switchboard_integration_id': 'str',
        'message_history_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'integration_id': 'integrationId',
        'integration_type': 'integrationType',
        'deliver_standby_events': 'deliverStandbyEvents',
        'next_switchboard_integration_id': 'nextSwitchboardIntegrationId',
        'message_history_count': 'messageHistoryCount'
    }

    nulls = set()

    def __init__(self, id=None, name=None, integration_id=None, integration_type=None, deliver_standby_events=None, next_switchboard_integration_id=None, message_history_count=Undefined(), local_vars_configuration=None):  # noqa: E501
        """SwitchboardIntegration - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._integration_id = None
        self._integration_type = None
        self._deliver_standby_events = None
        self._next_switchboard_integration_id = None
        self._message_history_count = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.integration_id = integration_id
        self.integration_type = integration_type
        self.deliver_standby_events = deliver_standby_events
        if next_switchboard_integration_id is not None:
            self.next_switchboard_integration_id = next_switchboard_integration_id
        self.message_history_count = message_history_count

    @property
    def id(self):
        """Gets the id of this SwitchboardIntegration.  # noqa: E501

        The unique ID of the switchboard integration.  # noqa: E501

        :return: The id of this SwitchboardIntegration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SwitchboardIntegration.

        The unique ID of the switchboard integration.  # noqa: E501

        :param id: The id of this SwitchboardIntegration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SwitchboardIntegration.  # noqa: E501

        Identifier for use in control transfer protocols. Restricted to alphanumeric characters, `-` and `_`.  # noqa: E501

        :return: The name of this SwitchboardIntegration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SwitchboardIntegration.

        Identifier for use in control transfer protocols. Restricted to alphanumeric characters, `-` and `_`.  # noqa: E501

        :param name: The name of this SwitchboardIntegration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self._name = name

    @property
    def integration_id(self):
        """Gets the integration_id of this SwitchboardIntegration.  # noqa: E501

        Id of the integration that should deliver events routed by the switchboard.  # noqa: E501

        :return: The integration_id of this SwitchboardIntegration.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this SwitchboardIntegration.

        Id of the integration that should deliver events routed by the switchboard.  # noqa: E501

        :param integration_id: The integration_id of this SwitchboardIntegration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_id`, must not be `None`")  # noqa: E501

        self._integration_id = integration_id

    @property
    def integration_type(self):
        """Gets the integration_type of this SwitchboardIntegration.  # noqa: E501

        Type of integration that should deliver events routed by the switchboard. If referencing an OAuth integration, the clientId issued by Sunshine Conversations during the OAuth partnership process will be the value of integrationType.  # noqa: E501

        :return: The integration_type of this SwitchboardIntegration.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this SwitchboardIntegration.

        Type of integration that should deliver events routed by the switchboard. If referencing an OAuth integration, the clientId issued by Sunshine Conversations during the OAuth partnership process will be the value of integrationType.  # noqa: E501

        :param integration_type: The integration_type of this SwitchboardIntegration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_type is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_type`, must not be `None`")  # noqa: E501

        self._integration_type = integration_type

    @property
    def deliver_standby_events(self):
        """Gets the deliver_standby_events of this SwitchboardIntegration.  # noqa: E501

        Setting to determine if webhooks should be sent when the switchboard integration is not in control of a conversation (standby status)  # noqa: E501

        :return: The deliver_standby_events of this SwitchboardIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._deliver_standby_events

    @deliver_standby_events.setter
    def deliver_standby_events(self, deliver_standby_events):
        """Sets the deliver_standby_events of this SwitchboardIntegration.

        Setting to determine if webhooks should be sent when the switchboard integration is not in control of a conversation (standby status)  # noqa: E501

        :param deliver_standby_events: The deliver_standby_events of this SwitchboardIntegration.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and deliver_standby_events is None:  # noqa: E501
            raise ValueError("Invalid value for `deliver_standby_events`, must not be `None`")  # noqa: E501

        self._deliver_standby_events = deliver_standby_events

    @property
    def next_switchboard_integration_id(self):
        """Gets the next_switchboard_integration_id of this SwitchboardIntegration.  # noqa: E501

        The switchboard integration id to which control of a conversation is passed / offered by default.  # noqa: E501

        :return: The next_switchboard_integration_id of this SwitchboardIntegration.  # noqa: E501
        :rtype: str
        """
        return self._next_switchboard_integration_id

    @next_switchboard_integration_id.setter
    def next_switchboard_integration_id(self, next_switchboard_integration_id):
        """Sets the next_switchboard_integration_id of this SwitchboardIntegration.

        The switchboard integration id to which control of a conversation is passed / offered by default.  # noqa: E501

        :param next_switchboard_integration_id: The next_switchboard_integration_id of this SwitchboardIntegration.  # noqa: E501
        :type: str
        """

        self._next_switchboard_integration_id = next_switchboard_integration_id

    @property
    def message_history_count(self):
        """Gets the message_history_count of this SwitchboardIntegration.  # noqa: E501

        Number of messages to include in the message history context.  # noqa: E501

        :return: The message_history_count of this SwitchboardIntegration.  # noqa: E501
        :rtype: int
        """
        return self._message_history_count

    @message_history_count.setter
    def message_history_count(self, message_history_count):
        """Sets the message_history_count of this SwitchboardIntegration.

        Number of messages to include in the message history context.  # noqa: E501

        :param message_history_count: The message_history_count of this SwitchboardIntegration.  # noqa: E501
        :type: int
        """
        if type(message_history_count) is Undefined:
            message_history_count = None
            self.nulls.discard("message_history_count")
        elif message_history_count is None:
            self.nulls.add("message_history_count")
        else:
            self.nulls.discard("message_history_count")
        if (self.local_vars_configuration.client_side_validation and
                message_history_count is not None and message_history_count > 10):  # noqa: E501
            raise ValueError("Invalid value for `message_history_count`, must be a value less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message_history_count is not None and message_history_count < 1):  # noqa: E501
            raise ValueError("Invalid value for `message_history_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._message_history_count = message_history_count

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
        if not isinstance(other, SwitchboardIntegration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardIntegration):
            return True

        return self.to_dict() != other.to_dict()
