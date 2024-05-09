# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class ConversationMessageDeliveryPayloadDestination(object):
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
        'integration_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'integration_id': 'integrationId'
    }

    nulls = set()

    def __init__(self, type=None, integration_id=None, local_vars_configuration=None):  # noqa: E501
        """ConversationMessageDeliveryPayloadDestination - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._integration_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if integration_id is not None:
            self.integration_id = integration_id

    @property
    def type(self):
        """Gets the type of this ConversationMessageDeliveryPayloadDestination.  # noqa: E501

        An identifier for the channel to which a message was sent to. May include one of \"web\", \"ios\", \"android\", \"messenger\", \"viber\", \"telegram\", \"wechat\", \"line\", \"twilio\", \"api\", \"notification\", or any other channel.  # noqa: E501

        :return: The type of this ConversationMessageDeliveryPayloadDestination.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConversationMessageDeliveryPayloadDestination.

        An identifier for the channel to which a message was sent to. May include one of \"web\", \"ios\", \"android\", \"messenger\", \"viber\", \"telegram\", \"wechat\", \"line\", \"twilio\", \"api\", \"notification\", or any other channel.  # noqa: E501

        :param type: The type of this ConversationMessageDeliveryPayloadDestination.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def integration_id(self):
        """Gets the integration_id of this ConversationMessageDeliveryPayloadDestination.  # noqa: E501

        Identifier indicating which integration the message was sent to.  # noqa: E501

        :return: The integration_id of this ConversationMessageDeliveryPayloadDestination.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this ConversationMessageDeliveryPayloadDestination.

        Identifier indicating which integration the message was sent to.  # noqa: E501

        :param integration_id: The integration_id of this ConversationMessageDeliveryPayloadDestination.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

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
        if not isinstance(other, ConversationMessageDeliveryPayloadDestination):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversationMessageDeliveryPayloadDestination):
            return True

        return self.to_dict() != other.to_dict()
