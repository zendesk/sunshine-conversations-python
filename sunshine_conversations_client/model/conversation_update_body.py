# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ConversationUpdateBody(object):
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
        'display_name': 'str',
        'description': 'str',
        'icon_url': 'str',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'icon_url': 'iconUrl',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, display_name=None, description=Undefined(), icon_url=Undefined(), metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """ConversationUpdateBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._description = None
        self._icon_url = None
        self._metadata = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        self.description = description
        self.icon_url = icon_url
        self.metadata = metadata

    @property
    def display_name(self):
        """Gets the display_name of this ConversationUpdateBody.  # noqa: E501

        A friendly name for the conversation, may be displayed to the business or the user.   # noqa: E501

        :return: The display_name of this ConversationUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ConversationUpdateBody.

        A friendly name for the conversation, may be displayed to the business or the user.   # noqa: E501

        :param display_name: The display_name of this ConversationUpdateBody.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ConversationUpdateBody.  # noqa: E501

        A short text describing the conversation.  # noqa: E501

        :return: The description of this ConversationUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConversationUpdateBody.

        A short text describing the conversation.  # noqa: E501

        :param description: The description of this ConversationUpdateBody.  # noqa: E501
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
        """Gets the icon_url of this ConversationUpdateBody.  # noqa: E501

        A custom conversation icon url. The image must be in either JPG, PNG, or GIF format  # noqa: E501

        :return: The icon_url of this ConversationUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this ConversationUpdateBody.

        A custom conversation icon url. The image must be in either JPG, PNG, or GIF format  # noqa: E501

        :param icon_url: The icon_url of this ConversationUpdateBody.  # noqa: E501
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
        """Gets the metadata of this ConversationUpdateBody.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this ConversationUpdateBody.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ConversationUpdateBody.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this ConversationUpdateBody.  # noqa: E501
        :type: dict(str, object)
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

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
        if not isinstance(other, ConversationUpdateBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationUpdateBody):
            return True

        return self.to_dict() != other.to_dict()
