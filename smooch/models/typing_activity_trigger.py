# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TypingActivityTrigger(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, role=None, type=None, name=None, avatar_url=None):
        """
        TypingActivityTrigger - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'role': 'str',
            'type': 'str',
            'name': 'str',
            'avatar_url': 'str'
        }

        self.attribute_map = {
            'role': 'role',
            'type': 'type',
            'name': 'name',
            'avatar_url': 'avatarUrl'
        }

        self._role = role
        self._type = type
        self._name = name
        self._avatar_url = avatar_url

    @property
    def role(self):
        """
        Gets the role of this TypingActivityTrigger.
        The role of the actor. Must be *appMaker*.

        :return: The role of this TypingActivityTrigger.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this TypingActivityTrigger.
        The role of the actor. Must be *appMaker*.

        :param role: The role of this TypingActivityTrigger.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def type(self):
        """
        Gets the type of this TypingActivityTrigger.
        The type of activity to trigger. Must be either *typing:start* or *typing:stop*.

        :return: The type of this TypingActivityTrigger.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TypingActivityTrigger.
        The type of activity to trigger. Must be either *typing:start* or *typing:stop*.

        :param type: The type of this TypingActivityTrigger.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this TypingActivityTrigger.
        The name of the app maker that starts or stops typing a response.

        :return: The name of this TypingActivityTrigger.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TypingActivityTrigger.
        The name of the app maker that starts or stops typing a response.

        :param name: The name of this TypingActivityTrigger.
        :type: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this TypingActivityTrigger.
        The avatar URL of the app maker that starts typing a response.

        :return: The avatar_url of this TypingActivityTrigger.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this TypingActivityTrigger.
        The avatar URL of the app maker that starts typing a response.

        :param avatar_url: The avatar_url of this TypingActivityTrigger.
        :type: str
        """

        self._avatar_url = avatar_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TypingActivityTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
