# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined

try:
    Integration = __import__("sunshine_conversations_client.model."+re.sub(r'(?<!^)(?=[A-Z])', '_', "Integration").lower(), fromlist=("Integration")).Integration
except ImportError:
    pass

class Twitter(Integration):
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
        'tier': 'str',
        'env_name': 'str',
        'consumer_key': 'str',
        'consumer_secret': 'str',
        'access_token_key': 'str',
        'access_token_secret': 'str',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'tier': 'tier',
        'env_name': 'envName',
        'consumer_key': 'consumerKey',
        'consumer_secret': 'consumerSecret',
        'access_token_key': 'accessTokenKey',
        'access_token_secret': 'accessTokenSecret',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='twitter', tier=None, env_name=None, consumer_key=None, consumer_secret=Undefined(), access_token_key=None, access_token_secret=Undefined(), default_responder_id=Undefined(), default_responder=Undefined(), local_vars_configuration=None, **kwargs):  # noqa: E501
        """Twitter - a model defined in OpenAPI"""  # noqa: E501
        super().__init__(**kwargs)

        if (super().openapi_types is not None):
            all_types = super().openapi_types.copy()
            all_types.update(self.openapi_types)
            self.openapi_types = all_types

        if (super().attribute_map is not None):
            all_attributes = super().attribute_map.copy()
            all_attributes.update(self.attribute_map)
            self.attribute_map = all_attributes
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._tier = None
        self._env_name = None
        self._consumer_key = None
        self._consumer_secret = None
        self._access_token_key = None
        self._access_token_secret = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.tier = tier
        if env_name is not None:
            self.env_name = env_name
        if consumer_key is not None:
            self.consumer_key = consumer_key
        if consumer_secret is not None:
            self.consumer_secret = consumer_secret
        if access_token_key is not None:
            self.access_token_key = access_token_key
        if access_token_secret is not None:
            self.access_token_secret = access_token_secret
        self.default_responder_id = default_responder_id
        self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Twitter.  # noqa: E501

        To set up a Twitter integration, please follow the steps outlined in the [Twitter Setup Guide](https://docs.smooch.io/guide/twitter/#setup).   # noqa: E501

        :return: The type of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Twitter.

        To set up a Twitter integration, please follow the steps outlined in the [Twitter Setup Guide](https://docs.smooch.io/guide/twitter/#setup).   # noqa: E501

        :param type: The type of this Twitter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def tier(self):
        """Gets the tier of this Twitter.  # noqa: E501

        Your Twitter app's tier. Only \"enterprise\" is supported for new integrations.  # noqa: E501

        :return: The tier of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this Twitter.

        Your Twitter app's tier. Only \"enterprise\" is supported for new integrations.  # noqa: E501

        :param tier: The tier of this Twitter.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tier is None:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must not be `None`")  # noqa: E501
        allowed_values = ["enterprise"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tier not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tier` ({0}), must be one of {1}"  # noqa: E501
                .format(tier, allowed_values)
            )

        self._tier = tier

    @property
    def env_name(self):
        """Gets the env_name of this Twitter.  # noqa: E501

        The Twitter dev environments label. Only required / used for sandbox and premium tiers.  # noqa: E501

        :return: The env_name of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this Twitter.

        The Twitter dev environments label. Only required / used for sandbox and premium tiers.  # noqa: E501

        :param env_name: The env_name of this Twitter.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                env_name is not None and len(env_name) < 1):
            raise ValueError("Invalid value for `env_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._env_name = env_name

    @property
    def consumer_key(self):
        """Gets the consumer_key of this Twitter.  # noqa: E501

        The consumer key for your Twitter app.  # noqa: E501

        :return: The consumer_key of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, consumer_key):
        """Sets the consumer_key of this Twitter.

        The consumer key for your Twitter app.  # noqa: E501

        :param consumer_key: The consumer_key of this Twitter.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and consumer_key is None:  # noqa: E501
            raise ValueError("Invalid value for `consumer_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                consumer_key is not None and len(consumer_key) < 1):
            raise ValueError("Invalid value for `consumer_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._consumer_key = consumer_key

    @property
    def consumer_secret(self):
        """Gets the consumer_secret of this Twitter.  # noqa: E501

        The consumer key secret for your Twitter app.  # noqa: E501

        :return: The consumer_secret of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._consumer_secret

    @consumer_secret.setter
    def consumer_secret(self, consumer_secret):
        """Sets the consumer_secret of this Twitter.

        The consumer key secret for your Twitter app.  # noqa: E501

        :param consumer_secret: The consumer_secret of this Twitter.  # noqa: E501
        :type: str
        """
        if type(consumer_secret) is Undefined:
            consumer_secret = None
            self.nulls.discard("consumer_secret")
        elif consumer_secret is None:
            self.nulls.add("consumer_secret")
        else:
            self.nulls.discard("consumer_secret")
        if (self.local_vars_configuration.client_side_validation and
                consumer_secret is not None and len(consumer_secret) < 1):
            raise ValueError("Invalid value for `consumer_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._consumer_secret = consumer_secret

    @property
    def access_token_key(self):
        """Gets the access_token_key of this Twitter.  # noqa: E501

        The access token key obtained from your user via oauth.  # noqa: E501

        :return: The access_token_key of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._access_token_key

    @access_token_key.setter
    def access_token_key(self, access_token_key):
        """Sets the access_token_key of this Twitter.

        The access token key obtained from your user via oauth.  # noqa: E501

        :param access_token_key: The access_token_key of this Twitter.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token_key is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                access_token_key is not None and len(access_token_key) < 1):
            raise ValueError("Invalid value for `access_token_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_token_key = access_token_key

    @property
    def access_token_secret(self):
        """Gets the access_token_secret of this Twitter.  # noqa: E501

        The access token secret obtained from your user via oauth.  # noqa: E501

        :return: The access_token_secret of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._access_token_secret

    @access_token_secret.setter
    def access_token_secret(self, access_token_secret):
        """Sets the access_token_secret of this Twitter.

        The access token secret obtained from your user via oauth.  # noqa: E501

        :param access_token_secret: The access_token_secret of this Twitter.  # noqa: E501
        :type: str
        """
        if type(access_token_secret) is Undefined:
            access_token_secret = None
            self.nulls.discard("access_token_secret")
        elif access_token_secret is None:
            self.nulls.add("access_token_secret")
        else:
            self.nulls.discard("access_token_secret")
        if (self.local_vars_configuration.client_side_validation and
                access_token_secret is not None and len(access_token_secret) < 1):
            raise ValueError("Invalid value for `access_token_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_token_secret = access_token_secret

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Twitter.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this Twitter.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Twitter.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Twitter.  # noqa: E501
        :type: str
        """
        if type(default_responder_id) is Undefined:
            default_responder_id = None
            self.nulls.discard("default_responder_id")
        elif default_responder_id is None:
            self.nulls.add("default_responder_id")
        else:
            self.nulls.discard("default_responder_id")

        self._default_responder_id = default_responder_id

    @property
    def default_responder(self):
        """Gets the default_responder of this Twitter.  # noqa: E501


        :return: The default_responder of this Twitter.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Twitter.


        :param default_responder: The default_responder of this Twitter.  # noqa: E501
        :type: DefaultResponderDefaultResponder
        """
        if type(default_responder) is Undefined:
            default_responder = None
            self.nulls.discard("default_responder")
        elif default_responder is None:
            self.nulls.add("default_responder")
        else:
            self.nulls.discard("default_responder")

        self._default_responder = default_responder

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
        if not isinstance(other, Twitter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Twitter):
            return True

        return self.to_dict() != other.to_dict()
