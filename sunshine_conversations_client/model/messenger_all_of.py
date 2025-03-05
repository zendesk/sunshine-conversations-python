# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class MessengerAllOf(object):
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
        'page_id': 'float',
        'page_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'page_access_token': 'pageAccessToken',
        'app_id': 'appId',
        'app_secret': 'appSecret',
        'page_id': 'pageId',
        'page_name': 'pageName'
    }

    nulls = set()

    def __init__(self, type='messenger', page_access_token=Undefined(), app_id=None, app_secret=Undefined(), page_id=None, page_name=None, local_vars_configuration=None):  # noqa: E501
        """MessengerAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._page_access_token = None
        self._app_id = None
        self._app_secret = None
        self._page_id = None
        self._page_name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.page_access_token = page_access_token
        self.app_id = app_id
        if app_secret is not None:
            self.app_secret = app_secret
        if page_id is not None:
            self.page_id = page_id
        if page_name is not None:
            self.page_name = page_name

    @property
    def type(self):
        """Gets the type of this MessengerAllOf.  # noqa: E501

        Facebook Messenger Setup steps: - Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); - The Facebook app must have been submitted to Meta for app review with the “pages_manage_metadata” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. - In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.   # noqa: E501

        :return: The type of this MessengerAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MessengerAllOf.

        Facebook Messenger Setup steps: - Take note of your Facebook app ID and secret (apps can be created at developer.facebook.com); - The Facebook app must have been submitted to Meta for app review with the “pages_manage_metadata” (to retrieve Page Access Tokens for the Pages, apps that the app user administers and set a webhook) and “pages_messaging” (to send messages) permissions. - In order to integrate a Facebook Messenger app you must acquire a Page Access Token from your user. Once you have acquired a page access token from your user, call the Create Integration endpoint with your app secret and ID and the user’s page access token.   # noqa: E501

        :param type: The type of this MessengerAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def page_access_token(self):
        """Gets the page_access_token of this MessengerAllOf.  # noqa: E501

        A Facebook Page Access Token.  # noqa: E501

        :return: The page_access_token of this MessengerAllOf.  # noqa: E501
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """Sets the page_access_token of this MessengerAllOf.

        A Facebook Page Access Token.  # noqa: E501

        :param page_access_token: The page_access_token of this MessengerAllOf.  # noqa: E501
        :type: str
        """
        if type(page_access_token) is Undefined:
            page_access_token = None
            self.nulls.discard("page_access_token")
        elif page_access_token is None:
            self.nulls.add("page_access_token")
        else:
            self.nulls.discard("page_access_token")

        self._page_access_token = page_access_token

    @property
    def app_id(self):
        """Gets the app_id of this MessengerAllOf.  # noqa: E501

        A Facebook App ID.  # noqa: E501

        :return: The app_id of this MessengerAllOf.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this MessengerAllOf.

        A Facebook App ID.  # noqa: E501

        :param app_id: The app_id of this MessengerAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_secret(self):
        """Gets the app_secret of this MessengerAllOf.  # noqa: E501

        A Facebook App Secret.  # noqa: E501

        :return: The app_secret of this MessengerAllOf.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this MessengerAllOf.

        A Facebook App Secret.  # noqa: E501

        :param app_secret: The app_secret of this MessengerAllOf.  # noqa: E501
        :type: str
        """
        if type(app_secret) is Undefined:
            app_secret = None
            self.nulls.discard("app_secret")
        elif app_secret is None:
            self.nulls.add("app_secret")
        else:
            self.nulls.discard("app_secret")

        self._app_secret = app_secret

    @property
    def page_id(self):
        """Gets the page_id of this MessengerAllOf.  # noqa: E501

        A Facebook page ID.  # noqa: E501

        :return: The page_id of this MessengerAllOf.  # noqa: E501
        :rtype: float
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """Sets the page_id of this MessengerAllOf.

        A Facebook page ID.  # noqa: E501

        :param page_id: The page_id of this MessengerAllOf.  # noqa: E501
        :type: float
        """

        self._page_id = page_id

    @property
    def page_name(self):
        """Gets the page_name of this MessengerAllOf.  # noqa: E501

        A Facebook page name.  # noqa: E501

        :return: The page_name of this MessengerAllOf.  # noqa: E501
        :rtype: str
        """
        return self._page_name

    @page_name.setter
    def page_name(self, page_name):
        """Sets the page_name of this MessengerAllOf.

        A Facebook page name.  # noqa: E501

        :param page_name: The page_name of this MessengerAllOf.  # noqa: E501
        :type: str
        """

        self._page_name = page_name

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
        if not isinstance(other, MessengerAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessengerAllOf):
            return True

        return self.to_dict() != other.to_dict()
