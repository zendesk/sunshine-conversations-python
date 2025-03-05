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


class ReferralDetails(object):
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
        'source': 'str',
        'type': 'str',
        'ad_id': 'str'
    }

    attribute_map = {
        'source': 'source',
        'type': 'type',
        'ad_id': 'adId'
    }

    nulls = set()

    def __init__(self, source=None, type=None, ad_id=Undefined(), local_vars_configuration=None):  # noqa: E501
        """ReferralDetails - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._type = None
        self._ad_id = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if type is not None:
            self.type = type
        self.ad_id = ad_id

    @property
    def source(self):
        """Gets the source of this ReferralDetails.  # noqa: E501

        The source of the referral - MESSENGER_CODE, ADS etc…  # noqa: E501

        :return: The source of this ReferralDetails.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ReferralDetails.

        The source of the referral - MESSENGER_CODE, ADS etc…  # noqa: E501

        :param source: The source of this ReferralDetails.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this ReferralDetails.  # noqa: E501

        The type of referral, typically OPEN-THREAD.  # noqa: E501

        :return: The type of this ReferralDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReferralDetails.

        The type of referral, typically OPEN-THREAD.  # noqa: E501

        :param type: The type of this ReferralDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ad_id(self):
        """Gets the ad_id of this ReferralDetails.  # noqa: E501

        If the referral came from an ad, this field will be present with the ad’s Id.  # noqa: E501

        :return: The ad_id of this ReferralDetails.  # noqa: E501
        :rtype: str
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this ReferralDetails.

        If the referral came from an ad, this field will be present with the ad’s Id.  # noqa: E501

        :param ad_id: The ad_id of this ReferralDetails.  # noqa: E501
        :type: str
        """
        if type(ad_id) is Undefined:
            ad_id = None
            self.nulls.discard("ad_id")
        elif ad_id is None:
            self.nulls.add("ad_id")
        else:
            self.nulls.discard("ad_id")

        self._ad_id = ad_id

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
        if not isinstance(other, ReferralDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferralDetails):
            return True

        return self.to_dict() != other.to_dict()
