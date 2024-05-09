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


class Author(object):
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
        'subtypes': 'list[str]',
        'user_id': 'str',
        'user_external_id': 'str',
        'display_name': 'str',
        'avatar_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'subtypes': 'subtypes',
        'user_id': 'userId',
        'user_external_id': 'userExternalId',
        'display_name': 'displayName',
        'avatar_url': 'avatarUrl'
    }

    nulls = set()

    def __init__(self, type=None, subtypes=None, user_id=None, user_external_id=None, display_name=None, avatar_url=None, local_vars_configuration=None):  # noqa: E501
        """Author - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._subtypes = None
        self._user_id = None
        self._user_external_id = None
        self._display_name = None
        self._avatar_url = None
        self.discriminator = None

        self.type = type
        if subtypes is not None:
            self.subtypes = subtypes
        if user_id is not None:
            self.user_id = user_id
        if user_external_id is not None:
            self.user_external_id = user_external_id
        if display_name is not None:
            self.display_name = display_name
        if avatar_url is not None:
            self.avatar_url = avatar_url

    @property
    def type(self):
        """Gets the type of this Author.  # noqa: E501

        The author type. Either \"user\" (representing the end user)  or \"business\" (sent on behalf of the business).   # noqa: E501

        :return: The type of this Author.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Author.

        The author type. Either \"user\" (representing the end user)  or \"business\" (sent on behalf of the business).   # noqa: E501

        :param type: The type of this Author.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["business", "user"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subtypes(self):
        """Gets the subtypes of this Author.  # noqa: E501

        A string array that indicates the author's subtypes. Messages from \"business\" type with an \"AI\" subtype  are generated by AI and a disclaimer is appended to the text of the message sent to the customer.  For third-party channels, the disclaimer is applied for image, file, and text message types.   # noqa: E501

        :return: The subtypes of this Author.  # noqa: E501
        :rtype: list[str]
        """
        return self._subtypes

    @subtypes.setter
    def subtypes(self, subtypes):
        """Sets the subtypes of this Author.

        A string array that indicates the author's subtypes. Messages from \"business\" type with an \"AI\" subtype  are generated by AI and a disclaimer is appended to the text of the message sent to the customer.  For third-party channels, the disclaimer is applied for image, file, and text message types.   # noqa: E501

        :param subtypes: The subtypes of this Author.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AI"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(subtypes).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `subtypes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(subtypes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._subtypes = subtypes

    @property
    def user_id(self):
        """Gets the user_id of this Author.  # noqa: E501

        The id of the user. Only supported when `type` is user.  # noqa: E501

        :return: The user_id of this Author.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Author.

        The id of the user. Only supported when `type` is user.  # noqa: E501

        :param user_id: The user_id of this Author.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_external_id(self):
        """Gets the user_external_id of this Author.  # noqa: E501

        The externalId of the user. Only supported when `type` is user.  # noqa: E501

        :return: The user_external_id of this Author.  # noqa: E501
        :rtype: str
        """
        return self._user_external_id

    @user_external_id.setter
    def user_external_id(self, user_external_id):
        """Sets the user_external_id of this Author.

        The externalId of the user. Only supported when `type` is user.  # noqa: E501

        :param user_external_id: The user_external_id of this Author.  # noqa: E501
        :type: str
        """

        self._user_external_id = user_external_id

    @property
    def display_name(self):
        """Gets the display_name of this Author.  # noqa: E501

        The display name of the message author.  # noqa: E501

        :return: The display_name of this Author.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Author.

        The display name of the message author.  # noqa: E501

        :param display_name: The display_name of this Author.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Author.  # noqa: E501

        A custom message icon URL. The image must be JPG, PNG, or GIF format.  # noqa: E501

        :return: The avatar_url of this Author.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Author.

        A custom message icon URL. The image must be JPG, PNG, or GIF format.  # noqa: E501

        :param avatar_url: The avatar_url of this Author.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

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
        if not isinstance(other, Author):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Author):
            return True

        return self.to_dict() != other.to_dict()
