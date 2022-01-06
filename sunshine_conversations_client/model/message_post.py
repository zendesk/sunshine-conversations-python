# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MessagePost(object):
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
        'author': 'Author',
        'content': 'Content',
        'destination': 'Destination',
        'metadata': 'object',
        'override': 'MessageOverride',
        'schema': 'str'
    }

    attribute_map = {
        'author': 'author',
        'content': 'content',
        'destination': 'destination',
        'metadata': 'metadata',
        'override': 'override',
        'schema': 'schema'
    }

    nulls = set()

    def __init__(self, author=None, content=None, destination=None, metadata=Undefined(), override=None, schema=None, local_vars_configuration=None):  # noqa: E501
        """MessagePost - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._content = None
        self._destination = None
        self._metadata = None
        self._override = None
        self._schema = None
        self.discriminator = None

        self.author = author
        self.content = content
        if destination is not None:
            self.destination = destination
        self.metadata = metadata
        if override is not None:
            self.override = override
        if schema is not None:
            self.schema = schema

    @property
    def author(self):
        """Gets the author of this MessagePost.  # noqa: E501

        The author of the message.  # noqa: E501

        :return: The author of this MessagePost.  # noqa: E501
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this MessagePost.

        The author of the message.  # noqa: E501

        :param author: The author of this MessagePost.  # noqa: E501
        :type: Author
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def content(self):
        """Gets the content of this MessagePost.  # noqa: E501

        The content of the message.  # noqa: E501

        :return: The content of this MessagePost.  # noqa: E501
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MessagePost.

        The content of the message.  # noqa: E501

        :param content: The content of this MessagePost.  # noqa: E501
        :type: Content
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def destination(self):
        """Gets the destination of this MessagePost.  # noqa: E501


        :return: The destination of this MessagePost.  # noqa: E501
        :rtype: Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this MessagePost.


        :param destination: The destination of this MessagePost.  # noqa: E501
        :type: Destination
        """

        self._destination = destination

    @property
    def metadata(self):
        """Gets the metadata of this MessagePost.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this MessagePost.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MessagePost.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this MessagePost.  # noqa: E501
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
    def override(self):
        """Gets the override of this MessagePost.  # noqa: E501


        :return: The override of this MessagePost.  # noqa: E501
        :rtype: MessageOverride
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this MessagePost.


        :param override: The override of this MessagePost.  # noqa: E501
        :type: MessageOverride
        """

        self._override = override

    @property
    def schema(self):
        """Gets the schema of this MessagePost.  # noqa: E501

        When `schema` is set to `\"whatsapp\"`, the `content` key is expected to conform to the [native WhatsApp schema](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates) for sending message templates. For more details, consult the documentation for [sending message templates on WhatsApp](https://docs.smooch.io/guide/whatsapp/#sending-message-templates).   # noqa: E501

        :return: The schema of this MessagePost.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this MessagePost.

        When `schema` is set to `\"whatsapp\"`, the `content` key is expected to conform to the [native WhatsApp schema](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates) for sending message templates. For more details, consult the documentation for [sending message templates on WhatsApp](https://docs.smooch.io/guide/whatsapp/#sending-message-templates).   # noqa: E501

        :param schema: The schema of this MessagePost.  # noqa: E501
        :type: str
        """

        self._schema = schema

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
        if not isinstance(other, MessagePost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessagePost):
            return True

        return self.to_dict() != other.to_dict()