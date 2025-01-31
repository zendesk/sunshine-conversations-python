# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.3.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class SwitchboardIntegrationListResponse(object):
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
        'switchboard_integrations': 'list[SwitchboardIntegration]'
    }

    attribute_map = {
        'switchboard_integrations': 'switchboardIntegrations'
    }

    nulls = set()

    def __init__(self, switchboard_integrations=None, local_vars_configuration=None):  # noqa: E501
        """SwitchboardIntegrationListResponse - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._switchboard_integrations = None
        self.discriminator = None

        if switchboard_integrations is not None:
            self.switchboard_integrations = switchboard_integrations

    @property
    def switchboard_integrations(self):
        """Gets the switchboard_integrations of this SwitchboardIntegrationListResponse.  # noqa: E501

        List of returned switchboard integrations.  # noqa: E501

        :return: The switchboard_integrations of this SwitchboardIntegrationListResponse.  # noqa: E501
        :rtype: list[SwitchboardIntegration]
        """
        return self._switchboard_integrations

    @switchboard_integrations.setter
    def switchboard_integrations(self, switchboard_integrations):
        """Sets the switchboard_integrations of this SwitchboardIntegrationListResponse.

        List of returned switchboard integrations.  # noqa: E501

        :param switchboard_integrations: The switchboard_integrations of this SwitchboardIntegrationListResponse.  # noqa: E501
        :type: list[SwitchboardIntegration]
        """

        self._switchboard_integrations = switchboard_integrations

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
        if not isinstance(other, SwitchboardIntegrationListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardIntegrationListResponse):
            return True

        return self.to_dict() != other.to_dict()
