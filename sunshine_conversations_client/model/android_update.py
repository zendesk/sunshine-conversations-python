# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class AndroidUpdate(object):
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
        'display_name': 'str',
        'default_responder_id': 'str',
        'project_id': 'str',
        'client_email': 'str',
        'private_key': 'str',
        'server_key': 'str',
        'sender_id': 'str',
        'can_user_create_more_conversations': 'bool'
    }

    attribute_map = {
        'display_name': 'displayName',
        'default_responder_id': 'defaultResponderId',
        'project_id': 'projectId',
        'client_email': 'clientEmail',
        'private_key': 'privateKey',
        'server_key': 'serverKey',
        'sender_id': 'senderId',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations'
    }

    nulls = set()

    def __init__(self, display_name=Undefined(), default_responder_id=Undefined(), project_id=Undefined(), client_email=Undefined(), private_key=Undefined(), server_key=Undefined(), sender_id=Undefined(), can_user_create_more_conversations=None, local_vars_configuration=None):  # noqa: E501
        """AndroidUpdate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._default_responder_id = None
        self._project_id = None
        self._client_email = None
        self._private_key = None
        self._server_key = None
        self._sender_id = None
        self._can_user_create_more_conversations = None
        self.discriminator = None

        self.display_name = display_name
        self.default_responder_id = default_responder_id
        self.project_id = project_id
        self.client_email = client_email
        self.private_key = private_key
        self.server_key = server_key
        self.sender_id = sender_id
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def display_name(self):
        """Gets the display_name of this AndroidUpdate.  # noqa: E501

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :return: The display_name of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AndroidUpdate.

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :param display_name: The display_name of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(display_name) is Undefined:
            display_name = None
            self.nulls.discard("display_name")
        elif display_name is None:
            self.nulls.add("display_name")
        else:
            self.nulls.discard("display_name")
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 100):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def default_responder_id(self):
        """Gets the default_responder_id of this AndroidUpdate.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this AndroidUpdate.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this AndroidUpdate.  # noqa: E501
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
    def project_id(self):
        """Gets the project_id of this AndroidUpdate.  # noqa: E501

        Your project ID from your generated private key file.  # noqa: E501

        :return: The project_id of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AndroidUpdate.

        Your project ID from your generated private key file.  # noqa: E501

        :param project_id: The project_id of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(project_id) is Undefined:
            project_id = None
            self.nulls.discard("project_id")
        elif project_id is None:
            self.nulls.add("project_id")
        else:
            self.nulls.discard("project_id")
        if (self.local_vars_configuration.client_side_validation and
                project_id is not None and len(project_id) < 1):
            raise ValueError("Invalid value for `project_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._project_id = project_id

    @property
    def client_email(self):
        """Gets the client_email of this AndroidUpdate.  # noqa: E501

        Your client email from your generated private key file.  # noqa: E501

        :return: The client_email of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._client_email

    @client_email.setter
    def client_email(self, client_email):
        """Sets the client_email of this AndroidUpdate.

        Your client email from your generated private key file.  # noqa: E501

        :param client_email: The client_email of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(client_email) is Undefined:
            client_email = None
            self.nulls.discard("client_email")
        elif client_email is None:
            self.nulls.add("client_email")
        else:
            self.nulls.discard("client_email")
        if (self.local_vars_configuration.client_side_validation and
                client_email is not None and len(client_email) < 1):
            raise ValueError("Invalid value for `client_email`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_email = client_email

    @property
    def private_key(self):
        """Gets the private_key of this AndroidUpdate.  # noqa: E501

        Your private key from your generated private key file.  # noqa: E501

        :return: The private_key of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this AndroidUpdate.

        Your private key from your generated private key file.  # noqa: E501

        :param private_key: The private_key of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(private_key) is Undefined:
            private_key = None
            self.nulls.discard("private_key")
        elif private_key is None:
            self.nulls.add("private_key")
        else:
            self.nulls.discard("private_key")
        if (self.local_vars_configuration.client_side_validation and
                private_key is not None and len(private_key) < 1):
            raise ValueError("Invalid value for `private_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._private_key = private_key

    @property
    def server_key(self):
        """Gets the server_key of this AndroidUpdate.  # noqa: E501

        Your server key from the fcm console.  # noqa: E501

        :return: The server_key of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """Sets the server_key of this AndroidUpdate.

        Your server key from the fcm console.  # noqa: E501

        :param server_key: The server_key of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(server_key) is Undefined:
            server_key = None
            self.nulls.discard("server_key")
        elif server_key is None:
            self.nulls.add("server_key")
        else:
            self.nulls.discard("server_key")
        if (self.local_vars_configuration.client_side_validation and
                server_key is not None and len(server_key) < 1):
            raise ValueError("Invalid value for `server_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_key = server_key

    @property
    def sender_id(self):
        """Gets the sender_id of this AndroidUpdate.  # noqa: E501

        Your sender id from the fcm console.  # noqa: E501

        :return: The sender_id of this AndroidUpdate.  # noqa: E501
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this AndroidUpdate.

        Your sender id from the fcm console.  # noqa: E501

        :param sender_id: The sender_id of this AndroidUpdate.  # noqa: E501
        :type: str
        """
        if type(sender_id) is Undefined:
            sender_id = None
            self.nulls.discard("sender_id")
        elif sender_id is None:
            self.nulls.add("sender_id")
        else:
            self.nulls.discard("sender_id")
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and len(sender_id) < 1):
            raise ValueError("Invalid value for `sender_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this AndroidUpdate.  # noqa: E501

        Allows users to create more than one conversation on the android integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this AndroidUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this AndroidUpdate.

        Allows users to create more than one conversation on the android integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this AndroidUpdate.  # noqa: E501
        :type: bool
        """

        self._can_user_create_more_conversations = can_user_create_more_conversations

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
        if not isinstance(other, AndroidUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidUpdate):
            return True

        return self.to_dict() != other.to_dict()
