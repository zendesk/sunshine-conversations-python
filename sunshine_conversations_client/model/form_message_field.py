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


class FormMessageField(object):
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
        'placeholder': 'str',
        'min_size': 'int',
        'max_size': 'int',
        'options': 'list[object]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'label': 'label',
        'text': 'text',
        'email': 'email',
        'select': 'select',
        'placeholder': 'placeholder',
        'min_size': 'minSize',
        'max_size': 'maxSize',
        'options': 'options'
    }

    nulls = set()

    def __init__(self, type=None, name=None, label=None, text=None, email=None, select=None, placeholder=None, min_size=1, max_size=128, options=None, local_vars_configuration=None):  # noqa: E501
        """FormMessageField - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._label = None
        self._text = None
        self._email = None
        self._select = None
        self._placeholder = None
        self._min_size = None
        self._max_size = None
        self._options = None
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
        if placeholder is not None:
            self.placeholder = placeholder
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if options is not None:
            self.options = options

    @property
    def type(self):
        """Gets the type of this FormMessageField.  # noqa: E501

        The field type.  # noqa: E501

        :return: The type of this FormMessageField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormMessageField.

        The field type.  # noqa: E501

        :param type: The type of this FormMessageField.  # noqa: E501
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
        """Gets the name of this FormMessageField.  # noqa: E501

        The name of the field. Must be unique per form or formResponse.  # noqa: E501

        :return: The name of this FormMessageField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormMessageField.

        The name of the field. Must be unique per form or formResponse.  # noqa: E501

        :param name: The name of this FormMessageField.  # noqa: E501
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
        """Gets the label of this FormMessageField.  # noqa: E501

        The label of the field. What the field is displayed as on Web Messenger.  # noqa: E501

        :return: The label of this FormMessageField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FormMessageField.

        The label of the field. What the field is displayed as on Web Messenger.  # noqa: E501

        :param label: The label of this FormMessageField.  # noqa: E501
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
        """Gets the text of this FormMessageField.  # noqa: E501

        Specifies the response for a text field.  # noqa: E501

        :return: The text of this FormMessageField.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FormMessageField.

        Specifies the response for a text field.  # noqa: E501

        :param text: The text of this FormMessageField.  # noqa: E501
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
        """Gets the email of this FormMessageField.  # noqa: E501

        Specifies the response for a email field.  # noqa: E501

        :return: The email of this FormMessageField.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this FormMessageField.

        Specifies the response for a email field.  # noqa: E501

        :param email: The email of this FormMessageField.  # noqa: E501
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
        """Gets the select of this FormMessageField.  # noqa: E501

        Array of objects representing the response for a field of type select. Form and formResponse messages only.  # noqa: E501

        :return: The select of this FormMessageField.  # noqa: E501
        :rtype: list[object]
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this FormMessageField.

        Array of objects representing the response for a field of type select. Form and formResponse messages only.  # noqa: E501

        :param select: The select of this FormMessageField.  # noqa: E501
        :type: list[object]
        """

        self._select = select

    @property
    def placeholder(self):
        """Gets the placeholder of this FormMessageField.  # noqa: E501

        Placeholder text for the field. Form message only.  # noqa: E501

        :return: The placeholder of this FormMessageField.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this FormMessageField.

        Placeholder text for the field. Form message only.  # noqa: E501

        :param placeholder: The placeholder of this FormMessageField.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                placeholder is not None and len(placeholder) > 128):
            raise ValueError("Invalid value for `placeholder`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                placeholder is not None and len(placeholder) < 1):
            raise ValueError("Invalid value for `placeholder`, length must be greater than or equal to `1`")  # noqa: E501

        self._placeholder = placeholder

    @property
    def min_size(self):
        """Gets the min_size of this FormMessageField.  # noqa: E501

        The minimum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :return: The min_size of this FormMessageField.  # noqa: E501
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this FormMessageField.

        The minimum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :param min_size: The min_size of this FormMessageField.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                min_size is not None and min_size > 256):  # noqa: E501
            raise ValueError("Invalid value for `min_size`, must be a value less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_size is not None and min_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `min_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this FormMessageField.  # noqa: E501

        The maximum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :return: The max_size of this FormMessageField.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this FormMessageField.

        The maximum allowed length for the response for a field of type text. Form message only.  # noqa: E501

        :param max_size: The max_size of this FormMessageField.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_size is not None and max_size > 256):  # noqa: E501
            raise ValueError("Invalid value for `max_size`, must be a value less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_size is not None and max_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_size = max_size

    @property
    def options(self):
        """Gets the options of this FormMessageField.  # noqa: E501

        Array of objects representing options for a field of type select.  # noqa: E501

        :return: The options of this FormMessageField.  # noqa: E501
        :rtype: list[object]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FormMessageField.

        Array of objects representing options for a field of type select.  # noqa: E501

        :param options: The options of this FormMessageField.  # noqa: E501
        :type: list[object]
        """

        self._options = options

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
        if not isinstance(other, FormMessageField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormMessageField):
            return True

        return self.to_dict() != other.to_dict()
