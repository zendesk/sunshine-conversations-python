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


class IntegrationListResponse(object):
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
        'integrations': 'list[Integration]',
        'meta': 'Meta',
        'links': 'Links'
    }

    attribute_map = {
        'integrations': 'integrations',
        'meta': 'meta',
        'links': 'links'
    }

    nulls = set()

    def __init__(self, integrations=None, meta=None, links=None, local_vars_configuration=None):  # noqa: E501
        """IntegrationListResponse - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integrations = None
        self._meta = None
        self._links = None
        self.discriminator = None

        if integrations is not None:
            self.integrations = integrations
        if meta is not None:
            self.meta = meta
        if links is not None:
            self.links = links

    @property
    def integrations(self):
        """Gets the integrations of this IntegrationListResponse.  # noqa: E501

        List of returned integrations.  # noqa: E501

        :return: The integrations of this IntegrationListResponse.  # noqa: E501
        :rtype: list[Integration]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this IntegrationListResponse.

        List of returned integrations.  # noqa: E501

        :param integrations: The integrations of this IntegrationListResponse.  # noqa: E501
        :type: list[Integration]
        """

        self._integrations = integrations

    @property
    def meta(self):
        """Gets the meta of this IntegrationListResponse.  # noqa: E501


        :return: The meta of this IntegrationListResponse.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this IntegrationListResponse.


        :param meta: The meta of this IntegrationListResponse.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

    @property
    def links(self):
        """Gets the links of this IntegrationListResponse.  # noqa: E501


        :return: The links of this IntegrationListResponse.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IntegrationListResponse.


        :param links: The links of this IntegrationListResponse.  # noqa: E501
        :type: Links
        """

        self._links = links

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
        if not isinstance(other, IntegrationListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationListResponse):
            return True

        return self.to_dict() != other.to_dict()
