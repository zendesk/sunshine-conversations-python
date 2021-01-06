# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Conversation(object):
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
        'active_switchboard_integration': 'SwitchboardIntegrationWebhook',
        'pending_switchboard_integration': 'SwitchboardIntegrationWebhook',
        'is_default': 'bool',
        'display_name': 'str',
        'description': 'str',
        'icon_url': 'str',
        'metadata': 'object',
        'business_last_read': 'str',
        'last_updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'active_switchboard_integration': 'activeSwitchboardIntegration',
        'pending_switchboard_integration': 'pendingSwitchboardIntegration',
        'is_default': 'isDefault',
        'display_name': 'displayName',
        'description': 'description',
        'icon_url': 'iconUrl',
        'metadata': 'metadata',
        'business_last_read': 'businessLastRead',
        'last_updated_at': 'lastUpdatedAt'
    }

    nulls = set()

    def __init__(self, id=None, type=None, active_switchboard_integration=Undefined(), pending_switchboard_integration=Undefined(), is_default=None, display_name=None, description=Undefined(), icon_url=Undefined(), metadata=Undefined(), business_last_read=Undefined(), last_updated_at=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Conversation - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._active_switchboard_integration = None
        self._pending_switchboard_integration = None
        self._is_default = None
        self._display_name = None
        self._description = None
        self._icon_url = None
        self._metadata = None
        self._business_last_read = None
        self._last_updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.active_switchboard_integration = active_switchboard_integration
        self.pending_switchboard_integration = pending_switchboard_integration
        if is_default is not None:
            self.is_default = is_default
        if display_name is not None:
            self.display_name = display_name
        self.description = description
        self.icon_url = icon_url
        self.metadata = metadata
        self.business_last_read = business_last_read
        self.last_updated_at = last_updated_at

    @property
    def id(self):
        """Gets the id of this Conversation.  # noqa: E501

        The unique ID of the conversation.  # noqa: E501

        :return: The id of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Conversation.

        The unique ID of the conversation.  # noqa: E501

        :param id: The id of this Conversation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Conversation.  # noqa: E501


        :return: The type of this Conversation.  # noqa: E501
        :rtype: ConversationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Conversation.


        :param type: The type of this Conversation.  # noqa: E501
        :type: ConversationType
        """

        self._type = type

    @property
    def active_switchboard_integration(self):
        """Gets the active_switchboard_integration of this Conversation.  # noqa: E501

        The current switchboard integration that is in control of the conversation. This field is omitted if no `activeSwitchboardIntegration` exists for the conversation.  # noqa: E501

        :return: The active_switchboard_integration of this Conversation.  # noqa: E501
        :rtype: SwitchboardIntegrationWebhook
        """
        return self._active_switchboard_integration

    @active_switchboard_integration.setter
    def active_switchboard_integration(self, active_switchboard_integration):
        """Sets the active_switchboard_integration of this Conversation.

        The current switchboard integration that is in control of the conversation. This field is omitted if no `activeSwitchboardIntegration` exists for the conversation.  # noqa: E501

        :param active_switchboard_integration: The active_switchboard_integration of this Conversation.  # noqa: E501
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
        """Gets the pending_switchboard_integration of this Conversation.  # noqa: E501

        The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control.  # noqa: E501

        :return: The pending_switchboard_integration of this Conversation.  # noqa: E501
        :rtype: SwitchboardIntegrationWebhook
        """
        return self._pending_switchboard_integration

    @pending_switchboard_integration.setter
    def pending_switchboard_integration(self, pending_switchboard_integration):
        """Sets the pending_switchboard_integration of this Conversation.

        The switchboard integration that is awaiting control. This field is omitted if no switchboard integration has been previously offered control.  # noqa: E501

        :param pending_switchboard_integration: The pending_switchboard_integration of this Conversation.  # noqa: E501
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

    @property
    def is_default(self):
        """Gets the is_default of this Conversation.  # noqa: E501

        Whether the conversation is the default conversation for the user. Will be true for the first personal conversation created for the user, and false in all other cases.   # noqa: E501

        :return: The is_default of this Conversation.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this Conversation.

        Whether the conversation is the default conversation for the user. Will be true for the first personal conversation created for the user, and false in all other cases.   # noqa: E501

        :param is_default: The is_default of this Conversation.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def display_name(self):
        """Gets the display_name of this Conversation.  # noqa: E501

        A friendly name for the conversation, may be displayed to the business or the user.   # noqa: E501

        :return: The display_name of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Conversation.

        A friendly name for the conversation, may be displayed to the business or the user.   # noqa: E501

        :param display_name: The display_name of this Conversation.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Conversation.  # noqa: E501

        A short text describing the conversation.  # noqa: E501

        :return: The description of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Conversation.

        A short text describing the conversation.  # noqa: E501

        :param description: The description of this Conversation.  # noqa: E501
        :type: str
        """
        if type(description) is Undefined:
            description = None
            self.nulls.discard("description")
        elif description is None:
            self.nulls.add("description")
        else:
            self.nulls.discard("description")
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 100):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this Conversation.  # noqa: E501

        A custom conversation icon url. The image must be in either JPG, PNG, or GIF format  # noqa: E501

        :return: The icon_url of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Conversation.

        A custom conversation icon url. The image must be in either JPG, PNG, or GIF format  # noqa: E501

        :param icon_url: The icon_url of this Conversation.  # noqa: E501
        :type: str
        """
        if type(icon_url) is Undefined:
            icon_url = None
            self.nulls.discard("icon_url")
        elif icon_url is None:
            self.nulls.add("icon_url")
        else:
            self.nulls.discard("icon_url")
        if (self.local_vars_configuration.client_side_validation and
                icon_url is not None and len(icon_url) > 2048):
            raise ValueError("Invalid value for `icon_url`, length must be less than or equal to `2048`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                icon_url is not None and len(icon_url) < 1):
            raise ValueError("Invalid value for `icon_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._icon_url = icon_url

    @property
    def metadata(self):
        """Gets the metadata of this Conversation.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this Conversation.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Conversation.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this Conversation.  # noqa: E501
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
    def business_last_read(self):
        """Gets the business_last_read of this Conversation.  # noqa: E501

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the conversation was last marked as read with role business.   # noqa: E501

        :return: The business_last_read of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._business_last_read

    @business_last_read.setter
    def business_last_read(self, business_last_read):
        """Sets the business_last_read of this Conversation.

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the conversation was last marked as read with role business.   # noqa: E501

        :param business_last_read: The business_last_read of this Conversation.  # noqa: E501
        :type: str
        """
        if type(business_last_read) is Undefined:
            business_last_read = None
            self.nulls.discard("business_last_read")
        elif business_last_read is None:
            self.nulls.add("business_last_read")
        else:
            self.nulls.discard("business_last_read")

        self._business_last_read = business_last_read

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this Conversation.  # noqa: E501

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the last message was received in the conversation, or the creation time if no messages have been received yet.   # noqa: E501

        :return: The last_updated_at of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this Conversation.

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the moment the last message was received in the conversation, or the creation time if no messages have been received yet.   # noqa: E501

        :param last_updated_at: The last_updated_at of this Conversation.  # noqa: E501
        :type: str
        """
        if type(last_updated_at) is Undefined:
            last_updated_at = None
            self.nulls.discard("last_updated_at")
        elif last_updated_at is None:
            self.nulls.add("last_updated_at")
        else:
            self.nulls.discard("last_updated_at")

        self._last_updated_at = last_updated_at

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
        if not isinstance(other, Conversation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Conversation):
            return True

        return self.to_dict() != other.to_dict()
