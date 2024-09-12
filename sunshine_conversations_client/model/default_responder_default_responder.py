# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.8.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class DefaultResponderDefaultResponder(object):
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
        'switchboard_id': 'str',
        'app_id': 'str',
        'integration_id': 'str',
        'integration_type': 'str',
        'name': 'str',
        'deliver_standby_events': 'bool',
        'next_switchboard_integration_id': 'str',
        'message_history_count': 'float',
        'inherited': 'bool'
    }

    attribute_map = {
        'switchboard_id': 'switchboardId',
        'app_id': 'appId',
        'integration_id': 'integrationId',
        'integration_type': 'integrationType',
        'name': 'name',
        'deliver_standby_events': 'deliverStandbyEvents',
        'next_switchboard_integration_id': 'nextSwitchboardIntegrationId',
        'message_history_count': 'messageHistoryCount',
        'inherited': 'inherited'
    }

    nulls = set()

    def __init__(self, switchboard_id=None, app_id=None, integration_id=None, integration_type=None, name=None, deliver_standby_events=None, next_switchboard_integration_id=None, message_history_count=None, inherited=None, local_vars_configuration=None):  # noqa: E501
        """DefaultResponderDefaultResponder - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._switchboard_id = None
        self._app_id = None
        self._integration_id = None
        self._integration_type = None
        self._name = None
        self._deliver_standby_events = None
        self._next_switchboard_integration_id = None
        self._message_history_count = None
        self._inherited = None
        self.discriminator = None

        if switchboard_id is not None:
            self.switchboard_id = switchboard_id
        if app_id is not None:
            self.app_id = app_id
        if integration_id is not None:
            self.integration_id = integration_id
        if integration_type is not None:
            self.integration_type = integration_type
        if name is not None:
            self.name = name
        if deliver_standby_events is not None:
            self.deliver_standby_events = deliver_standby_events
        if next_switchboard_integration_id is not None:
            self.next_switchboard_integration_id = next_switchboard_integration_id
        if message_history_count is not None:
            self.message_history_count = message_history_count
        if inherited is not None:
            self.inherited = inherited

    @property
    def switchboard_id(self):
        """Gets the switchboard_id of this DefaultResponderDefaultResponder.  # noqa: E501

        The unique ID of the switchboard.  # noqa: E501

        :return: The switchboard_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: str
        """
        return self._switchboard_id

    @switchboard_id.setter
    def switchboard_id(self, switchboard_id):
        """Sets the switchboard_id of this DefaultResponderDefaultResponder.

        The unique ID of the switchboard.  # noqa: E501

        :param switchboard_id: The switchboard_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: str
        """

        self._switchboard_id = switchboard_id

    @property
    def app_id(self):
        """Gets the app_id of this DefaultResponderDefaultResponder.  # noqa: E501

        Identifies the app.  # noqa: E501

        :return: The app_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this DefaultResponderDefaultResponder.

        Identifies the app.  # noqa: E501

        :param app_id: The app_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def integration_id(self):
        """Gets the integration_id of this DefaultResponderDefaultResponder.  # noqa: E501

        The unique ID of the integration.  # noqa: E501

        :return: The integration_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this DefaultResponderDefaultResponder.

        The unique ID of the integration.  # noqa: E501

        :param integration_id: The integration_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def integration_type(self):
        """Gets the integration_type of this DefaultResponderDefaultResponder.  # noqa: E501

        The type of the integration.  # noqa: E501

        :return: The integration_type of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this DefaultResponderDefaultResponder.

        The type of the integration.  # noqa: E501

        :param integration_type: The integration_type of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

    @property
    def name(self):
        """Gets the name of this DefaultResponderDefaultResponder.  # noqa: E501

        The name of the switchboard.  # noqa: E501

        :return: The name of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DefaultResponderDefaultResponder.

        The name of the switchboard.  # noqa: E501

        :param name: The name of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deliver_standby_events(self):
        """Gets the deliver_standby_events of this DefaultResponderDefaultResponder.  # noqa: E501

        Indicates whether the switchboard should deliver standby events.  # noqa: E501

        :return: The deliver_standby_events of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: bool
        """
        return self._deliver_standby_events

    @deliver_standby_events.setter
    def deliver_standby_events(self, deliver_standby_events):
        """Sets the deliver_standby_events of this DefaultResponderDefaultResponder.

        Indicates whether the switchboard should deliver standby events.  # noqa: E501

        :param deliver_standby_events: The deliver_standby_events of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: bool
        """

        self._deliver_standby_events = deliver_standby_events

    @property
    def next_switchboard_integration_id(self):
        """Gets the next_switchboard_integration_id of this DefaultResponderDefaultResponder.  # noqa: E501

        The unique ID of the next switchboard integration.  # noqa: E501

        :return: The next_switchboard_integration_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: str
        """
        return self._next_switchboard_integration_id

    @next_switchboard_integration_id.setter
    def next_switchboard_integration_id(self, next_switchboard_integration_id):
        """Sets the next_switchboard_integration_id of this DefaultResponderDefaultResponder.

        The unique ID of the next switchboard integration.  # noqa: E501

        :param next_switchboard_integration_id: The next_switchboard_integration_id of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: str
        """

        self._next_switchboard_integration_id = next_switchboard_integration_id

    @property
    def message_history_count(self):
        """Gets the message_history_count of this DefaultResponderDefaultResponder.  # noqa: E501

        The number of messages to keep in the message history.  # noqa: E501

        :return: The message_history_count of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: float
        """
        return self._message_history_count

    @message_history_count.setter
    def message_history_count(self, message_history_count):
        """Sets the message_history_count of this DefaultResponderDefaultResponder.

        The number of messages to keep in the message history.  # noqa: E501

        :param message_history_count: The message_history_count of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: float
        """

        self._message_history_count = message_history_count

    @property
    def inherited(self):
        """Gets the inherited of this DefaultResponderDefaultResponder.  # noqa: E501

        Indicates whether the switchboard is inherited.  # noqa: E501

        :return: The inherited of this DefaultResponderDefaultResponder.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this DefaultResponderDefaultResponder.

        Indicates whether the switchboard is inherited.  # noqa: E501

        :param inherited: The inherited of this DefaultResponderDefaultResponder.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

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
        if not isinstance(other, DefaultResponderDefaultResponder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefaultResponderDefaultResponder):
            return True

        return self.to_dict() != other.to_dict()
