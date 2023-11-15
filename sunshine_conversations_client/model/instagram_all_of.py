# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class InstagramAllOf(object):
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
        'page_access_token': 'str',
        'app_id': 'str',
        'app_secret': 'str',
        'business_name': 'str',
        'business_username': 'str',
        'page_id': 'str',
        'business_id': 'str',
        'username': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'page_access_token': 'pageAccessToken',
        'app_id': 'appId',
        'app_secret': 'appSecret',
        'business_name': 'businessName',
        'business_username': 'businessUsername',
        'page_id': 'pageId',
        'business_id': 'businessId',
        'username': 'username',
        'user_id': 'userId'
    }

    nulls = set()

    def __init__(self, type='instagram', page_access_token=None, app_id=None, app_secret=None, business_name=None, business_username=None, page_id=None, business_id=None, username=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """InstagramAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._page_access_token = None
        self._app_id = None
        self._app_secret = None
        self._business_name = None
        self._business_username = None
        self._page_id = None
        self._business_id = None
        self._username = None
        self._user_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if page_access_token is not None:
            self.page_access_token = page_access_token
        self.app_id = app_id
        if app_secret is not None:
            self.app_secret = app_secret
        if business_name is not None:
            self.business_name = business_name
        if business_username is not None:
            self.business_username = business_username
        if page_id is not None:
            self.page_id = page_id
        if business_id is not None:
            self.business_id = business_id
        if username is not None:
            self.username = username
        if user_id is not None:
            self.user_id = user_id

    @property
    def type(self):
        """Gets the type of this InstagramAllOf.  # noqa: E501

        Instagram Direct setup steps:   - Take note of your Facebook app ID and secret (apps can be created at [developer.facebook.com](https://developer.facebook.com));   - The Facebook app must have been submitted to Meta for app review with the \"pages_manage_metadata\" (to retrieve Page Access Tokens for the Pages and apps that the app user administers and to set a webhook), \"instagram_basic\", and \"instagram_manage_messages\" (to retrieve basic Instagram account information and send messages) permissions.   - In order to integrate an Instagram Direct app, you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.   # noqa: E501

        :return: The type of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstagramAllOf.

        Instagram Direct setup steps:   - Take note of your Facebook app ID and secret (apps can be created at [developer.facebook.com](https://developer.facebook.com));   - The Facebook app must have been submitted to Meta for app review with the \"pages_manage_metadata\" (to retrieve Page Access Tokens for the Pages and apps that the app user administers and to set a webhook), \"instagram_basic\", and \"instagram_manage_messages\" (to retrieve basic Instagram account information and send messages) permissions.   - In order to integrate an Instagram Direct app, you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.   # noqa: E501

        :param type: The type of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def page_access_token(self):
        """Gets the page_access_token of this InstagramAllOf.  # noqa: E501

        The Facebook Page Access Token of the Facebook page that is linked to your Instagram account.  # noqa: E501

        :return: The page_access_token of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """Sets the page_access_token of this InstagramAllOf.

        The Facebook Page Access Token of the Facebook page that is linked to your Instagram account.  # noqa: E501

        :param page_access_token: The page_access_token of this InstagramAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `page_access_token`, must not be `None`")  # noqa: E501

        self._page_access_token = page_access_token

    @property
    def app_id(self):
        """Gets the app_id of this InstagramAllOf.  # noqa: E501

        Your Facebook App ID.  # noqa: E501

        :return: The app_id of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this InstagramAllOf.

        Your Facebook App ID.  # noqa: E501

        :param app_id: The app_id of this InstagramAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_secret(self):
        """Gets the app_secret of this InstagramAllOf.  # noqa: E501

        Your Facebook App secret.  # noqa: E501

        :return: The app_secret of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this InstagramAllOf.

        Your Facebook App secret.  # noqa: E501

        :param app_secret: The app_secret of this InstagramAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `app_secret`, must not be `None`")  # noqa: E501

        self._app_secret = app_secret

    @property
    def business_name(self):
        """Gets the business_name of this InstagramAllOf.  # noqa: E501

        Your Instagram Business account name  # noqa: E501

        :return: The business_name of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this InstagramAllOf.

        Your Instagram Business account name  # noqa: E501

        :param business_name: The business_name of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def business_username(self):
        """Gets the business_username of this InstagramAllOf.  # noqa: E501

        Your Instagram Business unique username  # noqa: E501

        :return: The business_username of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._business_username

    @business_username.setter
    def business_username(self, business_username):
        """Sets the business_username of this InstagramAllOf.

        Your Instagram Business unique username  # noqa: E501

        :param business_username: The business_username of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._business_username = business_username

    @property
    def page_id(self):
        """Gets the page_id of this InstagramAllOf.  # noqa: E501

        The ID of the Facebook Page linked to your Instagram Business account  # noqa: E501

        :return: The page_id of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """Sets the page_id of this InstagramAllOf.

        The ID of the Facebook Page linked to your Instagram Business account  # noqa: E501

        :param page_id: The page_id of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._page_id = page_id

    @property
    def business_id(self):
        """Gets the business_id of this InstagramAllOf.  # noqa: E501

        The ID of the Instagram Business account  # noqa: E501

        :return: The business_id of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this InstagramAllOf.

        The ID of the Instagram Business account  # noqa: E501

        :param business_id: The business_id of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._business_id = business_id

    @property
    def username(self):
        """Gets the username of this InstagramAllOf.  # noqa: E501

        The Facebook user's username. This is returned when integrating through the Dashboard  # noqa: E501

        :return: The username of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InstagramAllOf.

        The Facebook user's username. This is returned when integrating through the Dashboard  # noqa: E501

        :param username: The username of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_id(self):
        """Gets the user_id of this InstagramAllOf.  # noqa: E501

        The Facebook user's user ID. This is returned when integrating through the Dashboard  # noqa: E501

        :return: The user_id of this InstagramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InstagramAllOf.

        The Facebook user's user ID. This is returned when integrating through the Dashboard  # noqa: E501

        :param user_id: The user_id of this InstagramAllOf.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, InstagramAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstagramAllOf):
            return True

        return self.to_dict() != other.to_dict()
