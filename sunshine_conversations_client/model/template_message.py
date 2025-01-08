# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.3.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class TemplateMessage(object):
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
        'template': 'object'
    }

    attribute_map = {
        'type': 'type',
        'template': 'template'
    }

    nulls = set()

    def __init__(self, type='template', template=None, local_vars_configuration=None):  # noqa: E501
        """TemplateMessage - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._template = None
        self.discriminator = None

        self.type = type
        self.template = template

    @property
    def type(self):
        """Gets the type of this TemplateMessage.  # noqa: E501

        The type of message.  # noqa: E501

        :return: The type of this TemplateMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateMessage.

        The type of message.  # noqa: E501

        :param type: The type of this TemplateMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def template(self):
        """Gets the template of this TemplateMessage.  # noqa: E501

        The whatsapp template message to send. For more information, consult the [guide](https://docs.smooch.io/guide/whatsapp#sending-message-templates). `schema` must be set to `whatsapp`.  # noqa: E501

        :return: The template of this TemplateMessage.  # noqa: E501
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TemplateMessage.

        The whatsapp template message to send. For more information, consult the [guide](https://docs.smooch.io/guide/whatsapp#sending-message-templates). `schema` must be set to `whatsapp`.  # noqa: E501

        :param template: The template of this TemplateMessage.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

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
        if not isinstance(other, TemplateMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateMessage):
            return True

        return self.to_dict() != other.to_dict()
