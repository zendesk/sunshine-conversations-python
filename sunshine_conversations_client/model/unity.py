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

try:
    Integration = __import__("sunshine_conversations_client.model."+re.sub(r'(?<!^)(?=[A-Z])', '_', "Integration").lower(), fromlist=("Integration")).Integration
except ImportError:
    pass

class Unity(Integration):
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
        'type': 'str',
        'can_user_create_more_conversations': 'bool',
        'attachments_enabled': 'bool',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations',
        'attachments_enabled': 'attachmentsEnabled',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='unity', can_user_create_more_conversations=None, attachments_enabled=None, default_responder_id=Undefined(), default_responder=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """Unity - a model defined in OpenAPI"""  # noqa: E501
        super().__init__(**kwargs)

        if (super().openapi_types is not None):
            all_types = super().openapi_types.copy()
            all_types.update(self.openapi_types)
            self.openapi_types = all_types

        if (super().attribute_map is not None):
            all_attributes = super().attribute_map.copy()
            all_attributes.update(self.attribute_map)
            self.attribute_map = all_attributes
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._can_user_create_more_conversations = None
        self._attachments_enabled = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations
        if attachments_enabled is not None:
            self.attachments_enabled = attachments_enabled
        self.default_responder_id = default_responder_id
        if default_responder is not None:
            self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Unity.  # noqa: E501

        To configure a Unity integration, create an integration with type 'unity' by calling the Create Integration endpoint.   # noqa: E501

        :return: The type of this Unity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Unity.

        To configure a Unity integration, create an integration with type 'unity' by calling the Create Integration endpoint.   # noqa: E501

        :param type: The type of this Unity.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this Unity.  # noqa: E501

        Allows users to create more than one conversation on the Unity integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this Unity.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this Unity.

        Allows users to create more than one conversation on the Unity integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this Unity.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def attachments_enabled(self):
        """Gets the attachments_enabled of this Unity.  # noqa: E501

        Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.   # noqa: E501

        :return: The attachments_enabled of this Unity.  # noqa: E501
        :rtype: bool
        """
        return self._attachments_enabled

    @attachments_enabled.setter
    def attachments_enabled(self, attachments_enabled):
        """Sets the attachments_enabled of this Unity.

        Allows users to send attachments. By default, the setting is set to true. This setting can only be configured in Zendesk Admin Center.   # noqa: E501

        :param attachments_enabled: The attachments_enabled of this Unity.  # noqa: E501
        :type: bool
        """

        self._attachments_enabled = attachments_enabled

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Unity.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this Unity.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Unity.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Unity.  # noqa: E501
        :type: str
        """
        if type(default_responder_id) is Undefined:
            default_responder_id = None
            self.nulls.discard("default_responder_id")
        elif default_responder_id is None:
            self.nulls.add("default_responder_id")
        else:
            self.nulls.discard("default_responder_id")

        self._default_responder_id = default_responder_id

    @property
    def default_responder(self):
        """Gets the default_responder of this Unity.  # noqa: E501


        :return: The default_responder of this Unity.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Unity.


        :param default_responder: The default_responder of this Unity.  # noqa: E501
        :type: DefaultResponderDefaultResponder
        """

        self._default_responder = default_responder

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
        if not isinstance(other, Unity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Unity):
            return True

        return self.to_dict() != other.to_dict()
