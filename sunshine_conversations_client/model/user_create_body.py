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


class UserCreateBody(object):
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
        'external_id': 'str',
        'signed_up_at': 'str',
        'to_be_retained': 'bool',
        'profile': 'Profile',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'external_id': 'externalId',
        'signed_up_at': 'signedUpAt',
        'to_be_retained': 'toBeRetained',
        'profile': 'profile',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, external_id=None, signed_up_at=None, to_be_retained=None, profile=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """UserCreateBody - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_id = None
        self._signed_up_at = None
        self._to_be_retained = None
        self._profile = None
        self._metadata = None
        self.discriminator = None

        self.external_id = external_id
        if signed_up_at is not None:
            self.signed_up_at = signed_up_at
        if to_be_retained is not None:
            self.to_be_retained = to_be_retained
        if profile is not None:
            self.profile = profile
        self.metadata = metadata

    @property
    def external_id(self):
        """Gets the external_id of this UserCreateBody.  # noqa: E501

        A unique identifier for the user. The `externalId` can be used to link a user to the same conversation [across multiple devices](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/authenticating-users/).   # noqa: E501

        :return: The external_id of this UserCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UserCreateBody.

        A unique identifier for the user. The `externalId` can be used to link a user to the same conversation [across multiple devices](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/authenticating-users/).   # noqa: E501

        :param external_id: The external_id of this UserCreateBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_id is None:  # noqa: E501
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 1024):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) < 1):
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_id = external_id

    @property
    def signed_up_at(self):
        """Gets the signed_up_at of this UserCreateBody.  # noqa: E501

        The date at which the user signed up. Must be ISO 8601 time format `YYYY-MM-DDThh:mm:ss.sssZ`.  # noqa: E501

        :return: The signed_up_at of this UserCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._signed_up_at

    @signed_up_at.setter
    def signed_up_at(self, signed_up_at):
        """Sets the signed_up_at of this UserCreateBody.

        The date at which the user signed up. Must be ISO 8601 time format `YYYY-MM-DDThh:mm:ss.sssZ`.  # noqa: E501

        :param signed_up_at: The signed_up_at of this UserCreateBody.  # noqa: E501
        :type: str
        """

        self._signed_up_at = signed_up_at

    @property
    def to_be_retained(self):
        """Gets the to_be_retained of this UserCreateBody.  # noqa: E501

        Flag indicating whether a user should be retained after they have passed their inactive expiry. See [creating deletion schedules for bot-only conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154) for more information.  # noqa: E501

        :return: The to_be_retained of this UserCreateBody.  # noqa: E501
        :rtype: bool
        """
        return self._to_be_retained

    @to_be_retained.setter
    def to_be_retained(self, to_be_retained):
        """Sets the to_be_retained of this UserCreateBody.

        Flag indicating whether a user should be retained after they have passed their inactive expiry. See [creating deletion schedules for bot-only conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154) for more information.  # noqa: E501

        :param to_be_retained: The to_be_retained of this UserCreateBody.  # noqa: E501
        :type: bool
        """

        self._to_be_retained = to_be_retained

    @property
    def profile(self):
        """Gets the profile of this UserCreateBody.  # noqa: E501


        :return: The profile of this UserCreateBody.  # noqa: E501
        :rtype: Profile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this UserCreateBody.


        :param profile: The profile of this UserCreateBody.  # noqa: E501
        :type: Profile
        """

        self._profile = profile

    @property
    def metadata(self):
        """Gets the metadata of this UserCreateBody.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this UserCreateBody.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UserCreateBody.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this UserCreateBody.  # noqa: E501
        :type: dict(str, object)
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

        self._metadata = metadata

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
        if not isinstance(other, UserCreateBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserCreateBody):
            return True

        return self.to_dict() != other.to_dict()
