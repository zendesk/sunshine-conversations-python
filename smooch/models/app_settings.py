# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, mask_credit_card_numbers=None):
        """
        AppSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mask_credit_card_numbers': 'bool'
        }

        self.attribute_map = {
            'mask_credit_card_numbers': 'maskCreditCardNumbers'
        }

        self._mask_credit_card_numbers = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if mask_credit_card_numbers is not None:
          self.mask_credit_card_numbers = mask_credit_card_numbers

    @property
    def mask_credit_card_numbers(self):
        """
        Gets the mask_credit_card_numbers of this AppSettings.
        Flag specifying whether credit card numbers will be automatically masked if sent through Smooch.

        :return: The mask_credit_card_numbers of this AppSettings.
        :rtype: bool
        """
        return self._mask_credit_card_numbers

    @mask_credit_card_numbers.setter
    def mask_credit_card_numbers(self, mask_credit_card_numbers):
        """
        Sets the mask_credit_card_numbers of this AppSettings.
        Flag specifying whether credit card numbers will be automatically masked if sent through Smooch.

        :param mask_credit_card_numbers: The mask_credit_card_numbers of this AppSettings.
        :type: bool
        """

        self._mask_credit_card_numbers = mask_credit_card_numbers

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
        if not isinstance(other, AppSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
