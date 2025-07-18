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


class PassControlBody(object):
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
        'switchboard_integration': 'str',
        'reason': 'str',
        'metadata': 'dict'
    }

    attribute_map = {
        'switchboard_integration': 'switchboardIntegration',
        'reason': 'reason',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, switchboard_integration=None, reason=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """PassControlBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._switchboard_integration = None
        self._reason = None
        self._metadata = None
        self.discriminator = None

        self.switchboard_integration = switchboard_integration
        if reason is not None:
            self.reason = reason
        if metadata is not None:
            self.metadata = metadata

    @property
    def switchboard_integration(self):
        """Gets the switchboard_integration of this PassControlBody.  # noqa: E501

        The id or the name of the switchboard integration that will become active. May also use the `next` keyword to transfer control to the next switchboard integration designated in the switchboard hierarchy configuration  # noqa: E501

        :return: The switchboard_integration of this PassControlBody.  # noqa: E501
        :rtype: str
        """
        return self._switchboard_integration

    @switchboard_integration.setter
    def switchboard_integration(self, switchboard_integration):
        """Sets the switchboard_integration of this PassControlBody.

        The id or the name of the switchboard integration that will become active. May also use the `next` keyword to transfer control to the next switchboard integration designated in the switchboard hierarchy configuration  # noqa: E501

        :param switchboard_integration: The switchboard_integration of this PassControlBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and switchboard_integration is None:  # noqa: E501
            raise ValueError("Invalid value for `switchboard_integration`, must not be `None`")  # noqa: E501

        self._switchboard_integration = switchboard_integration

    @property
    def reason(self):
        """Gets the reason of this PassControlBody.  # noqa: E501

        Reason for the pass control action.  # noqa: E501

        :return: The reason of this PassControlBody.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PassControlBody.

        Reason for the pass control action.  # noqa: E501

        :param reason: The reason of this PassControlBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["ticketClosed", "transferToEmail"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def metadata(self):
        """Gets the metadata of this PassControlBody.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the `switchboard:passControl` webhook.  # noqa: E501

        :return: The metadata of this PassControlBody.  # noqa: E501
        :rtype: dict
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PassControlBody.

        Flat object containing custom properties. Strings, numbers and booleans are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size. The metadata object will be included in the `switchboard:passControl` webhook.  # noqa: E501

        :param metadata: The metadata of this PassControlBody.  # noqa: E501
        :type: dict
        """

        self._metadata = metadata

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
        if not isinstance(other, PassControlBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PassControlBody):
            return True

        return self.to_dict() != other.to_dict()
