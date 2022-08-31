# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.12.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Source(object):
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
        'integration_id': 'str',
        'original_message_id': 'str',
        'original_message_timestamp': 'str',
        'client': 'Client',
        'device': 'Device'
    }

    attribute_map = {
        'type': 'type',
        'integration_id': 'integrationId',
        'original_message_id': 'originalMessageId',
        'original_message_timestamp': 'originalMessageTimestamp',
        'client': 'client',
        'device': 'device'
    }

    nulls = set()

    def __init__(self, type=None, integration_id=Undefined(), original_message_id=Undefined(), original_message_timestamp=Undefined(), client=Undefined(), device=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Source - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._integration_id = None
        self._original_message_id = None
        self._original_message_timestamp = None
        self._client = None
        self._device = None
        self.discriminator = None

        self.type = type
        self.integration_id = integration_id
        self.original_message_id = original_message_id
        self.original_message_timestamp = original_message_timestamp
        self.client = client
        self.device = device

    @property
    def type(self):
        """Gets the type of this Source.  # noqa: E501

        An identifier for the channel from which a message originated. May include one of api, sdk, messenger, or any number of other channels.  # noqa: E501

        :return: The type of this Source.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Source.

        An identifier for the channel from which a message originated. May include one of api, sdk, messenger, or any number of other channels.  # noqa: E501

        :param type: The type of this Source.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def integration_id(self):
        """Gets the integration_id of this Source.  # noqa: E501

        Identifier indicating which integration the message was sent from. For user messages only.  # noqa: E501

        :return: The integration_id of this Source.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this Source.

        Identifier indicating which integration the message was sent from. For user messages only.  # noqa: E501

        :param integration_id: The integration_id of this Source.  # noqa: E501
        :type: str
        """
        if type(integration_id) is Undefined:
            integration_id = None
            self.nulls.discard("integration_id")
        elif integration_id is None:
            self.nulls.add("integration_id")
        else:
            self.nulls.discard("integration_id")

        self._integration_id = integration_id

    @property
    def original_message_id(self):
        """Gets the original_message_id of this Source.  # noqa: E501

        Message identifier assigned by the originating channel.  # noqa: E501

        :return: The original_message_id of this Source.  # noqa: E501
        :rtype: str
        """
        return self._original_message_id

    @original_message_id.setter
    def original_message_id(self, original_message_id):
        """Sets the original_message_id of this Source.

        Message identifier assigned by the originating channel.  # noqa: E501

        :param original_message_id: The original_message_id of this Source.  # noqa: E501
        :type: str
        """
        if type(original_message_id) is Undefined:
            original_message_id = None
            self.nulls.discard("original_message_id")
        elif original_message_id is None:
            self.nulls.add("original_message_id")
        else:
            self.nulls.discard("original_message_id")

        self._original_message_id = original_message_id

    @property
    def original_message_timestamp(self):
        """Gets the original_message_timestamp of this Source.  # noqa: E501

        A datetime string with the format `YYYY-MM-DDThh:mm:ss.SSSZ` representing when the third party channel received the message.  # noqa: E501

        :return: The original_message_timestamp of this Source.  # noqa: E501
        :rtype: str
        """
        return self._original_message_timestamp

    @original_message_timestamp.setter
    def original_message_timestamp(self, original_message_timestamp):
        """Sets the original_message_timestamp of this Source.

        A datetime string with the format `YYYY-MM-DDThh:mm:ss.SSSZ` representing when the third party channel received the message.  # noqa: E501

        :param original_message_timestamp: The original_message_timestamp of this Source.  # noqa: E501
        :type: str
        """
        if type(original_message_timestamp) is Undefined:
            original_message_timestamp = None
            self.nulls.discard("original_message_timestamp")
        elif original_message_timestamp is None:
            self.nulls.add("original_message_timestamp")
        else:
            self.nulls.discard("original_message_timestamp")

        self._original_message_timestamp = original_message_timestamp

    @property
    def client(self):
        """Gets the client of this Source.  # noqa: E501

        The client from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the `includeFullSource` option is enabled.  # noqa: E501

        :return: The client of this Source.  # noqa: E501
        :rtype: Client
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this Source.

        The client from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the `includeFullSource` option is enabled.  # noqa: E501

        :param client: The client of this Source.  # noqa: E501
        :type: Client
        """
        if type(client) is Undefined:
            client = None
            self.nulls.discard("client")
        elif client is None:
            self.nulls.add("client")
        else:
            self.nulls.discard("client")

        self._client = client

    @property
    def device(self):
        """Gets the device of this Source.  # noqa: E501

        The device from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the `includeFullSource` option is enabled.  # noqa: E501

        :return: The device of this Source.  # noqa: E501
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this Source.

        The device from which the user authored the message or activity, if applicable. This field is not applicable in API responses, it is used only in webhook payloads if the `includeFullSource` option is enabled.  # noqa: E501

        :param device: The device of this Source.  # noqa: E501
        :type: Device
        """
        if type(device) is Undefined:
            device = None
            self.nulls.discard("device")
        elif device is None:
            self.nulls.add("device")
        else:
            self.nulls.discard("device")

        self._device = device

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
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
