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


class ImageMessage(object):
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
        'media_url': 'str',
        'alt_text': 'str',
        'text': 'str',
        'actions': 'list[Action]'
    }

    attribute_map = {
        'type': 'type',
        'media_url': 'mediaUrl',
        'alt_text': 'altText',
        'text': 'text',
        'actions': 'actions'
    }

    nulls = set()

    def __init__(self, type='image', media_url=None, alt_text=None, text=None, actions=None, local_vars_configuration=None):  # noqa: E501
        """ImageMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._media_url = None
        self._alt_text = None
        self._text = None
        self._actions = None
        self.discriminator = None

        self.type = type
        self.media_url = media_url
        if alt_text is not None:
            self.alt_text = alt_text
        if text is not None:
            self.text = text
        if actions is not None:
            self.actions = actions

    @property
    def type(self):
        """Gets the type of this ImageMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageMessage.

        The type of message.  # noqa: E501

        :param type: The type of this ImageMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def media_url(self):
        """Gets the media_url of this ImageMessage.  # noqa: E501

        The URL for media, such as an image, attached to the message.  # noqa: E501

        :return: The media_url of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this ImageMessage.

        The URL for media, such as an image, attached to the message.  # noqa: E501

        :param media_url: The media_url of this ImageMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and media_url is None:  # noqa: E501
            raise ValueError("Invalid value for `media_url`, must not be `None`")  # noqa: E501

        self._media_url = media_url

    @property
    def alt_text(self):
        """Gets the alt_text of this ImageMessage.  # noqa: E501

        An optional description of the image for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :return: The alt_text of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._alt_text

    @alt_text.setter
    def alt_text(self, alt_text):
        """Sets the alt_text of this ImageMessage.

        An optional description of the image for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :param alt_text: The alt_text of this ImageMessage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alt_text is not None and len(alt_text) > 128):
            raise ValueError("Invalid value for `alt_text`, length must be less than or equal to `128`")  # noqa: E501

        self._alt_text = alt_text

    @property
    def text(self):
        """Gets the text of this ImageMessage.  # noqa: E501

        The text content of the message. Optional only if actions are provided.  # noqa: E501

        :return: The text of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ImageMessage.

        The text content of the message. Optional only if actions are provided.  # noqa: E501

        :param text: The text of this ImageMessage.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def actions(self):
        """Gets the actions of this ImageMessage.  # noqa: E501

        Array of message actions.  # noqa: E501

        :return: The actions of this ImageMessage.  # noqa: E501
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ImageMessage.

        Array of message actions.  # noqa: E501

        :param actions: The actions of this ImageMessage.  # noqa: E501
        :type: list[Action]
        """

        self._actions = actions

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
        if not isinstance(other, ImageMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageMessage):
            return True

        return self.to_dict() != other.to_dict()
