# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined

try:
    Integration = __import__("sunshine_conversations_client.model."+re.sub(r'(?<!^)(?=[A-Z])', '_', "Integration").lower(), fromlist=("Integration")).Integration
except ImportError:
    pass

class Line(Integration):
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
        'channel_id': 'str',
        'channel_secret': 'str',
        'channel_access_token': 'str',
        'service_code': 'str',
        'switcher_secret': 'str',
        'qr_code_url': 'str',
        'line_id': 'str',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'channel_id': 'channelId',
        'channel_secret': 'channelSecret',
        'channel_access_token': 'channelAccessToken',
        'service_code': 'serviceCode',
        'switcher_secret': 'switcherSecret',
        'qr_code_url': 'qrCodeUrl',
        'line_id': 'lineId',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='line', channel_id=None, channel_secret=None, channel_access_token=None, service_code=None, switcher_secret=None, qr_code_url=None, line_id=None, default_responder_id=Undefined(), default_responder=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """Line - a model defined in OpenAPI"""  # noqa: E501
        super().__init__(**kwargs)

        if (super().openapi_types is not None):
            all_types = super().openapi_types.copy()
            all_types.update(self.openapi_types)
            self.openapi_types = all_types

        if (super().attribute_map is not None):
            all_attributes = super().attribute_map.copy()
            all_attributes.update(self.attribute_map)
            self.attribute_map = all_attributes
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._channel_id = None
        self._channel_secret = None
        self._channel_access_token = None
        self._service_code = None
        self._switcher_secret = None
        self._qr_code_url = None
        self._line_id = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_secret is not None:
            self.channel_secret = channel_secret
        if channel_access_token is not None:
            self.channel_access_token = channel_access_token
        if service_code is not None:
            self.service_code = service_code
        if switcher_secret is not None:
            self.switcher_secret = switcher_secret
        if qr_code_url is not None:
            self.qr_code_url = qr_code_url
        if line_id is not None:
            self.line_id = line_id
        self.default_responder_id = default_responder_id
        if default_responder is not None:
            self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Line.  # noqa: E501

        For LINE, each of your customers will need to manually configure a webhook in their LINE configuration page that will point to Sunshine Conversations servers. You must instruct your customers how to configure this manually on their LINE bot page. Once you’ve acquired all the required information, call the Create Integration endpoint. Then, using the returned integration _id, your customer must set the Callback URL field in their LINE Business Center page. The URL should look like the following: `https://app.smooch.io:443/api/line/webhooks/{appId}/{integrationId}`.   # noqa: E501

        :return: The type of this Line.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Line.

        For LINE, each of your customers will need to manually configure a webhook in their LINE configuration page that will point to Sunshine Conversations servers. You must instruct your customers how to configure this manually on their LINE bot page. Once you’ve acquired all the required information, call the Create Integration endpoint. Then, using the returned integration _id, your customer must set the Callback URL field in their LINE Business Center page. The URL should look like the following: `https://app.smooch.io:443/api/line/webhooks/{appId}/{integrationId}`.   # noqa: E501

        :param type: The type of this Line.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def channel_id(self):
        """Gets the channel_id of this Line.  # noqa: E501

        LINE Channel ID. Can be omitted along with `channelSecret` to integrate LINE to setup a webhook before receiving the `channelId` and `channelSecret` back from LINE.  # noqa: E501

        :return: The channel_id of this Line.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this Line.

        LINE Channel ID. Can be omitted along with `channelSecret` to integrate LINE to setup a webhook before receiving the `channelId` and `channelSecret` back from LINE.  # noqa: E501

        :param channel_id: The channel_id of this Line.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

    @property
    def channel_secret(self):
        """Gets the channel_secret of this Line.  # noqa: E501

        LINE Channel Secret. Can be omitted along with `channelId` to integrate LINE to setup a webhook before receiving the `channelId` and `channelSecret` back from LINE.  # noqa: E501

        :return: The channel_secret of this Line.  # noqa: E501
        :rtype: str
        """
        return self._channel_secret

    @channel_secret.setter
    def channel_secret(self, channel_secret):
        """Sets the channel_secret of this Line.

        LINE Channel Secret. Can be omitted along with `channelId` to integrate LINE to setup a webhook before receiving the `channelId` and `channelSecret` back from LINE.  # noqa: E501

        :param channel_secret: The channel_secret of this Line.  # noqa: E501
        :type: str
        """

        self._channel_secret = channel_secret

    @property
    def channel_access_token(self):
        """Gets the channel_access_token of this Line.  # noqa: E501

        LINE Channel Access Token.  # noqa: E501

        :return: The channel_access_token of this Line.  # noqa: E501
        :rtype: str
        """
        return self._channel_access_token

    @channel_access_token.setter
    def channel_access_token(self, channel_access_token):
        """Sets the channel_access_token of this Line.

        LINE Channel Access Token.  # noqa: E501

        :param channel_access_token: The channel_access_token of this Line.  # noqa: E501
        :type: str
        """

        self._channel_access_token = channel_access_token

    @property
    def service_code(self):
        """Gets the service_code of this Line.  # noqa: E501

        LINE Service Code.  # noqa: E501

        :return: The service_code of this Line.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this Line.

        LINE Service Code.  # noqa: E501

        :param service_code: The service_code of this Line.  # noqa: E501
        :type: str
        """

        self._service_code = service_code

    @property
    def switcher_secret(self):
        """Gets the switcher_secret of this Line.  # noqa: E501

        LINE Switcher Secret.  # noqa: E501

        :return: The switcher_secret of this Line.  # noqa: E501
        :rtype: str
        """
        return self._switcher_secret

    @switcher_secret.setter
    def switcher_secret(self, switcher_secret):
        """Sets the switcher_secret of this Line.

        LINE Switcher Secret.  # noqa: E501

        :param switcher_secret: The switcher_secret of this Line.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                switcher_secret is not None and len(switcher_secret) < 1):
            raise ValueError("Invalid value for `switcher_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._switcher_secret = switcher_secret

    @property
    def qr_code_url(self):
        """Gets the qr_code_url of this Line.  # noqa: E501

        URL provided by LINE in the [Developer Console](https://developers.line.biz/console/).  # noqa: E501

        :return: The qr_code_url of this Line.  # noqa: E501
        :rtype: str
        """
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, qr_code_url):
        """Sets the qr_code_url of this Line.

        URL provided by LINE in the [Developer Console](https://developers.line.biz/console/).  # noqa: E501

        :param qr_code_url: The qr_code_url of this Line.  # noqa: E501
        :type: str
        """

        self._qr_code_url = qr_code_url

    @property
    def line_id(self):
        """Gets the line_id of this Line.  # noqa: E501

        LINE Basic ID. Is automatically set when qrCodeUrl is updated.  # noqa: E501

        :return: The line_id of this Line.  # noqa: E501
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this Line.

        LINE Basic ID. Is automatically set when qrCodeUrl is updated.  # noqa: E501

        :param line_id: The line_id of this Line.  # noqa: E501
        :type: str
        """

        self._line_id = line_id

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Line.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this Line.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Line.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Line.  # noqa: E501
        :type: str
        """
        if type(default_responder_id) is Undefined:
            default_responder_id = None
            self.nulls.discard("default_responder_id")
        elif default_responder_id is None:
            self.nulls.add("default_responder_id")
        else:
            self.nulls.discard("default_responder_id")

        self._default_responder_id = default_responder_id

    @property
    def default_responder(self):
        """Gets the default_responder of this Line.  # noqa: E501


        :return: The default_responder of this Line.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Line.


        :param default_responder: The default_responder of this Line.  # noqa: E501
        :type: DefaultResponderDefaultResponder
        """

        self._default_responder = default_responder

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
        if not isinstance(other, Line):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Line):
            return True

        return self.to_dict() != other.to_dict()
