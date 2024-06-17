# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class SwitchboardIntegrationCreateBody(object):
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
        'name': 'str',
        'integration_id': 'str',
        'integration_type': 'str',
        'deliver_standby_events': 'bool',
        'next_switchboard_integration_id': 'str',
        'message_history_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'integration_id': 'integrationId',
        'integration_type': 'integrationType',
        'deliver_standby_events': 'deliverStandbyEvents',
        'next_switchboard_integration_id': 'nextSwitchboardIntegrationId',
        'message_history_count': 'messageHistoryCount'
    }

    nulls = set()

    def __init__(self, name=None, integration_id=None, integration_type=None, deliver_standby_events=None, next_switchboard_integration_id=Undefined(), message_history_count=Undefined(), local_vars_configuration=None):  # noqa: E501
        """SwitchboardIntegrationCreateBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._integration_id = None
        self._integration_type = None
        self._deliver_standby_events = None
        self._next_switchboard_integration_id = None
        self._message_history_count = None
        self.discriminator = None

        self.name = name
        if integration_id is not None:
            self.integration_id = integration_id
        if integration_type is not None:
            self.integration_type = integration_type
        if deliver_standby_events is not None:
            self.deliver_standby_events = deliver_standby_events
        self.next_switchboard_integration_id = next_switchboard_integration_id
        self.message_history_count = message_history_count

    @property
    def name(self):
        """Gets the name of this SwitchboardIntegrationCreateBody.  # noqa: E501

        Identifier for use in control transfer protocols. Restricted to alphanumeric characters, `-` and `_`.  # noqa: E501

        :return: The name of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SwitchboardIntegrationCreateBody.

        Identifier for use in control transfer protocols. Restricted to alphanumeric characters, `-` and `_`.  # noqa: E501

        :param name: The name of this SwitchboardIntegrationCreateBody.  # noqa: E501
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
        """Gets the integration_id of this SwitchboardIntegrationCreateBody.  # noqa: E501

        The id of the integration to link to the switchboard integration. Must be used when linking a custom integration. One of `integrationId` or `integrationType` must be provided.  # noqa: E501

        :return: The integration_id of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this SwitchboardIntegrationCreateBody.

        The id of the integration to link to the switchboard integration. Must be used when linking a custom integration. One of `integrationId` or `integrationType` must be provided.  # noqa: E501

        :param integration_id: The integration_id of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def integration_type(self):
        """Gets the integration_type of this SwitchboardIntegrationCreateBody.  # noqa: E501

        The type of the integration to link to the switchboard integration. Must be used when linking an OAuth integration. One of `integrationId` or `integrationType` must be provided.  # noqa: E501

        :return: The integration_type of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this SwitchboardIntegrationCreateBody.

        The type of the integration to link to the switchboard integration. Must be used when linking an OAuth integration. One of `integrationId` or `integrationType` must be provided.  # noqa: E501

        :param integration_type: The integration_type of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

    @property
    def deliver_standby_events(self):
        """Gets the deliver_standby_events of this SwitchboardIntegrationCreateBody.  # noqa: E501


        :return: The deliver_standby_events of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :rtype: bool
        """
        return self._deliver_standby_events

    @deliver_standby_events.setter
    def deliver_standby_events(self, deliver_standby_events):
        """Sets the deliver_standby_events of this SwitchboardIntegrationCreateBody.


        :param deliver_standby_events: The deliver_standby_events of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :type: bool
        """

        self._deliver_standby_events = deliver_standby_events

    @property
    def next_switchboard_integration_id(self):
        """Gets the next_switchboard_integration_id of this SwitchboardIntegrationCreateBody.  # noqa: E501


        :return: The next_switchboard_integration_id of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._next_switchboard_integration_id

    @next_switchboard_integration_id.setter
    def next_switchboard_integration_id(self, next_switchboard_integration_id):
        """Sets the next_switchboard_integration_id of this SwitchboardIntegrationCreateBody.


        :param next_switchboard_integration_id: The next_switchboard_integration_id of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :type: str
        """
        if type(next_switchboard_integration_id) is Undefined:
            next_switchboard_integration_id = None
            self.nulls.discard("next_switchboard_integration_id")
        elif next_switchboard_integration_id is None:
            self.nulls.add("next_switchboard_integration_id")
        else:
            self.nulls.discard("next_switchboard_integration_id")

        self._next_switchboard_integration_id = next_switchboard_integration_id

    @property
    def message_history_count(self):
        """Gets the message_history_count of this SwitchboardIntegrationCreateBody.  # noqa: E501

        Number of messages to include in the message history context.  # noqa: E501

        :return: The message_history_count of this SwitchboardIntegrationCreateBody.  # noqa: E501
        :rtype: int
        """
        return self._message_history_count

    @message_history_count.setter
    def message_history_count(self, message_history_count):
        """Sets the message_history_count of this SwitchboardIntegrationCreateBody.

        Number of messages to include in the message history context.  # noqa: E501

        :param message_history_count: The message_history_count of this SwitchboardIntegrationCreateBody.  # noqa: E501
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
        if not isinstance(other, SwitchboardIntegrationCreateBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardIntegrationCreateBody):
            return True

        return self.to_dict() != other.to_dict()
