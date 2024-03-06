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


class ClientCreate(object):
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
        'match_criteria': 'MatchCriteria',
        'confirmation': 'Confirmation',
        'target': 'Target'
    }

    attribute_map = {
        'match_criteria': 'matchCriteria',
        'confirmation': 'confirmation',
        'target': 'target'
    }

    nulls = set()

    def __init__(self, match_criteria=None, confirmation=None, target=None, local_vars_configuration=None):  # noqa: E501
        """ClientCreate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._match_criteria = None
        self._confirmation = None
        self._target = None
        self.discriminator = None

        self.match_criteria = match_criteria
        self.confirmation = confirmation
        self.target = target

    @property
    def match_criteria(self):
        """Gets the match_criteria of this ClientCreate.  # noqa: E501


        :return: The match_criteria of this ClientCreate.  # noqa: E501
        :rtype: MatchCriteria
        """
        return self._match_criteria

    @match_criteria.setter
    def match_criteria(self, match_criteria):
        """Sets the match_criteria of this ClientCreate.


        :param match_criteria: The match_criteria of this ClientCreate.  # noqa: E501
        :type: MatchCriteria
        """
        if self.local_vars_configuration.client_side_validation and match_criteria is None:  # noqa: E501
            raise ValueError("Invalid value for `match_criteria`, must not be `None`")  # noqa: E501

        self._match_criteria = match_criteria

    @property
    def confirmation(self):
        """Gets the confirmation of this ClientCreate.  # noqa: E501


        :return: The confirmation of this ClientCreate.  # noqa: E501
        :rtype: Confirmation
        """
        return self._confirmation

    @confirmation.setter
    def confirmation(self, confirmation):
        """Sets the confirmation of this ClientCreate.


        :param confirmation: The confirmation of this ClientCreate.  # noqa: E501
        :type: Confirmation
        """
        if self.local_vars_configuration.client_side_validation and confirmation is None:  # noqa: E501
            raise ValueError("Invalid value for `confirmation`, must not be `None`")  # noqa: E501

        self._confirmation = confirmation

    @property
    def target(self):
        """Gets the target of this ClientCreate.  # noqa: E501


        :return: The target of this ClientCreate.  # noqa: E501
        :rtype: Target
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ClientCreate.


        :param target: The target of this ClientCreate.  # noqa: E501
        :type: Target
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, ClientCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientCreate):
            return True

        return self.to_dict() != other.to_dict()
