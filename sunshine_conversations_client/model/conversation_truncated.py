# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ConversationTruncated(object):
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
        'type': 'ConversationType',
        'metadata': 'object',
        'active_switchboard_integration': 'SwitchboardIntegrationWebhook',
        'pending_switchboard_integration': 'SwitchboardIntegrationWebhook'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'metadata': 'metadata',
        'active_switchboard_integration': 'activeSwitchboardIntegration',
        'pending_switchboard_integration': 'pendingSwitchboardIntegration'
    }

    nulls = set()

    def __init__(self, id=None, type=None, metadata=Undefined(), active_switchboard_integration=Undefined(), pending_switchboard_integration=Undefined(), local_vars_configuration=None):  # noqa: E501
        """ConversationTruncated - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._metadata = None
        self._active_switchboard_integration = None
        self._pending_switchboard_integration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.metadata = metadata
        self.active_switchboard_integration = active_switchboard_integration
        self.pending_switchboard_integration = pending_switchboard_integration

    @property
    def id(self):
        """Gets the id of this ConversationTruncated.  # noqa: E501

        The unique ID of the conversation.  # noqa: E501

        :return: The id of this ConversationTruncated.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConversationTruncated.

        The unique ID of the conversation.  # noqa: E501

        :param id: The id of this ConversationTruncated.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ConversationTruncated.  # noqa: E501


        :return: The type of this ConversationTruncated.  # noqa: E501
        :rtype: ConversationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationTruncated.


        :param type: The type of this ConversationTruncated.  # noqa: E501
        :type: ConversationType
        """

        self._type = type

    @property
    def metadata(self):
        """Gets the metadata of this ConversationTruncated.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this ConversationTruncated.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ConversationTruncated.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this ConversationTruncated.  # noqa: E501
        :type: object
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

        self._metadata = metadata

    @property
    def active_switchboard_integration(self):
        """Gets the active_switchboard_integration of this ConversationTruncated.  # noqa: E501

        The current switchboard integration that is in control of the conversation. This field is omitted if no `activeSwitchboardIntegration` exists for the conversation.  # noqa: E501

        :return: The active_switchboard_integration of this ConversationTruncated.  # noqa: E501
        :rtype: SwitchboardIntegrationWebhook
        """
        return self._active_switchboard_integration

    @active_switchboard_integration.setter
    def active_switchboard_integration(self, active_switchboard_integration):
        """Sets the active_switchboard_integration of this ConversationTruncated.

        The current switchboard integration that is in control of the conversation. This field is omitted if no `activeSwitchboardIntegration` exists for the conversation.  # noqa: E501

        :param active_switchboard_integration: The active_switchboard_integration of this ConversationTruncated.  # noqa: E501
        :type: SwitchboardIntegrationWebhook
        """
        if type(active_switchboard_integration) is Undefined:
            active_switchboard_integration = None
            self.nulls.discard("active_switchboard_integration")
        elif active_switchboard_integration is None:
            self.nulls.add("active_switchboard_integration")
        else:
            self.nulls.discard("active_switchboard_integration")

        self._active_switchboard_integration = active_switchboard_integration

    @property
    def pending_switchboard_integration(self):
        """Gets the pending_switchboard_integration of this ConversationTruncated.  # noqa: E501

        The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control.  # noqa: E501

        :return: The pending_switchboard_integration of this ConversationTruncated.  # noqa: E501
        :rtype: SwitchboardIntegrationWebhook
        """
        return self._pending_switchboard_integration

    @pending_switchboard_integration.setter
    def pending_switchboard_integration(self, pending_switchboard_integration):
        """Sets the pending_switchboard_integration of this ConversationTruncated.

        The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control.  # noqa: E501

        :param pending_switchboard_integration: The pending_switchboard_integration of this ConversationTruncated.  # noqa: E501
        :type: SwitchboardIntegrationWebhook
        """
        if type(pending_switchboard_integration) is Undefined:
            pending_switchboard_integration = None
            self.nulls.discard("pending_switchboard_integration")
        elif pending_switchboard_integration is None:
            self.nulls.add("pending_switchboard_integration")
        else:
            self.nulls.discard("pending_switchboard_integration")

        self._pending_switchboard_integration = pending_switchboard_integration

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
        if not isinstance(other, ConversationTruncated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationTruncated):
            return True

        return self.to_dict() != other.to_dict()
