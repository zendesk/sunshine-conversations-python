# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class WhatsappAllOf(object):
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
        'deployment_id': 'str',
        'hsm_fallback_language': 'str',
        'account_id': 'str',
        'account_management_access_token': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'deployment_id': 'deploymentId',
        'hsm_fallback_language': 'hsmFallbackLanguage',
        'account_id': 'accountId',
        'account_management_access_token': 'accountManagementAccessToken',
        'phone_number': 'phoneNumber'
    }

    nulls = set()

    def __init__(self, type='whatsapp', deployment_id=None, hsm_fallback_language='en_US', account_id=Undefined(), account_management_access_token=Undefined(), phone_number=Undefined(), local_vars_configuration=None):  # noqa: E501
        """WhatsappAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._deployment_id = None
        self._hsm_fallback_language = None
        self._account_id = None
        self._account_management_access_token = None
        self._phone_number = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.deployment_id = deployment_id
        self.hsm_fallback_language = hsm_fallback_language
        self.account_id = account_id
        self.account_management_access_token = account_management_access_token
        self.phone_number = phone_number

    @property
    def type(self):
        """Gets the type of this WhatsappAllOf.  # noqa: E501

        To configure a WhatsApp integration, use your WhatsApp API Client connection information. Sunshine Conversations can provide WhatsApp API Client hosting for approved brands. See our [WhatsApp guide](https://docs.smooch.io/guide/whatsapp/#whatsapp-api-client) for more details on WhatsApp API Client hosting.   # noqa: E501

        :return: The type of this WhatsappAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WhatsappAllOf.

        To configure a WhatsApp integration, use your WhatsApp API Client connection information. Sunshine Conversations can provide WhatsApp API Client hosting for approved brands. See our [WhatsApp guide](https://docs.smooch.io/guide/whatsapp/#whatsapp-api-client) for more details on WhatsApp API Client hosting.   # noqa: E501

        :param type: The type of this WhatsappAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def deployment_id(self):
        """Gets the deployment_id of this WhatsappAllOf.  # noqa: E501

        The Id of the deployment. The integrationId and the appId will be added to the deployment. Additionally, the deployment’s status will be set to integrated.  # noqa: E501

        :return: The deployment_id of this WhatsappAllOf.  # noqa: E501
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this WhatsappAllOf.

        The Id of the deployment. The integrationId and the appId will be added to the deployment. Additionally, the deployment’s status will be set to integrated.  # noqa: E501

        :param deployment_id: The deployment_id of this WhatsappAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and deployment_id is None:  # noqa: E501
            raise ValueError("Invalid value for `deployment_id`, must not be `None`")  # noqa: E501

        self._deployment_id = deployment_id

    @property
    def hsm_fallback_language(self):
        """Gets the hsm_fallback_language of this WhatsappAllOf.  # noqa: E501

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :return: The hsm_fallback_language of this WhatsappAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hsm_fallback_language

    @hsm_fallback_language.setter
    def hsm_fallback_language(self, hsm_fallback_language):
        """Sets the hsm_fallback_language of this WhatsappAllOf.

        Specify a fallback language to use when sending WhatsApp message template using the short hand syntax. Defaults to en_US. See WhatsApp documentation for more info.  # noqa: E501

        :param hsm_fallback_language: The hsm_fallback_language of this WhatsappAllOf.  # noqa: E501
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
        """Gets the account_id of this WhatsappAllOf.  # noqa: E501

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_id of this WhatsappAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this WhatsappAllOf.

        The business ID associated with the WhatsApp account. In combination with accountManagementAccessToken, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_id: The account_id of this WhatsappAllOf.  # noqa: E501
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
        """Gets the account_management_access_token of this WhatsappAllOf.  # noqa: E501

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :return: The account_management_access_token of this WhatsappAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_management_access_token

    @account_management_access_token.setter
    def account_management_access_token(self, account_management_access_token):
        """Sets the account_management_access_token of this WhatsappAllOf.

        An access token associated with the accountId used to query the WhatsApp Account Management API. In combination with accountId, it’s used for Message Template Reconstruction.  # noqa: E501

        :param account_management_access_token: The account_management_access_token of this WhatsappAllOf.  # noqa: E501
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
        """Gets the phone_number of this WhatsappAllOf.  # noqa: E501

        The phone number that is associated with the deployment of this integration, if one exists.  # noqa: E501

        :return: The phone_number of this WhatsappAllOf.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this WhatsappAllOf.

        The phone number that is associated with the deployment of this integration, if one exists.  # noqa: E501

        :param phone_number: The phone_number of this WhatsappAllOf.  # noqa: E501
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
        if not isinstance(other, WhatsappAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhatsappAllOf):
            return True

        return self.to_dict() != other.to_dict()
