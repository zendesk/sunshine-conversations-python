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


class Integration(object):
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
        'id': 'str',
        'type': 'str',
        'status': 'Status',
        'display_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'display_name': 'displayName'
    }

    nulls = set()

    discriminator_value_class_map = {
        'line': 'Line',
        'viber': 'Viber',
        'messagebird': 'Messagebird',
        'whatsapp': 'Whatsapp',
        'instagram': 'Instagram',
        'twilio': 'Twilio',
        'mailgun': 'Mailgun',
        'twitter': 'Twitter',
        'apple': 'Apple',
        'messenger': 'Messenger',
        'web': 'Web',
        'custom': 'Custom',
        'android': 'Android',
        'unity': 'Unity',
        'telegram': 'Telegram',
        'ios': 'Ios'
    }

    def __init__(self, id=None, type=None, status=None, display_name=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Integration - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._status = None
        self._display_name = None
        self.discriminator = 'type'

        if id is not None:
            self.id = id
        self.type = type
        if status is not None:
            self.status = status
        self.display_name = display_name

    @property
    def id(self):
        """Gets the id of this Integration.  # noqa: E501

        The unique ID of the integration.  # noqa: E501

        :return: The id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Integration.

        The unique ID of the integration.  # noqa: E501

        :param id: The id of this Integration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Integration.  # noqa: E501


        :return: The type of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Integration.


        :param type: The type of this Integration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this Integration.  # noqa: E501


        :return: The status of this Integration.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Integration.


        :param status: The status of this Integration.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def display_name(self):
        """Gets the display_name of this Integration.  # noqa: E501

        A human-friendly name used to identify the integration.  # noqa: E501

        :return: The display_name of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Integration.

        A human-friendly name used to identify the integration.  # noqa: E501

        :param display_name: The display_name of this Integration.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 100):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")  # noqa: E501

        self._display_name = display_name

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
        if not isinstance(other, Integration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Integration):
            return True

        return self.to_dict() != other.to_dict()
