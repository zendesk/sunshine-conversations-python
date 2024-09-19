# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 13.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Content(object):
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
        'actions': 'list[ActionSubset]',
        'payload': 'str',
        'items': 'list[Item]',
        'display_settings': 'CarouselMessageDisplaySettings',
        'media_url': 'str',
        'media_size': 'float',
        'media_type': 'str',
        'alt_text': 'str',
        'attachment_id': 'str',
        'submitted': 'bool',
        'block_chat_input': 'bool',
        'fields': 'list[FormResponseMessageField]',
        'text_fallback': 'str',
        'coordinates': 'LocationMessageCoordinates',
        'location': 'LocationMessageLocation',
        'template': 'object'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'actions': 'actions',
        'payload': 'payload',
        'items': 'items',
        'display_settings': 'displaySettings',
        'media_url': 'mediaUrl',
        'media_size': 'mediaSize',
        'media_type': 'mediaType',
        'alt_text': 'altText',
        'attachment_id': 'attachmentId',
        'submitted': 'submitted',
        'block_chat_input': 'blockChatInput',
        'fields': 'fields',
        'text_fallback': 'textFallback',
        'coordinates': 'coordinates',
        'location': 'location',
        'template': 'template'
    }

    nulls = set()

    discriminator_value_class_map = {
    }

    def __init__(self, type='template', text=None, actions=None, payload=None, items=None, display_settings=None, media_url=None, media_size=None, media_type=None, alt_text=None, attachment_id=None, submitted=None, block_chat_input=None, fields=None, text_fallback=None, coordinates=None, location=None, template=None, local_vars_configuration=None):  # noqa: E501
        """Content - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._actions = None
        self._payload = None
        self._items = None
        self._display_settings = None
        self._media_url = None
        self._media_size = None
        self._media_type = None
        self._alt_text = None
        self._attachment_id = None
        self._submitted = None
        self._block_chat_input = None
        self._fields = None
        self._text_fallback = None
        self._coordinates = None
        self._location = None
        self._template = None
        self.discriminator = 'type'

        self.type = type
        if text is not None:
            self.text = text
        if actions is not None:
            self.actions = actions
        if payload is not None:
            self.payload = payload
        self.items = items
        if display_settings is not None:
            self.display_settings = display_settings
        self.media_url = media_url
        if media_size is not None:
            self.media_size = media_size
        if media_type is not None:
            self.media_type = media_type
        if alt_text is not None:
            self.alt_text = alt_text
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if submitted is not None:
            self.submitted = submitted
        if block_chat_input is not None:
            self.block_chat_input = block_chat_input
        self.fields = fields
        if text_fallback is not None:
            self.text_fallback = text_fallback
        self.coordinates = coordinates
        if location is not None:
            self.location = location
        self.template = template

    @property
    def type(self):
        """Gets the type of this Content.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this Content.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Content.

        The type of message.  # noqa: E501

        :param type: The type of this Content.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def text(self):
        """Gets the text of this Content.  # noqa: E501

        The fallback text message used when location messages are not supported by the channel.  # noqa: E501

        :return: The text of this Content.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Content.

        The fallback text message used when location messages are not supported by the channel.  # noqa: E501

        :param text: The text of this Content.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def actions(self):
        """Gets the actions of this Content.  # noqa: E501

        An array of objects representing the actions associated with the message. The array length is limited by the third party channel.  # noqa: E501

        :return: The actions of this Content.  # noqa: E501
        :rtype: list[ActionSubset]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Content.

        An array of objects representing the actions associated with the message. The array length is limited by the third party channel.  # noqa: E501

        :param actions: The actions of this Content.  # noqa: E501
        :type: list[ActionSubset]
        """

        self._actions = actions

    @property
    def payload(self):
        """Gets the payload of this Content.  # noqa: E501

        The payload of a [reply button](https://docs.smooch.io/guide/structured-messages/#reply-buttons) response message.  # noqa: E501

        :return: The payload of this Content.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Content.

        The payload of a [reply button](https://docs.smooch.io/guide/structured-messages/#reply-buttons) response message.  # noqa: E501

        :param payload: The payload of this Content.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def items(self):
        """Gets the items of this Content.  # noqa: E501

        An array of objects representing the items associated with the message. Only present in carousel and list type messages.  # noqa: E501

        :return: The items of this Content.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Content.

        An array of objects representing the items associated with the message. Only present in carousel and list type messages.  # noqa: E501

        :param items: The items of this Content.  # noqa: E501
        :type: list[Item]
        """

        self._items = items

    @property
    def display_settings(self):
        """Gets the display_settings of this Content.  # noqa: E501


        :return: The display_settings of this Content.  # noqa: E501
        :rtype: CarouselMessageDisplaySettings
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        """Sets the display_settings of this Content.


        :param display_settings: The display_settings of this Content.  # noqa: E501
        :type: CarouselMessageDisplaySettings
        """

        self._display_settings = display_settings

    @property
    def media_url(self):
        """Gets the media_url of this Content.  # noqa: E501

        The URL for media, such as an image, attached to the message.  # noqa: E501

        :return: The media_url of this Content.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this Content.

        The URL for media, such as an image, attached to the message.  # noqa: E501

        :param media_url: The media_url of this Content.  # noqa: E501
        :type: str
        """

        self._media_url = media_url

    @property
    def media_size(self):
        """Gets the media_size of this Content.  # noqa: E501

        The size of the media in bytes.  # noqa: E501

        :return: The media_size of this Content.  # noqa: E501
        :rtype: float
        """
        return self._media_size

    @media_size.setter
    def media_size(self, media_size):
        """Sets the media_size of this Content.

        The size of the media in bytes.  # noqa: E501

        :param media_size: The media_size of this Content.  # noqa: E501
        :type: float
        """

        self._media_size = media_size

    @property
    def media_type(self):
        """Gets the media_type of this Content.  # noqa: E501

        The type of media.  # noqa: E501

        :return: The media_type of this Content.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Content.

        The type of media.  # noqa: E501

        :param media_type: The media_type of this Content.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                media_type is not None and len(media_type) > 128):
            raise ValueError("Invalid value for `media_type`, length must be less than or equal to `128`")  # noqa: E501

        self._media_type = media_type

    @property
    def alt_text(self):
        """Gets the alt_text of this Content.  # noqa: E501

        An optional description of the image for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :return: The alt_text of this Content.  # noqa: E501
        :rtype: str
        """
        return self._alt_text

    @alt_text.setter
    def alt_text(self, alt_text):
        """Sets the alt_text of this Content.

        An optional description of the image for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :param alt_text: The alt_text of this Content.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alt_text is not None and len(alt_text) > 128):
            raise ValueError("Invalid value for `alt_text`, length must be less than or equal to `128`")  # noqa: E501

        self._alt_text = alt_text

    @property
    def attachment_id(self):
        """Gets the attachment_id of this Content.  # noqa: E501

        An identifier used by Sunshine Conversations for internal purposes.  # noqa: E501

        :return: The attachment_id of this Content.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this Content.

        An identifier used by Sunshine Conversations for internal purposes.  # noqa: E501

        :param attachment_id: The attachment_id of this Content.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

    @property
    def submitted(self):
        """Gets the submitted of this Content.  # noqa: E501

        Flag which states whether the form is submitted.  # noqa: E501

        :return: The submitted of this Content.  # noqa: E501
        :rtype: bool
        """
        return self._submitted

    @submitted.setter
    def submitted(self, submitted):
        """Sets the submitted of this Content.

        Flag which states whether the form is submitted.  # noqa: E501

        :param submitted: The submitted of this Content.  # noqa: E501
        :type: bool
        """

        self._submitted = submitted

    @property
    def block_chat_input(self):
        """Gets the block_chat_input of this Content.  # noqa: E501

        true if the message should block the chat input on Web Messenger.  # noqa: E501

        :return: The block_chat_input of this Content.  # noqa: E501
        :rtype: bool
        """
        return self._block_chat_input

    @block_chat_input.setter
    def block_chat_input(self, block_chat_input):
        """Sets the block_chat_input of this Content.

        true if the message should block the chat input on Web Messenger.  # noqa: E501

        :param block_chat_input: The block_chat_input of this Content.  # noqa: E501
        :type: bool
        """

        self._block_chat_input = block_chat_input

    @property
    def fields(self):
        """Gets the fields of this Content.  # noqa: E501

        Array of field objects that contain the submitted fields.  # noqa: E501

        :return: The fields of this Content.  # noqa: E501
        :rtype: list[FormResponseMessageField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Content.

        Array of field objects that contain the submitted fields.  # noqa: E501

        :param fields: The fields of this Content.  # noqa: E501
        :type: list[FormResponseMessageField]
        """

        self._fields = fields

    @property
    def text_fallback(self):
        """Gets the text_fallback of this Content.  # noqa: E501

        A string containing the `label: value` of all fields, each separated by a newline character.  # noqa: E501

        :return: The text_fallback of this Content.  # noqa: E501
        :rtype: str
        """
        return self._text_fallback

    @text_fallback.setter
    def text_fallback(self, text_fallback):
        """Sets the text_fallback of this Content.

        A string containing the `label: value` of all fields, each separated by a newline character.  # noqa: E501

        :param text_fallback: The text_fallback of this Content.  # noqa: E501
        :type: str
        """

        self._text_fallback = text_fallback

    @property
    def coordinates(self):
        """Gets the coordinates of this Content.  # noqa: E501


        :return: The coordinates of this Content.  # noqa: E501
        :rtype: LocationMessageCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Content.


        :param coordinates: The coordinates of this Content.  # noqa: E501
        :type: LocationMessageCoordinates
        """

        self._coordinates = coordinates

    @property
    def location(self):
        """Gets the location of this Content.  # noqa: E501


        :return: The location of this Content.  # noqa: E501
        :rtype: LocationMessageLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Content.


        :param location: The location of this Content.  # noqa: E501
        :type: LocationMessageLocation
        """

        self._location = location

    @property
    def template(self):
        """Gets the template of this Content.  # noqa: E501

        The whatsapp template message to send. For more information, consult the [guide](https://docs.smooch.io/guide/whatsapp#sending-message-templates). `schema` must be set to `whatsapp`.  # noqa: E501

        :return: The template of this Content.  # noqa: E501
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Content.

        The whatsapp template message to send. For more information, consult the [guide](https://docs.smooch.io/guide/whatsapp#sending-message-templates). `schema` must be set to `whatsapp`.  # noqa: E501

        :param template: The template of this Content.  # noqa: E501
        :type: object
        """

        self._template = template

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        if self.discriminator is None:
            return
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, Content):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Content):
            return True

        return self.to_dict() != other.to_dict()
