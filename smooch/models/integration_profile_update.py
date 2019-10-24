# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IntegrationProfileUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, about=None, address=None, description=None, email=None, photo_url=None, vertical=None, websites=None):
        """
        IntegrationProfileUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'about': 'str',
            'address': 'str',
            'description': 'str',
            'email': 'str',
            'photo_url': 'str',
            'vertical': 'str',
            'websites': 'list[str]'
        }

        self.attribute_map = {
            'about': 'about',
            'address': 'address',
            'description': 'description',
            'email': 'email',
            'photo_url': 'photoUrl',
            'vertical': 'vertical',
            'websites': 'websites'
        }

        self._about = None
        self._address = None
        self._description = None
        self._email = None
        self._photo_url = None
        self._vertical = None
        self._websites = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if about is not None:
          self.about = about
        if address is not None:
          self.address = address
        if description is not None:
          self.description = description
        if email is not None:
          self.email = email
        if photo_url is not None:
          self.photo_url = photo_url
        if vertical is not None:
          self.vertical = vertical
        if websites is not None:
          self.websites = websites

    @property
    def about(self):
        """
        Gets the about of this IntegrationProfileUpdate.
        Text to display in your profile's About section. Can be used as a status update. Maximum of 139 characters.

        :return: The about of this IntegrationProfileUpdate.
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """
        Sets the about of this IntegrationProfileUpdate.
        Text to display in your profile's About section. Can be used as a status update. Maximum of 139 characters.

        :param about: The about of this IntegrationProfileUpdate.
        :type: str
        """

        self._about = about

    @property
    def address(self):
        """
        Gets the address of this IntegrationProfileUpdate.
        Address of the business. Maximum of 256 characters.

        :return: The address of this IntegrationProfileUpdate.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this IntegrationProfileUpdate.
        Address of the business. Maximum of 256 characters.

        :param address: The address of this IntegrationProfileUpdate.
        :type: str
        """

        self._address = address

    @property
    def description(self):
        """
        Gets the description of this IntegrationProfileUpdate.
        Description of the business. Maximum of 256 characters.

        :return: The description of this IntegrationProfileUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IntegrationProfileUpdate.
        Description of the business. Maximum of 256 characters.

        :param description: The description of this IntegrationProfileUpdate.
        :type: str
        """

        self._description = description

    @property
    def email(self):
        """
        Gets the email of this IntegrationProfileUpdate.
        Email address to contact the business. Maximum of 128 characters.

        :return: The email of this IntegrationProfileUpdate.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this IntegrationProfileUpdate.
        Email address to contact the business. Maximum of 128 characters.

        :param email: The email of this IntegrationProfileUpdate.
        :type: str
        """

        self._email = email

    @property
    def photo_url(self):
        """
        Gets the photo_url of this IntegrationProfileUpdate.
        URL where the business' profile photo is hosted. WhatsApp recommends an image with dimensions of 640x640 and max size of 63KB.

        :return: The photo_url of this IntegrationProfileUpdate.
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """
        Sets the photo_url of this IntegrationProfileUpdate.
        URL where the business' profile photo is hosted. WhatsApp recommends an image with dimensions of 640x640 and max size of 63KB.

        :param photo_url: The photo_url of this IntegrationProfileUpdate.
        :type: str
        """

        self._photo_url = photo_url

    @property
    def vertical(self):
        """
        Gets the vertical of this IntegrationProfileUpdate.
        Industry of the business. Maximum of 128 characters.

        :return: The vertical of this IntegrationProfileUpdate.
        :rtype: str
        """
        return self._vertical

    @vertical.setter
    def vertical(self, vertical):
        """
        Sets the vertical of this IntegrationProfileUpdate.
        Industry of the business. Maximum of 128 characters.

        :param vertical: The vertical of this IntegrationProfileUpdate.
        :type: str
        """

        self._vertical = vertical

    @property
    def websites(self):
        """
        Gets the websites of this IntegrationProfileUpdate.
        URLs associated with the business. Maximum of 2 websites.

        :return: The websites of this IntegrationProfileUpdate.
        :rtype: list[str]
        """
        return self._websites

    @websites.setter
    def websites(self, websites):
        """
        Sets the websites of this IntegrationProfileUpdate.
        URLs associated with the business. Maximum of 2 websites.

        :param websites: The websites of this IntegrationProfileUpdate.
        :type: list[str]
        """

        self._websites = websites

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
        if not isinstance(other, IntegrationProfileUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
