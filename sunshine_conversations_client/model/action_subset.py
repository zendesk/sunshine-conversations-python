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


class ActionSubset(object):
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
        'amount': 'int',
        'currency': 'str',
        'metadata': 'dict(str, object)',
        'uri': 'str',
        'default': 'bool',
        'extra_channel_options': 'ExtraChannelOptions',
        'payload': 'str',
        'size': 'str',
        'fallback': 'str',
        'open_on_receive': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'text': 'text',
        'amount': 'amount',
        'currency': 'currency',
        'metadata': 'metadata',
        'uri': 'uri',
        'default': 'default',
        'extra_channel_options': 'extraChannelOptions',
        'payload': 'payload',
        'size': 'size',
        'fallback': 'fallback',
        'open_on_receive': 'openOnReceive'
    }

    nulls = set()

    discriminator_value_class_map = {
    }

    def __init__(self, type=None, text=None, amount=None, currency=None, metadata=Undefined(), uri=None, default=None, extra_channel_options=None, payload=None, size=None, fallback=None, open_on_receive=None, local_vars_configuration=None):  # noqa: E501
        """ActionSubset - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._text = None
        self._amount = None
        self._currency = None
        self._metadata = None
        self._uri = None
        self._default = None
        self._extra_channel_options = None
        self._payload = None
        self._size = None
        self._fallback = None
        self._open_on_receive = None
        self.discriminator = 'type'

        self.type = type
        self.text = text
        self.amount = amount
        if currency is not None:
            self.currency = currency
        self.metadata = metadata
        self.uri = uri
        if default is not None:
            self.default = default
        if extra_channel_options is not None:
            self.extra_channel_options = extra_channel_options
        self.payload = payload
        if size is not None:
            self.size = size
        self.fallback = fallback
        if open_on_receive is not None:
            self.open_on_receive = open_on_receive

    @property
    def type(self):
        """Gets the type of this ActionSubset.  # noqa: E501

        The type of action.  # noqa: E501

        :return: The type of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ActionSubset.

        The type of action.  # noqa: E501

        :param type: The type of this ActionSubset.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def text(self):
        """Gets the text of this ActionSubset.  # noqa: E501

        The button text.  # noqa: E501

        :return: The text of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ActionSubset.

        The button text.  # noqa: E501

        :param text: The text of this ActionSubset.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def amount(self):
        """Gets the amount of this ActionSubset.  # noqa: E501

        The amount being charged. It needs to be specified in cents and is an integer (9.99$ -> 999).  # noqa: E501

        :return: The amount of this ActionSubset.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ActionSubset.

        The amount being charged. It needs to be specified in cents and is an integer (9.99$ -> 999).  # noqa: E501

        :param amount: The amount of this ActionSubset.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this ActionSubset.  # noqa: E501

        An ISO 4217 standard currency code in lowercase. Used for actions of type buy.  # noqa: E501

        :return: The currency of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ActionSubset.

        An ISO 4217 standard currency code in lowercase. Used for actions of type buy.  # noqa: E501

        :param currency: The currency of this ActionSubset.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def metadata(self):
        """Gets the metadata of this ActionSubset.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this ActionSubset.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ActionSubset.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this ActionSubset.  # noqa: E501
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

    @property
    def uri(self):
        """Gets the uri of this ActionSubset.  # noqa: E501

        The webview URI. This is the URI that will open in the webview when clicking the button.  # noqa: E501

        :return: The uri of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ActionSubset.

        The webview URI. This is the URI that will open in the webview when clicking the button.  # noqa: E501

        :param uri: The uri of this ActionSubset.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def default(self):
        """Gets the default of this ActionSubset.  # noqa: E501

        Boolean value indicating whether the action is the default action for a message item in Facebook Messenger.  # noqa: E501

        :return: The default of this ActionSubset.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ActionSubset.

        Boolean value indicating whether the action is the default action for a message item in Facebook Messenger.  # noqa: E501

        :param default: The default of this ActionSubset.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def extra_channel_options(self):
        """Gets the extra_channel_options of this ActionSubset.  # noqa: E501


        :return: The extra_channel_options of this ActionSubset.  # noqa: E501
        :rtype: ExtraChannelOptions
        """
        return self._extra_channel_options

    @extra_channel_options.setter
    def extra_channel_options(self, extra_channel_options):
        """Sets the extra_channel_options of this ActionSubset.


        :param extra_channel_options: The extra_channel_options of this ActionSubset.  # noqa: E501
        :type: ExtraChannelOptions
        """

        self._extra_channel_options = extra_channel_options

    @property
    def payload(self):
        """Gets the payload of this ActionSubset.  # noqa: E501

        The payload of a postback or reply button.  # noqa: E501

        :return: The payload of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ActionSubset.

        The payload of a postback or reply button.  # noqa: E501

        :param payload: The payload of this ActionSubset.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def size(self):
        """Gets the size of this ActionSubset.  # noqa: E501

        The size to display a webview. Used for actions of type webview.  # noqa: E501

        :return: The size of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ActionSubset.

        The size to display a webview. Used for actions of type webview.  # noqa: E501

        :param size: The size of this ActionSubset.  # noqa: E501
        :type: str
        """
        allowed_values = ["compact", "tall", "full"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

        self._size = size

    @property
    def fallback(self):
        """Gets the fallback of this ActionSubset.  # noqa: E501

        The fallback uri for channels that don’t support webviews. Used for actions of type webview.  # noqa: E501

        :return: The fallback of this ActionSubset.  # noqa: E501
        :rtype: str
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """Sets the fallback of this ActionSubset.

        The fallback uri for channels that don’t support webviews. Used for actions of type webview.  # noqa: E501

        :param fallback: The fallback of this ActionSubset.  # noqa: E501
        :type: str
        """

        self._fallback = fallback

    @property
    def open_on_receive(self):
        """Gets the open_on_receive of this ActionSubset.  # noqa: E501

        Boolean value indicating if the webview should open automatically. Only one action per message can be set to true. Currently only supported on the Web Messenger.  # noqa: E501

        :return: The open_on_receive of this ActionSubset.  # noqa: E501
        :rtype: bool
        """
        return self._open_on_receive

    @open_on_receive.setter
    def open_on_receive(self, open_on_receive):
        """Sets the open_on_receive of this ActionSubset.

        Boolean value indicating if the webview should open automatically. Only one action per message can be set to true. Currently only supported on the Web Messenger.  # noqa: E501

        :param open_on_receive: The open_on_receive of this ActionSubset.  # noqa: E501
        :type: bool
        """

        self._open_on_receive = open_on_receive

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
        if not isinstance(other, ActionSubset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionSubset):
            return True

        return self.to_dict() != other.to_dict()
