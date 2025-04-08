# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class SwitchboardUpdateBody(object):
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
        'enabled': 'bool',
        'default_switchboard_integration_id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'default_switchboard_integration_id': 'defaultSwitchboardIntegrationId'
    }

    nulls = set()

    def __init__(self, enabled=None, default_switchboard_integration_id=None, local_vars_configuration=None):  # noqa: E501
        """SwitchboardUpdateBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._default_switchboard_integration_id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if default_switchboard_integration_id is not None:
            self.default_switchboard_integration_id = default_switchboard_integration_id

    @property
    def enabled(self):
        """Gets the enabled of this SwitchboardUpdateBody.  # noqa: E501

        Whether the switchboard is enabled. Allows creating the switchboard in a disabled state so that messages don't get lost or misrouted during switchboard configuration. When a switchboard is disabled, integrations linked to the switchboard will receive all events.  # noqa: E501

        :return: The enabled of this SwitchboardUpdateBody.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SwitchboardUpdateBody.

        Whether the switchboard is enabled. Allows creating the switchboard in a disabled state so that messages don't get lost or misrouted during switchboard configuration. When a switchboard is disabled, integrations linked to the switchboard will receive all events.  # noqa: E501

        :param enabled: The enabled of this SwitchboardUpdateBody.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def default_switchboard_integration_id(self):
        """Gets the default_switchboard_integration_id of this SwitchboardUpdateBody.  # noqa: E501

        The id of the switchboard integration that will be given control when a new conversation begins. It will also be used for conversations that existed before the switchboard was enabled.  # noqa: E501

        :return: The default_switchboard_integration_id of this SwitchboardUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._default_switchboard_integration_id

    @default_switchboard_integration_id.setter
    def default_switchboard_integration_id(self, default_switchboard_integration_id):
        """Sets the default_switchboard_integration_id of this SwitchboardUpdateBody.

        The id of the switchboard integration that will be given control when a new conversation begins. It will also be used for conversations that existed before the switchboard was enabled.  # noqa: E501

        :param default_switchboard_integration_id: The default_switchboard_integration_id of this SwitchboardUpdateBody.  # noqa: E501
        :type: str
        """

        self._default_switchboard_integration_id = default_switchboard_integration_id

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
        if not isinstance(other, SwitchboardUpdateBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardUpdateBody):
            return True

        return self.to_dict() != other.to_dict()
