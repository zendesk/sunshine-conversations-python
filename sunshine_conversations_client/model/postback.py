# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 13.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Postback(object):
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
        'metadata': 'object'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'payload': 'payload',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, type='postback', text=None, payload=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Postback - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._payload = None
        self._metadata = None
        self.discriminator = None

        self.type = type
        self.text = text
        self.payload = payload
        self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this Postback.  # noqa: E501

        The type of action.  # noqa: E501

        :return: The type of this Postback.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Postback.

        The type of action.  # noqa: E501

        :param type: The type of this Postback.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def text(self):
        """Gets the text of this Postback.  # noqa: E501

        The button text.  # noqa: E501

        :return: The text of this Postback.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Postback.

        The button text.  # noqa: E501

        :param text: The text of this Postback.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def payload(self):
        """Gets the payload of this Postback.  # noqa: E501

        The payload of a postback or reply button.  # noqa: E501

        :return: The payload of this Postback.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Postback.

        The payload of a postback or reply button.  # noqa: E501

        :param payload: The payload of this Postback.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def metadata(self):
        """Gets the metadata of this Postback.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this Postback.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Postback.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this Postback.  # noqa: E501
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
        if not isinstance(other, Postback):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Postback):
            return True

        return self.to_dict() != other.to_dict()
