# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Item(object):
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
        'title': 'str',
        'description': 'str',
        'media_url': 'str',
        'media_type': 'str',
        'alt_text': 'str',
        'size': 'str',
        'actions': 'list[ActionSubset]',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'media_url': 'mediaUrl',
        'media_type': 'mediaType',
        'alt_text': 'altText',
        'size': 'size',
        'actions': 'actions',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, title=None, description=None, media_url=None, media_type=None, alt_text=None, size=None, actions=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Item - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._description = None
        self._media_url = None
        self._media_type = None
        self._alt_text = None
        self._size = None
        self._actions = None
        self._metadata = None
        self.discriminator = None

        self.title = title
        if description is not None:
            self.description = description
        if media_url is not None:
            self.media_url = media_url
        if media_type is not None:
            self.media_type = media_type
        if alt_text is not None:
            self.alt_text = alt_text
        if size is not None:
            self.size = size
        self.actions = actions
        self.metadata = metadata

    @property
    def title(self):
        """Gets the title of this Item.  # noqa: E501

        The title of the item.  # noqa: E501

        :return: The title of this Item.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Item.

        The title of the item.  # noqa: E501

        :param title: The title of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 128):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Item.  # noqa: E501

        The description of the item.  # noqa: E501

        :return: The description of this Item.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Item.

        The description of the item.  # noqa: E501

        :param description: The description of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 128):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501

        self._description = description

    @property
    def media_url(self):
        """Gets the media_url of this Item.  # noqa: E501

        The image url attached to the item.  # noqa: E501

        :return: The media_url of this Item.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this Item.

        The image url attached to the item.  # noqa: E501

        :param media_url: The media_url of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                media_url is not None and len(media_url) > 2048):
            raise ValueError("Invalid value for `media_url`, length must be less than or equal to `2048`")  # noqa: E501

        self._media_url = media_url

    @property
    def media_type(self):
        """Gets the media_type of this Item.  # noqa: E501

        The MIME type for any image attached in the mediaUrl.  # noqa: E501

        :return: The media_type of this Item.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Item.

        The MIME type for any image attached in the mediaUrl.  # noqa: E501

        :param media_type: The media_type of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                media_type is not None and len(media_type) > 128):
            raise ValueError("Invalid value for `media_type`, length must be less than or equal to `128`")  # noqa: E501

        self._media_type = media_type

    @property
    def alt_text(self):
        """Gets the alt_text of this Item.  # noqa: E501

        An optional description of the media for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :return: The alt_text of this Item.  # noqa: E501
        :rtype: str
        """
        return self._alt_text

    @alt_text.setter
    def alt_text(self, alt_text):
        """Sets the alt_text of this Item.

        An optional description of the media for accessibility purposes. The field will be saved by default with the file name as the value.  # noqa: E501

        :param alt_text: The alt_text of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alt_text is not None and len(alt_text) > 128):
            raise ValueError("Invalid value for `alt_text`, length must be less than or equal to `128`")  # noqa: E501

        self._alt_text = alt_text

    @property
    def size(self):
        """Gets the size of this Item.  # noqa: E501

        The size of the image.  # noqa: E501

        :return: The size of this Item.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Item.

        The size of the image.  # noqa: E501

        :param size: The size of this Item.  # noqa: E501
        :type: str
        """
        allowed_values = ["compact", "large"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

        self._size = size

    @property
    def actions(self):
        """Gets the actions of this Item.  # noqa: E501

        An array of objects representing the actions associated with the item.  # noqa: E501

        :return: The actions of this Item.  # noqa: E501
        :rtype: list[ActionSubset]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Item.

        An array of objects representing the actions associated with the item.  # noqa: E501

        :param actions: The actions of this Item.  # noqa: E501
        :type: list[ActionSubset]
        """
        if self.local_vars_configuration.client_side_validation and actions is None:  # noqa: E501
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def metadata(self):
        """Gets the metadata of this Item.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this Item.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Item.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this Item.  # noqa: E501
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
        if not isinstance(other, Item):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Item):
            return True

        return self.to_dict() != other.to_dict()
