# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class FormResponseMessageField(object):
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
        'name': 'str',
        'label': 'str',
        'text': 'str',
        'email': 'str',
        'select': 'list[object]',
        'quoted_message_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'label': 'label',
        'text': 'text',
        'email': 'email',
        'select': 'select',
        'quoted_message_id': 'quotedMessageId'
    }

    nulls = set()

    def __init__(self, type=None, name=None, label=None, text=None, email=None, select=None, quoted_message_id=None, local_vars_configuration=None):  # noqa: E501
        """FormResponseMessageField - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._label = None
        self._text = None
        self._email = None
        self._select = None
        self._quoted_message_id = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.label = label
        if text is not None:
            self.text = text
        if email is not None:
            self.email = email
        if select is not None:
            self.select = select
        if quoted_message_id is not None:
            self.quoted_message_id = quoted_message_id

    @property
    def type(self):
        """Gets the type of this FormResponseMessageField.  # noqa: E501

        The field type.  # noqa: E501

        :return: The type of this FormResponseMessageField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormResponseMessageField.

        The field type.  # noqa: E501

        :param type: The type of this FormResponseMessageField.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["email", "select", "text"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this FormResponseMessageField.  # noqa: E501

        The name of the field. Must be unique per form or formResponse.  # noqa: E501

        :return: The name of this FormResponseMessageField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormResponseMessageField.

        The name of the field. Must be unique per form or formResponse.  # noqa: E501

        :param name: The name of this FormResponseMessageField.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this FormResponseMessageField.  # noqa: E501

        The label of the field. What the field is displayed as on Web Messenger.  # noqa: E501

        :return: The label of this FormResponseMessageField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FormResponseMessageField.

        The label of the field. What the field is displayed as on Web Messenger.  # noqa: E501

        :param label: The label of this FormResponseMessageField.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) > 128):
            raise ValueError("Invalid value for `label`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) < 1):
            raise ValueError("Invalid value for `label`, length must be greater than or equal to `1`")  # noqa: E501

        self._label = label

    @property
    def text(self):
        """Gets the text of this FormResponseMessageField.  # noqa: E501

        Specifies the response for a text field.  # noqa: E501

        :return: The text of this FormResponseMessageField.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FormResponseMessageField.

        Specifies the response for a text field.  # noqa: E501

        :param text: The text of this FormResponseMessageField.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) > 256):
            raise ValueError("Invalid value for `text`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) < 1):
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def email(self):
        """Gets the email of this FormResponseMessageField.  # noqa: E501

        Specifies the response for a email field.  # noqa: E501

        :return: The email of this FormResponseMessageField.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this FormResponseMessageField.

        Specifies the response for a email field.  # noqa: E501

        :param email: The email of this FormResponseMessageField.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 128):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def select(self):
        """Gets the select of this FormResponseMessageField.  # noqa: E501

        Array of objects representing the response for a field of type select. Form and formResponse messages only.  # noqa: E501

        :return: The select of this FormResponseMessageField.  # noqa: E501
        :rtype: list[object]
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this FormResponseMessageField.

        Array of objects representing the response for a field of type select. Form and formResponse messages only.  # noqa: E501

        :param select: The select of this FormResponseMessageField.  # noqa: E501
        :type: list[object]
        """

        self._select = select

    @property
    def quoted_message_id(self):
        """Gets the quoted_message_id of this FormResponseMessageField.  # noqa: E501

        The messageId for the form that this response belongs to.  # noqa: E501

        :return: The quoted_message_id of this FormResponseMessageField.  # noqa: E501
        :rtype: str
        """
        return self._quoted_message_id

    @quoted_message_id.setter
    def quoted_message_id(self, quoted_message_id):
        """Sets the quoted_message_id of this FormResponseMessageField.

        The messageId for the form that this response belongs to.  # noqa: E501

        :param quoted_message_id: The quoted_message_id of this FormResponseMessageField.  # noqa: E501
        :type: str
        """

        self._quoted_message_id = quoted_message_id

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
        if not isinstance(other, FormResponseMessageField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormResponseMessageField):
            return True

        return self.to_dict() != other.to_dict()
