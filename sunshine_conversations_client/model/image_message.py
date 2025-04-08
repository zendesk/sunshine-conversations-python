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
        'media_type': 'str',
        'media_size': 'float',
        'alt_text': 'str',
        'text': 'str',
        'html_text': 'str',
        'markdown_text': 'str',
        'actions': 'list[Action]',
        'attachment_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'media_url': 'mediaUrl',
        'media_type': 'mediaType',
        'media_size': 'mediaSize',
        'alt_text': 'altText',
        'text': 'text',
        'html_text': 'htmlText',
        'markdown_text': 'markdownText',
        'actions': 'actions',
        'attachment_id': 'attachmentId'
    }

    nulls = set()

    def __init__(self, type='image', media_url=None, media_type=None, media_size=None, alt_text=None, text=None, html_text=None, markdown_text=None, actions=None, attachment_id=None, local_vars_configuration=None):  # noqa: E501
        """ImageMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._media_url = None
        self._media_type = None
        self._media_size = None
        self._alt_text = None
        self._text = None
        self._html_text = None
        self._markdown_text = None
        self._actions = None
        self._attachment_id = None
        self.discriminator = None

        self.type = type
        self.media_url = media_url
        if media_type is not None:
            self.media_type = media_type
        if media_size is not None:
            self.media_size = media_size
        if alt_text is not None:
            self.alt_text = alt_text
        if text is not None:
            self.text = text
        if html_text is not None:
            self.html_text = html_text
        if markdown_text is not None:
            self.markdown_text = markdown_text
        if actions is not None:
            self.actions = actions
        if attachment_id is not None:
            self.attachment_id = attachment_id

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

        The URL for media, such as an image, attached to the message. <aside class=\"notice\">Note that for private attachments an authorization header is required to access the mediaUrl. See [configuring private attachments for messaging](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/messaging_private_attachments/) guide for more details.</aside>   # noqa: E501

        :return: The media_url of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this ImageMessage.

        The URL for media, such as an image, attached to the message. <aside class=\"notice\">Note that for private attachments an authorization header is required to access the mediaUrl. See [configuring private attachments for messaging](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/messaging_private_attachments/) guide for more details.</aside>   # noqa: E501

        :param media_url: The media_url of this ImageMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and media_url is None:  # noqa: E501
            raise ValueError("Invalid value for `media_url`, must not be `None`")  # noqa: E501

        self._media_url = media_url

    @property
    def media_type(self):
        """Gets the media_type of this ImageMessage.  # noqa: E501

        The type of media.  # noqa: E501

        :return: The media_type of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ImageMessage.

        The type of media.  # noqa: E501

        :param media_type: The media_type of this ImageMessage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                media_type is not None and len(media_type) > 128):
            raise ValueError("Invalid value for `media_type`, length must be less than or equal to `128`")  # noqa: E501

        self._media_type = media_type

    @property
    def media_size(self):
        """Gets the media_size of this ImageMessage.  # noqa: E501

        The size of the media in bytes.  # noqa: E501

        :return: The media_size of this ImageMessage.  # noqa: E501
        :rtype: float
        """
        return self._media_size

    @media_size.setter
    def media_size(self, media_size):
        """Sets the media_size of this ImageMessage.

        The size of the media in bytes.  # noqa: E501

        :param media_size: The media_size of this ImageMessage.  # noqa: E501
        :type: float
        """

        self._media_size = media_size

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

        The text content of the message.  # noqa: E501

        :return: The text of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ImageMessage.

        The text content of the message.  # noqa: E501

        :param text: The text of this ImageMessage.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def html_text(self):
        """Gets the html_text of this ImageMessage.  # noqa: E501

        HTML text content of the message. Can be provided in place of `text`. Cannot be used with `markdownText`. If no `text` is provided, will be converted to `text` upon reception to be displayed on channels that do not support rich text. See [rich text](https://docs.smooch.io/guide/structured-messages/rich-text) documentation for more information.  # noqa: E501

        :return: The html_text of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._html_text

    @html_text.setter
    def html_text(self, html_text):
        """Sets the html_text of this ImageMessage.

        HTML text content of the message. Can be provided in place of `text`. Cannot be used with `markdownText`. If no `text` is provided, will be converted to `text` upon reception to be displayed on channels that do not support rich text. See [rich text](https://docs.smooch.io/guide/structured-messages/rich-text) documentation for more information.  # noqa: E501

        :param html_text: The html_text of this ImageMessage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                html_text is not None and len(html_text) > 4096):
            raise ValueError("Invalid value for `html_text`, length must be less than or equal to `4096`")  # noqa: E501

        self._html_text = html_text

    @property
    def markdown_text(self):
        """Gets the markdown_text of this ImageMessage.  # noqa: E501

        Markdown text content of the message. Can be provided in place of `text`. Cannot be used with `htmlText`. Will be converted to `htmlText` upon reception. If converted `htmlText` exceeds 4096 characters, the message will be rejected. If no `text` is provided, will be converted to `text` upon reception to be displayed on channels that do not support rich text. See [rich text](https://docs.smooch.io/guide/structured-messages/rich-text) documentation for more information.  # noqa: E501

        :return: The markdown_text of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._markdown_text

    @markdown_text.setter
    def markdown_text(self, markdown_text):
        """Sets the markdown_text of this ImageMessage.

        Markdown text content of the message. Can be provided in place of `text`. Cannot be used with `htmlText`. Will be converted to `htmlText` upon reception. If converted `htmlText` exceeds 4096 characters, the message will be rejected. If no `text` is provided, will be converted to `text` upon reception to be displayed on channels that do not support rich text. See [rich text](https://docs.smooch.io/guide/structured-messages/rich-text) documentation for more information.  # noqa: E501

        :param markdown_text: The markdown_text of this ImageMessage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                markdown_text is not None and len(markdown_text) > 4096):
            raise ValueError("Invalid value for `markdown_text`, length must be less than or equal to `4096`")  # noqa: E501

        self._markdown_text = markdown_text

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

    @property
    def attachment_id(self):
        """Gets the attachment_id of this ImageMessage.  # noqa: E501

        An identifier used by Sunshine Conversations for internal purposes.  # noqa: E501

        :return: The attachment_id of this ImageMessage.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this ImageMessage.

        An identifier used by Sunshine Conversations for internal purposes.  # noqa: E501

        :param attachment_id: The attachment_id of this ImageMessage.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

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
