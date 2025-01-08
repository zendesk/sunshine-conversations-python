# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.3.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class DownloadMessageRefBodyAllOfAppleInteractiveDataRef(object):
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
        'url': 'str',
        'bid': 'str',
        'key': 'str',
        'signature': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'url': 'url',
        'bid': 'bid',
        'key': 'key',
        'signature': 'signature',
        'owner': 'owner'
    }

    nulls = set()

    def __init__(self, url=None, bid=None, key=None, signature=None, owner=None, local_vars_configuration=None):  # noqa: E501
        """DownloadMessageRefBodyAllOfAppleInteractiveDataRef - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._bid = None
        self._key = None
        self._signature = None
        self._owner = None
        self.discriminator = None

        self.url = url
        self.bid = bid
        self.key = key
        self.signature = signature
        self.owner = owner

    @property
    def url(self):
        """Gets the url of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501


        :return: The url of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.


        :param url: The url of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def bid(self):
        """Gets the bid of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501


        :return: The bid of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :rtype: str
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.


        :param bid: The bid of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and bid is None:  # noqa: E501
            raise ValueError("Invalid value for `bid`, must not be `None`")  # noqa: E501

        self._bid = bid

    @property
    def key(self):
        """Gets the key of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501


        :return: The key of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.


        :param key: The key of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def signature(self):
        """Gets the signature of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501


        :return: The signature of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.


        :param signature: The signature of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def owner(self):
        """Gets the owner of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501


        :return: The owner of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.


        :param owner: The owner of this DownloadMessageRefBodyAllOfAppleInteractiveDataRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

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
        if not isinstance(other, DownloadMessageRefBodyAllOfAppleInteractiveDataRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DownloadMessageRefBodyAllOfAppleInteractiveDataRef):
            return True

        return self.to_dict() != other.to_dict()
