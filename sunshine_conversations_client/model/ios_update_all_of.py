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


class IosUpdateAllOf(object):
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
        'certificate': 'str',
        'password': 'str',
        'production': 'bool',
        'auto_update_badge': 'bool',
        'can_user_create_more_conversations': 'bool'
    }

    attribute_map = {
        'certificate': 'certificate',
        'password': 'password',
        'production': 'production',
        'auto_update_badge': 'autoUpdateBadge',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations'
    }

    nulls = set()

    def __init__(self, certificate=Undefined(), password=None, production=None, auto_update_badge=None, can_user_create_more_conversations=None, local_vars_configuration=None):  # noqa: E501
        """IosUpdateAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._certificate = None
        self._password = None
        self._production = None
        self._auto_update_badge = None
        self._can_user_create_more_conversations = None
        self.discriminator = None

        self.certificate = certificate
        if password is not None:
            self.password = password
        if production is not None:
            self.production = production
        if auto_update_badge is not None:
            self.auto_update_badge = auto_update_badge
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def certificate(self):
        """Gets the certificate of this IosUpdateAllOf.  # noqa: E501

        The binary of your APN certificate base64 encoded.  # noqa: E501

        :return: The certificate of this IosUpdateAllOf.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this IosUpdateAllOf.

        The binary of your APN certificate base64 encoded.  # noqa: E501

        :param certificate: The certificate of this IosUpdateAllOf.  # noqa: E501
        :type: str
        """
        if type(certificate) is Undefined:
            certificate = None
            self.nulls.discard("certificate")
        elif certificate is None:
            self.nulls.add("certificate")
        else:
            self.nulls.discard("certificate")
        if (self.local_vars_configuration.client_side_validation and
                certificate is not None and len(certificate) < 1):
            raise ValueError("Invalid value for `certificate`, length must be greater than or equal to `1`")  # noqa: E501

        self._certificate = certificate

    @property
    def password(self):
        """Gets the password of this IosUpdateAllOf.  # noqa: E501

        The password for your APN certificate.  # noqa: E501

        :return: The password of this IosUpdateAllOf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this IosUpdateAllOf.

        The password for your APN certificate.  # noqa: E501

        :param password: The password of this IosUpdateAllOf.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def production(self):
        """Gets the production of this IosUpdateAllOf.  # noqa: E501

        The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified.  # noqa: E501

        :return: The production of this IosUpdateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this IosUpdateAllOf.

        The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified.  # noqa: E501

        :param production: The production of this IosUpdateAllOf.  # noqa: E501
        :type: bool
        """

        self._production = production

    @property
    def auto_update_badge(self):
        """Gets the auto_update_badge of this IosUpdateAllOf.  # noqa: E501

        Use the unread count of the conversation as the application badge.  # noqa: E501

        :return: The auto_update_badge of this IosUpdateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._auto_update_badge

    @auto_update_badge.setter
    def auto_update_badge(self, auto_update_badge):
        """Sets the auto_update_badge of this IosUpdateAllOf.

        Use the unread count of the conversation as the application badge.  # noqa: E501

        :param auto_update_badge: The auto_update_badge of this IosUpdateAllOf.  # noqa: E501
        :type: bool
        """

        self._auto_update_badge = auto_update_badge

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this IosUpdateAllOf.  # noqa: E501

        Allows users to create more than one conversation on the iOS integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this IosUpdateAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this IosUpdateAllOf.

        Allows users to create more than one conversation on the iOS integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this IosUpdateAllOf.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

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
        if not isinstance(other, IosUpdateAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IosUpdateAllOf):
            return True

        return self.to_dict() != other.to_dict()
