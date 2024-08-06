# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.7.0
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

class Mailgun(Integration):
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
        'api_key': 'str',
        'domain': 'str',
        'incoming_address': 'str',
        'hide_unsubscribe_link': 'bool',
        'from_address': 'str',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'api_key': 'apiKey',
        'domain': 'domain',
        'incoming_address': 'incomingAddress',
        'hide_unsubscribe_link': 'hideUnsubscribeLink',
        'from_address': 'fromAddress',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='mailgun', api_key=None, domain=None, incoming_address=None, hide_unsubscribe_link=None, from_address=Undefined(), default_responder_id=Undefined(), default_responder=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """Mailgun - a model defined in OpenAPI"""  # noqa: E501
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
        self._api_key = None
        self._domain = None
        self._incoming_address = None
        self._hide_unsubscribe_link = None
        self._from_address = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if api_key is not None:
            self.api_key = api_key
        self.domain = domain
        self.incoming_address = incoming_address
        if hide_unsubscribe_link is not None:
            self.hide_unsubscribe_link = hide_unsubscribe_link
        self.from_address = from_address
        self.default_responder_id = default_responder_id
        if default_responder is not None:
            self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Mailgun.  # noqa: E501

        To configure a Mailgun integration, visit the API Keys tab in the settings page of the Mailgun dashboard and copy your active API key. Call the Create Integration endpoint with your API Key, a domain you have configured in Mailgun, and the incoming address you would like to use. Must have the same domain as the one specified in the domain parameter.   # noqa: E501

        :return: The type of this Mailgun.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Mailgun.

        To configure a Mailgun integration, visit the API Keys tab in the settings page of the Mailgun dashboard and copy your active API key. Call the Create Integration endpoint with your API Key, a domain you have configured in Mailgun, and the incoming address you would like to use. Must have the same domain as the one specified in the domain parameter.   # noqa: E501

        :param type: The type of this Mailgun.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def api_key(self):
        """Gets the api_key of this Mailgun.  # noqa: E501

        The public API key of your Mailgun account.  # noqa: E501

        :return: The api_key of this Mailgun.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Mailgun.

        The public API key of your Mailgun account.  # noqa: E501

        :param api_key: The api_key of this Mailgun.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_key is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_key is not None and len(api_key) < 1):
            raise ValueError("Invalid value for `api_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._api_key = api_key

    @property
    def domain(self):
        """Gets the domain of this Mailgun.  # noqa: E501

        The domain used to relay email. This domain must be configured and verified in your Mailgun account.  # noqa: E501

        :return: The domain of this Mailgun.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Mailgun.

        The domain used to relay email. This domain must be configured and verified in your Mailgun account.  # noqa: E501

        :param domain: The domain of this Mailgun.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                domain is not None and len(domain) < 1):
            raise ValueError("Invalid value for `domain`, length must be greater than or equal to `1`")  # noqa: E501

        self._domain = domain

    @property
    def incoming_address(self):
        """Gets the incoming_address of this Mailgun.  # noqa: E501

        Sunshine Conversations will receive all emails sent to this address. It will also be used as the Reply-To address.  # noqa: E501

        :return: The incoming_address of this Mailgun.  # noqa: E501
        :rtype: str
        """
        return self._incoming_address

    @incoming_address.setter
    def incoming_address(self, incoming_address):
        """Sets the incoming_address of this Mailgun.

        Sunshine Conversations will receive all emails sent to this address. It will also be used as the Reply-To address.  # noqa: E501

        :param incoming_address: The incoming_address of this Mailgun.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and incoming_address is None:  # noqa: E501
            raise ValueError("Invalid value for `incoming_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                incoming_address is not None and len(incoming_address) < 1):
            raise ValueError("Invalid value for `incoming_address`, length must be greater than or equal to `1`")  # noqa: E501

        self._incoming_address = incoming_address

    @property
    def hide_unsubscribe_link(self):
        """Gets the hide_unsubscribe_link of this Mailgun.  # noqa: E501

        A boolean value indicating whether the unsubscribe link should be omitted from outgoing emails. When enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. By default, the unsubscribe link will be included in all outgoing emails.  # noqa: E501

        :return: The hide_unsubscribe_link of this Mailgun.  # noqa: E501
        :rtype: bool
        """
        return self._hide_unsubscribe_link

    @hide_unsubscribe_link.setter
    def hide_unsubscribe_link(self, hide_unsubscribe_link):
        """Sets the hide_unsubscribe_link of this Mailgun.

        A boolean value indicating whether the unsubscribe link should be omitted from outgoing emails. When enabled, it is expected that the business is providing the user a way to unsubscribe by some other means. By default, the unsubscribe link will be included in all outgoing emails.  # noqa: E501

        :param hide_unsubscribe_link: The hide_unsubscribe_link of this Mailgun.  # noqa: E501
        :type: bool
        """

        self._hide_unsubscribe_link = hide_unsubscribe_link

    @property
    def from_address(self):
        """Gets the from_address of this Mailgun.  # noqa: E501

        Email address to use as the From and Reply-To address if it must be different from incomingAddress. Only use this option if the address that you supply is configured to forward emails to the incomingAddress, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user’s email client. May be unset with null.  # noqa: E501

        :return: The from_address of this Mailgun.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this Mailgun.

        Email address to use as the From and Reply-To address if it must be different from incomingAddress. Only use this option if the address that you supply is configured to forward emails to the incomingAddress, otherwise user replies will be lost. You must also make sure that the domain is properly configured as a mail provider so as to not be flagged as spam by the user’s email client. May be unset with null.  # noqa: E501

        :param from_address: The from_address of this Mailgun.  # noqa: E501
        :type: str
        """
        if type(from_address) is Undefined:
            from_address = None
            self.nulls.discard("from_address")
        elif from_address is None:
            self.nulls.add("from_address")
        else:
            self.nulls.discard("from_address")
        if (self.local_vars_configuration.client_side_validation and
                from_address is not None and len(from_address) < 1):
            raise ValueError("Invalid value for `from_address`, length must be greater than or equal to `1`")  # noqa: E501

        self._from_address = from_address

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Mailgun.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this Mailgun.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Mailgun.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Mailgun.  # noqa: E501
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
        """Gets the default_responder of this Mailgun.  # noqa: E501


        :return: The default_responder of this Mailgun.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Mailgun.


        :param default_responder: The default_responder of this Mailgun.  # noqa: E501
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
        if not isinstance(other, Mailgun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Mailgun):
            return True

        return self.to_dict() != other.to_dict()
