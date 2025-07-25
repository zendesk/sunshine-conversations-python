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


class ClientRemoveEventAllOfPayload(object):
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
        'conversation': 'ConversationTruncated',
        'user': 'UserTruncated',
        'client': 'Client',
        'reason': 'str',
        'error': 'object',
        'source': 'SourceWebhook'
    }

    attribute_map = {
        'conversation': 'conversation',
        'user': 'user',
        'client': 'client',
        'reason': 'reason',
        'error': 'error',
        'source': 'source'
    }

    nulls = set()

    def __init__(self, conversation=Undefined(), user=None, client=None, reason=None, error=Undefined(), source=None, local_vars_configuration=None):  # noqa: E501
        """ClientRemoveEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation = None
        self._user = None
        self._client = None
        self._reason = None
        self._error = None
        self._source = None
        self.discriminator = None

        self.conversation = conversation
        if user is not None:
            self.user = user
        if client is not None:
            self.client = client
        if reason is not None:
            self.reason = reason
        self.error = error
        if source is not None:
            self.source = source

    @property
    def conversation(self):
        """Gets the conversation of this ClientRemoveEventAllOfPayload.  # noqa: E501

        The conversation associated with the removal of the client. This field is only present when the reason is `theft`, `linkCancelled` or `linkFailed`. Note that for the `theft` reason, the conversation will not be present if it has been deleted.   # noqa: E501

        :return: The conversation of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this ClientRemoveEventAllOfPayload.

        The conversation associated with the removal of the client. This field is only present when the reason is `theft`, `linkCancelled` or `linkFailed`. Note that for the `theft` reason, the conversation will not be present if it has been deleted.   # noqa: E501

        :param conversation: The conversation of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """
        if type(conversation) is Undefined:
            conversation = None
            self.nulls.discard("conversation")
        elif conversation is None:
            self.nulls.add("conversation")
        else:
            self.nulls.discard("conversation")

        self._conversation = conversation

    @property
    def user(self):
        """Gets the user of this ClientRemoveEventAllOfPayload.  # noqa: E501

        The user associated with the client.  # noqa: E501

        :return: The user of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :rtype: UserTruncated
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ClientRemoveEventAllOfPayload.

        The user associated with the client.  # noqa: E501

        :param user: The user of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :type: UserTruncated
        """

        self._user = user

    @property
    def client(self):
        """Gets the client of this ClientRemoveEventAllOfPayload.  # noqa: E501

        The removed client.  # noqa: E501

        :return: The client of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :rtype: Client
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this ClientRemoveEventAllOfPayload.

        The removed client.  # noqa: E501

        :param client: The client of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :type: Client
        """

        self._client = client

    @property
    def reason(self):
        """Gets the reason of this ClientRemoveEventAllOfPayload.  # noqa: E501

        The reason for which the client was removed. * `api` - The client was removed using the API. * `linkCancelled` - The user cancelled a channel link. * `linkFailed` - The client was removed after a channel link attempt failed. * `sdk` - The client was removed using the SDK. * `theft` - The client was transferred to another user due to a channel link.   # noqa: E501

        :return: The reason of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ClientRemoveEventAllOfPayload.

        The reason for which the client was removed. * `api` - The client was removed using the API. * `linkCancelled` - The user cancelled a channel link. * `linkFailed` - The client was removed after a channel link attempt failed. * `sdk` - The client was removed using the SDK. * `theft` - The client was transferred to another user due to a channel link.   # noqa: E501

        :param reason: The reason of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["api", "linkCancelled", "linkFailed", "sdk", "theft"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def error(self):
        """Gets the error of this ClientRemoveEventAllOfPayload.  # noqa: E501

        Object containing details of what went wrong. This field will only be present when the reason is `linkCancelled` or `linkFailed`.  # noqa: E501

        :return: The error of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ClientRemoveEventAllOfPayload.

        Object containing details of what went wrong. This field will only be present when the reason is `linkCancelled` or `linkFailed`.  # noqa: E501

        :param error: The error of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :type: object
        """
        if type(error) is Undefined:
            error = None
            self.nulls.discard("error")
        elif error is None:
            self.nulls.add("error")
        else:
            self.nulls.discard("error")

        self._error = error

    @property
    def source(self):
        """Gets the source of this ClientRemoveEventAllOfPayload.  # noqa: E501

        The source where this event originated from. This could be the API or an SDK device.  # noqa: E501

        :return: The source of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :rtype: SourceWebhook
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ClientRemoveEventAllOfPayload.

        The source where this event originated from. This could be the API or an SDK device.  # noqa: E501

        :param source: The source of this ClientRemoveEventAllOfPayload.  # noqa: E501
        :type: SourceWebhook
        """

        self._source = source

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
        if not isinstance(other, ClientRemoveEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientRemoveEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
