# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class QuotedMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, external_message_id=None, content=None):
        """
        QuotedMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'external_message_id': 'str',
            'content': 'Message'
        }

        self.attribute_map = {
            'type': 'type',
            'external_message_id': 'externalMessageId',
            'content': 'content'
        }

        self._type = None
        self._external_message_id = None
        self._content = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if external_message_id is not None:
          self.external_message_id = external_message_id
        if content is not None:
          self.content = content

    @property
    def type(self):
        """
        Gets the type of this QuotedMessage.
        The quoted message type. See [**QuotedMessageTypeEnum**](Enums.md#QuotedMessageTypeEnum) for available values.

        :return: The type of this QuotedMessage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this QuotedMessage.
        The quoted message type. See [**QuotedMessageTypeEnum**](Enums.md#QuotedMessageTypeEnum) for available values.

        :param type: The type of this QuotedMessage.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def external_message_id(self):
        """
        Gets the external_message_id of this QuotedMessage.
        The external message Id of the quoted message. Only for quoted messages with type set to externalMessageId. 

        :return: The external_message_id of this QuotedMessage.
        :rtype: str
        """
        return self._external_message_id

    @external_message_id.setter
    def external_message_id(self, external_message_id):
        """
        Sets the external_message_id of this QuotedMessage.
        The external message Id of the quoted message. Only for quoted messages with type set to externalMessageId. 

        :param external_message_id: The external_message_id of this QuotedMessage.
        :type: str
        """

        self._external_message_id = external_message_id

    @property
    def content(self):
        """
        Gets the content of this QuotedMessage.

        :return: The content of this QuotedMessage.
        :rtype: Message
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this QuotedMessage.

        :param content: The content of this QuotedMessage.
        :type: Message
        """

        self._content = content

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, QuotedMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
