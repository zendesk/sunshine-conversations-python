# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Reply(object):
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
        'text': 'str',
        'payload': 'str',
        'metadata': 'object',
        'icon_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'payload': 'payload',
        'metadata': 'metadata',
        'icon_url': 'iconUrl'
    }

    nulls = set()

    def __init__(self, type=None, text=None, payload=None, metadata=Undefined(), icon_url=None, local_vars_configuration=None):  # noqa: E501
        """Reply - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._payload = None
        self._metadata = None
        self._icon_url = None
        self.discriminator = None

        self.type = type
        self.text = text
        self.payload = payload
        self.metadata = metadata
        if icon_url is not None:
            self.icon_url = icon_url

    @property
    def type(self):
        """Gets the type of this Reply.  # noqa: E501

        The type of action.  # noqa: E501

        :return: The type of this Reply.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Reply.

        The type of action.  # noqa: E501

        :param type: The type of this Reply.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def text(self):
        """Gets the text of this Reply.  # noqa: E501

        The button text. We recommend a non-empty value because some channels may not support empty ones. Text longer than 20 characters will be truncated on Facebook Messenger, and longer than 40 characters will be truncated on Web Messenger, iOS, and Android.  # noqa: E501

        :return: The text of this Reply.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Reply.

        The button text. We recommend a non-empty value because some channels may not support empty ones. Text longer than 20 characters will be truncated on Facebook Messenger, and longer than 40 characters will be truncated on Web Messenger, iOS, and Android.  # noqa: E501

        :param text: The text of this Reply.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def payload(self):
        """Gets the payload of this Reply.  # noqa: E501

        A string payload to help you identify the action context. Used when posting the reply. You can also use metadata for more complex needs.  # noqa: E501

        :return: The payload of this Reply.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Reply.

        A string payload to help you identify the action context. Used when posting the reply. You can also use metadata for more complex needs.  # noqa: E501

        :param payload: The payload of this Reply.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def metadata(self):
        """Gets the metadata of this Reply.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this Reply.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Reply.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this Reply.  # noqa: E501
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
    def icon_url(self):
        """Gets the icon_url of this Reply.  # noqa: E501

        An icon to render next to the reply option.  # noqa: E501

        :return: The icon_url of this Reply.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Reply.

        An icon to render next to the reply option.  # noqa: E501

        :param icon_url: The icon_url of this Reply.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

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
        if not isinstance(other, Reply):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Reply):
            return True

        return self.to_dict() != other.to_dict()
