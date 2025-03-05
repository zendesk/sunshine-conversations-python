# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Profile(object):
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
        'given_name': 'str',
        'surname': 'str',
        'email': 'str',
        'avatar_url': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'given_name': 'givenName',
        'surname': 'surname',
        'email': 'email',
        'avatar_url': 'avatarUrl',
        'locale': 'locale'
    }

    nulls = set()

    def __init__(self, given_name=Undefined(), surname=Undefined(), email=Undefined(), avatar_url=Undefined(), locale=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Profile - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._given_name = None
        self._surname = None
        self._email = None
        self._avatar_url = None
        self._locale = None
        self.discriminator = None

        self.given_name = given_name
        self.surname = surname
        self.email = email
        self.avatar_url = avatar_url
        self.locale = locale

    @property
    def given_name(self):
        """Gets the given_name of this Profile.  # noqa: E501

        The user's given name (first name).  # noqa: E501

        :return: The given_name of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this Profile.

        The user's given name (first name).  # noqa: E501

        :param given_name: The given_name of this Profile.  # noqa: E501
        :type: str
        """
        if type(given_name) is Undefined:
            given_name = None
            self.nulls.discard("given_name")
        elif given_name is None:
            self.nulls.add("given_name")
        else:
            self.nulls.discard("given_name")
        if (self.local_vars_configuration.client_side_validation and
                given_name is not None and len(given_name) > 128):
            raise ValueError("Invalid value for `given_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                given_name is not None and len(given_name) < 1):
            raise ValueError("Invalid value for `given_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._given_name = given_name

    @property
    def surname(self):
        """Gets the surname of this Profile.  # noqa: E501

        The user's surname (last name).  # noqa: E501

        :return: The surname of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this Profile.

        The user's surname (last name).  # noqa: E501

        :param surname: The surname of this Profile.  # noqa: E501
        :type: str
        """
        if type(surname) is Undefined:
            surname = None
            self.nulls.discard("surname")
        elif surname is None:
            self.nulls.add("surname")
        else:
            self.nulls.discard("surname")
        if (self.local_vars_configuration.client_side_validation and
                surname is not None and len(surname) > 128):
            raise ValueError("Invalid value for `surname`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                surname is not None and len(surname) < 1):
            raise ValueError("Invalid value for `surname`, length must be greater than or equal to `1`")  # noqa: E501

        self._surname = surname

    @property
    def email(self):
        """Gets the email of this Profile.  # noqa: E501

        The user's email address.  # noqa: E501

        :return: The email of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Profile.

        The user's email address.  # noqa: E501

        :param email: The email of this Profile.  # noqa: E501
        :type: str
        """
        if type(email) is Undefined:
            email = None
            self.nulls.discard("email")
        elif email is None:
            self.nulls.add("email")
        else:
            self.nulls.discard("email")
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 128):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Profile.  # noqa: E501

        The user's avatar.  # noqa: E501

        :return: The avatar_url of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Profile.

        The user's avatar.  # noqa: E501

        :param avatar_url: The avatar_url of this Profile.  # noqa: E501
        :type: str
        """
        if type(avatar_url) is Undefined:
            avatar_url = None
            self.nulls.discard("avatar_url")
        elif avatar_url is None:
            self.nulls.add("avatar_url")
        else:
            self.nulls.discard("avatar_url")
        if (self.local_vars_configuration.client_side_validation and
                avatar_url is not None and len(avatar_url) > 2048):
            raise ValueError("Invalid value for `avatar_url`, length must be less than or equal to `2048`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                avatar_url is not None and len(avatar_url) < 1):
            raise ValueError("Invalid value for `avatar_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._avatar_url = avatar_url

    @property
    def locale(self):
        """Gets the locale of this Profile.  # noqa: E501

        End-user's locale information in BCP 47 format.  # noqa: E501

        :return: The locale of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Profile.

        End-user's locale information in BCP 47 format.  # noqa: E501

        :param locale: The locale of this Profile.  # noqa: E501
        :type: str
        """
        if type(locale) is Undefined:
            locale = None
            self.nulls.discard("locale")
        elif locale is None:
            self.nulls.add("locale")
        else:
            self.nulls.discard("locale")
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and len(locale) > 64):
            raise ValueError("Invalid value for `locale`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and len(locale) < 1):
            raise ValueError("Invalid value for `locale`, length must be greater than or equal to `1`")  # noqa: E501

        self._locale = locale

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
        if not isinstance(other, Profile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Profile):
            return True

        return self.to_dict() != other.to_dict()
