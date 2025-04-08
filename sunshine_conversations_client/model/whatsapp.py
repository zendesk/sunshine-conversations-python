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

try:
    Integration = __import__("sunshine_conversations_client.model."+re.sub(r'(?<!^)(?=[A-Z])', '_', "Integration").lower(), fromlist=("Integration")).Integration
except ImportError:
    pass

class Whatsapp(Integration):
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
        'hsm_fallback_language': 'str',
        'account_id': 'str',
        'account_management_access_token': 'str',
        'phone_number': 'str',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'hsm_fallback_language': 'hsmFallbackLanguage',
        'account_id': 'accountId',
        'account_management_access_token': 'accountManagementAccessToken',
        'phone_number': 'phoneNumber',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='whatsapp', hsm_fallback_language='en_US', account_id=Undefined(), account_management_access_token=Undefined(), phone_number=Undefined(), default_responder_id=Undefined(), default_responder=Undefined(), local_vars_configuration=None, **kwargs):  # noqa: E501
        """Whatsapp - a model defined in OpenAPI"""  # noqa: E501
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
        self._hsm_fallback_language = None
        self._account_id = None
        self._account_management_access_token = None
        self._phone_number = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.hsm_fallback_language = hsm_fallback_language
        self.account_id = account_id
        self.account_management_access_token = account_management_access_token
        self.phone_number = phone_number
        self.default_responder_id = default_responder_id
        self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Whatsapp.  # noqa: E501

        To configure a WhatsApp integration, use your WhatsApp API Client connection information. Sunshine Conversations can provide WhatsApp API Client hosting for approved brands. See our [WhatsApp guide](https://docs.smooch.io/guide/whatsapp/#whatsapp-api-client) for more details on WhatsApp API Client hosting.   # noqa: E501

        :return: The type of this Whatsapp.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Whatsapp.

        To configure a WhatsApp integration, use your WhatsApp API Client connection information. Sunshine Conversations can provide WhatsApp API Client hosting for approved brands. See our [WhatsApp guide](https://docs.smooch.io/guide/whatsapp/#whatsapp-api-client) for more details on WhatsApp API Client hosting.   # noqa: E501

        :param type: The type of this Whatsapp.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def hsm_fallback_language(self):
        """Gets the hsm_fallback_language of this Whatsapp.  # noqa: E501

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :return: The hsm_fallback_language of this Whatsapp.  # noqa: E501
        :rtype: str
        """
        return self._hsm_fallback_language

    @hsm_fallback_language.setter
    def hsm_fallback_language(self, hsm_fallback_language):
        """Sets the hsm_fallback_language of this Whatsapp.

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :param hsm_fallback_language: The hsm_fallback_language of this Whatsapp.  # noqa: E501
        :type: str
        """
        if type(hsm_fallback_language) is Undefined:
            hsm_fallback_language = None
            self.nulls.discard("hsm_fallback_language")
        elif hsm_fallback_language is None:
            self.nulls.add("hsm_fallback_language")
        else:
            self.nulls.discard("hsm_fallback_language")

        self._hsm_fallback_language = hsm_fallback_language

    @property
    def account_id(self):
        """Gets the account_id of this Whatsapp.  # noqa: E501

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_id of this Whatsapp.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Whatsapp.

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_id: The account_id of this Whatsapp.  # noqa: E501
        :type: str
        """
        if type(account_id) is Undefined:
            account_id = None
            self.nulls.discard("account_id")
        elif account_id is None:
            self.nulls.add("account_id")
        else:
            self.nulls.discard("account_id")

        self._account_id = account_id

    @property
    def account_management_access_token(self):
        """Gets the account_management_access_token of this Whatsapp.  # noqa: E501

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_management_access_token of this Whatsapp.  # noqa: E501
        :rtype: str
        """
        return self._account_management_access_token

    @account_management_access_token.setter
    def account_management_access_token(self, account_management_access_token):
        """Sets the account_management_access_token of this Whatsapp.

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_management_access_token: The account_management_access_token of this Whatsapp.  # noqa: E501
        :type: str
        """
        if type(account_management_access_token) is Undefined:
            account_management_access_token = None
            self.nulls.discard("account_management_access_token")
        elif account_management_access_token is None:
            self.nulls.add("account_management_access_token")
        else:
            self.nulls.discard("account_management_access_token")

        self._account_management_access_token = account_management_access_token

    @property
    def phone_number(self):
        """Gets the phone_number of this Whatsapp.  # noqa: E501

        The phone number that is associated with the deployment of this integration, if one exists.  # noqa: E501

        :return: The phone_number of this Whatsapp.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Whatsapp.

        The phone number that is associated with the deployment of this integration, if one exists.  # noqa: E501

        :param phone_number: The phone_number of this Whatsapp.  # noqa: E501
        :type: str
        """
        if type(phone_number) is Undefined:
            phone_number = None
            self.nulls.discard("phone_number")
        elif phone_number is None:
            self.nulls.add("phone_number")
        else:
            self.nulls.discard("phone_number")

        self._phone_number = phone_number

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Whatsapp.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this Whatsapp.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Whatsapp.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Whatsapp.  # noqa: E501
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
        """Gets the default_responder of this Whatsapp.  # noqa: E501


        :return: The default_responder of this Whatsapp.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Whatsapp.


        :param default_responder: The default_responder of this Whatsapp.  # noqa: E501
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
        if not isinstance(other, Whatsapp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Whatsapp):
            return True

        return self.to_dict() != other.to_dict()
