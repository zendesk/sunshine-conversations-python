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

class Messagebird(Integration):
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
        'access_key': 'str',
        'signing_key': 'str',
        'originator': 'str',
        'webhook_secret': 'str',
        'default_responder_id': 'str',
        'default_responder': 'DefaultResponderDefaultResponder'
    }

    attribute_map = {
        'type': 'type',
        'access_key': 'accessKey',
        'signing_key': 'signingKey',
        'originator': 'originator',
        'webhook_secret': 'webhookSecret',
        'default_responder_id': 'defaultResponderId',
        'default_responder': 'defaultResponder'
    }

    nulls = set()

    def __init__(self, type='messagebird', access_key=Undefined(), signing_key=Undefined(), originator=None, webhook_secret=None, default_responder_id=Undefined(), default_responder=Undefined(), local_vars_configuration=None, **kwargs):  # noqa: E501
        """Messagebird - a model defined in OpenAPI"""  # noqa: E501
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
        self._access_key = None
        self._signing_key = None
        self._originator = None
        self._webhook_secret = None
        self._default_responder_id = None
        self._default_responder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if access_key is not None:
            self.access_key = access_key
        if signing_key is not None:
            self.signing_key = signing_key
        self.originator = originator
        if webhook_secret is not None:
            self.webhook_secret = webhook_secret
        self.default_responder_id = default_responder_id
        self.default_responder = default_responder

    @property
    def type(self):
        """Gets the type of this Messagebird.  # noqa: E501

        To configure a MessageBird integration, acquire the accessKey, the signingKey and the MessageBird number you would like to use, then call the Create Integration endpoint. The response will include the integration’s `_id` and `webhookSecret`, which must be used to configure the webhook in MessageBird. In the Flow Builder for the MessageBird number you’ve used to integrate, add a new step with the following settings: - Create a new Call HTTP endpoint with SMS flow. - Select your desired SMS number for Incoming SMS. - Click on Forward to URL and set its method to POST. - Then, using the integration _id and webhookSecret returned from the create integration call, enter the following into the URL field:  `https://app.smooch.io/api/messagebird/webhooks/{appId}/{integrationId}/{webhookSecret}` - Select application/json for the Set Content-Type header field. - Save and publish your changes.   # noqa: E501

        :return: The type of this Messagebird.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Messagebird.

        To configure a MessageBird integration, acquire the accessKey, the signingKey and the MessageBird number you would like to use, then call the Create Integration endpoint. The response will include the integration’s `_id` and `webhookSecret`, which must be used to configure the webhook in MessageBird. In the Flow Builder for the MessageBird number you’ve used to integrate, add a new step with the following settings: - Create a new Call HTTP endpoint with SMS flow. - Select your desired SMS number for Incoming SMS. - Click on Forward to URL and set its method to POST. - Then, using the integration _id and webhookSecret returned from the create integration call, enter the following into the URL field:  `https://app.smooch.io/api/messagebird/webhooks/{appId}/{integrationId}/{webhookSecret}` - Select application/json for the Set Content-Type header field. - Save and publish your changes.   # noqa: E501

        :param type: The type of this Messagebird.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def access_key(self):
        """Gets the access_key of this Messagebird.  # noqa: E501

        The public API key of your MessageBird account.  # noqa: E501

        :return: The access_key of this Messagebird.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this Messagebird.

        The public API key of your MessageBird account.  # noqa: E501

        :param access_key: The access_key of this Messagebird.  # noqa: E501
        :type: str
        """
        if type(access_key) is Undefined:
            access_key = None
            self.nulls.discard("access_key")
        elif access_key is None:
            self.nulls.add("access_key")
        else:
            self.nulls.discard("access_key")
        if (self.local_vars_configuration.client_side_validation and
                access_key is not None and len(access_key) < 1):
            raise ValueError("Invalid value for `access_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_key = access_key

    @property
    def signing_key(self):
        """Gets the signing_key of this Messagebird.  # noqa: E501

        The signing key of your MessageBird account. Used to validate the webhooks' origin.  # noqa: E501

        :return: The signing_key of this Messagebird.  # noqa: E501
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """Sets the signing_key of this Messagebird.

        The signing key of your MessageBird account. Used to validate the webhooks' origin.  # noqa: E501

        :param signing_key: The signing_key of this Messagebird.  # noqa: E501
        :type: str
        """
        if type(signing_key) is Undefined:
            signing_key = None
            self.nulls.discard("signing_key")
        elif signing_key is None:
            self.nulls.add("signing_key")
        else:
            self.nulls.discard("signing_key")
        if (self.local_vars_configuration.client_side_validation and
                signing_key is not None and len(signing_key) < 1):
            raise ValueError("Invalid value for `signing_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._signing_key = signing_key

    @property
    def originator(self):
        """Gets the originator of this Messagebird.  # noqa: E501

        Sunshine Conversations will receive all messages sent to this phone number.  # noqa: E501

        :return: The originator of this Messagebird.  # noqa: E501
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this Messagebird.

        Sunshine Conversations will receive all messages sent to this phone number.  # noqa: E501

        :param originator: The originator of this Messagebird.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and originator is None:  # noqa: E501
            raise ValueError("Invalid value for `originator`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                originator is not None and len(originator) < 1):
            raise ValueError("Invalid value for `originator`, length must be greater than or equal to `1`")  # noqa: E501

        self._originator = originator

    @property
    def webhook_secret(self):
        """Gets the webhook_secret of this Messagebird.  # noqa: E501

        The secret that is used to configure webhooks in MessageBird.  # noqa: E501

        :return: The webhook_secret of this Messagebird.  # noqa: E501
        :rtype: str
        """
        return self._webhook_secret

    @webhook_secret.setter
    def webhook_secret(self, webhook_secret):
        """Sets the webhook_secret of this Messagebird.

        The secret that is used to configure webhooks in MessageBird.  # noqa: E501

        :param webhook_secret: The webhook_secret of this Messagebird.  # noqa: E501
        :type: str
        """

        self._webhook_secret = webhook_secret

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this Messagebird.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this Messagebird.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this Messagebird.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this Messagebird.  # noqa: E501
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
        """Gets the default_responder of this Messagebird.  # noqa: E501


        :return: The default_responder of this Messagebird.  # noqa: E501
        :rtype: DefaultResponderDefaultResponder
        """
        return self._default_responder

    @default_responder.setter
    def default_responder(self, default_responder):
        """Sets the default_responder of this Messagebird.


        :param default_responder: The default_responder of this Messagebird.  # noqa: E501
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
        if not isinstance(other, Messagebird):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Messagebird):
            return True

        return self.to_dict() != other.to_dict()
