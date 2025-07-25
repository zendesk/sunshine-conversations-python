# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.5.2
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

class Twilio(Integration):
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
        'account_sid': 'str',
        'auth_token': 'str',
        'phone_number_sid': 'str',
        'messaging_service_sid': 'str',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'account_sid': 'accountSid',
        'auth_token': 'authToken',
        'phone_number_sid': 'phoneNumberSid',
        'messaging_service_sid': 'messagingServiceSid',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='twilio', account_sid=None, auth_token=Undefined(), phone_number_sid=None, messaging_service_sid=None, default_responder_id=Undefined(), default_responder=Undefined(), local_vars_configuration=None, **kwargs):  # noqa: E501
        """Twilio - a model defined in OpenAPI"""  # noqa: E501
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
        self._account_sid = None
        self._auth_token = None
        self._phone_number_sid = None
        self._messaging_service_sid = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.account_sid = account_sid
        if auth_token is not None:
            self.auth_token = auth_token
        if phone_number_sid is not None:
            self.phone_number_sid = phone_number_sid
        if messaging_service_sid is not None:
            self.messaging_service_sid = messaging_service_sid
        self.default_responder_id = default_responder_id
        self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Twilio.  # noqa: E501

        To configure a Twilio integration, acquire the required information from the user and call the Create Integration endpoint.   # noqa: E501

        :return: The type of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Twilio.

        To configure a Twilio integration, acquire the required information from the user and call the Create Integration endpoint.   # noqa: E501

        :param type: The type of this Twilio.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def account_sid(self):
        """Gets the account_sid of this Twilio.  # noqa: E501

        Twilio Account SID.  # noqa: E501

        :return: The account_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """Sets the account_sid of this Twilio.

        Twilio Account SID.  # noqa: E501

        :param account_sid: The account_sid of this Twilio.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_sid is None:  # noqa: E501
            raise ValueError("Invalid value for `account_sid`, must not be `None`")  # noqa: E501

        self._account_sid = account_sid

    @property
    def auth_token(self):
        """Gets the auth_token of this Twilio.  # noqa: E501

        Twilio Auth Token.  # noqa: E501

        :return: The auth_token of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this Twilio.

        Twilio Auth Token.  # noqa: E501

        :param auth_token: The auth_token of this Twilio.  # noqa: E501
        :type: str
        """
        if type(auth_token) is Undefined:
            auth_token = None
            self.nulls.discard("auth_token")
        elif auth_token is None:
            self.nulls.add("auth_token")
        else:
            self.nulls.discard("auth_token")
        if (self.local_vars_configuration.client_side_validation and
                auth_token is not None and len(auth_token) < 1):
            raise ValueError("Invalid value for `auth_token`, length must be greater than or equal to `1`")  # noqa: E501

        self._auth_token = auth_token

    @property
    def phone_number_sid(self):
        """Gets the phone_number_sid of this Twilio.  # noqa: E501

        SID for specific phone number. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :return: The phone_number_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_sid

    @phone_number_sid.setter
    def phone_number_sid(self, phone_number_sid):
        """Sets the phone_number_sid of this Twilio.

        SID for specific phone number. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :param phone_number_sid: The phone_number_sid of this Twilio.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone_number_sid is not None and len(phone_number_sid) < 1):
            raise ValueError("Invalid value for `phone_number_sid`, length must be greater than or equal to `1`")  # noqa: E501

        self._phone_number_sid = phone_number_sid

    @property
    def messaging_service_sid(self):
        """Gets the messaging_service_sid of this Twilio.  # noqa: E501

        SID for specific messaging service. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :return: The messaging_service_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._messaging_service_sid

    @messaging_service_sid.setter
    def messaging_service_sid(self, messaging_service_sid):
        """Sets the messaging_service_sid of this Twilio.

        SID for specific messaging service. One of `messagingServiceSid` or `phoneNumberSid` must be provided when creating a Twilio integration.  # noqa: E501

        :param messaging_service_sid: The messaging_service_sid of this Twilio.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                messaging_service_sid is not None and len(messaging_service_sid) < 1):
            raise ValueError("Invalid value for `messaging_service_sid`, length must be greater than or equal to `1`")  # noqa: E501

        self._messaging_service_sid = messaging_service_sid

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Twilio.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the <a href=\"https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\">Switchboard guide</a>.   # noqa: E501

        :return: The default_responder_id of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Twilio.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to the <a href=\"https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#default-integration-assignment\">Switchboard guide</a>.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Twilio.  # noqa: E501
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
        """Gets the default_responder of this Twilio.  # noqa: E501


        :return: The default_responder of this Twilio.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Twilio.


        :param default_responder: The default_responder of this Twilio.  # noqa: E501
        :type: DefaultResponderDefaultResponder
        """
        if type(default_responder) is Undefined:
            default_responder = None
            self.nulls.discard("default_responder")
        elif default_responder is None:
            self.nulls.add("default_responder")
        else:
            self.nulls.discard("default_responder")

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
        if not isinstance(other, Twilio):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Twilio):
            return True

        return self.to_dict() != other.to_dict()
