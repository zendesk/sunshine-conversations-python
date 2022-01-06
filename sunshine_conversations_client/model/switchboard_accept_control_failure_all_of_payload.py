# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class SwitchboardAcceptControlFailureAllOfPayload(object):
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
        'error': 'object',
        'conversation': 'ConversationTruncated',
        'metadata': 'object'
    }

    attribute_map = {
        'error': 'error',
        'conversation': 'conversation',
        'metadata': 'metadata'
    }

    nulls = set()

    def __init__(self, error=None, conversation=None, metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """SwitchboardAcceptControlFailureAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._conversation = None
        self._metadata = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if conversation is not None:
            self.conversation = conversation
        self.metadata = metadata

    @property
    def error(self):
        """Gets the error of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501

        Object containing details of what went wrong.  # noqa: E501

        :return: The error of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SwitchboardAcceptControlFailureAllOfPayload.

        Object containing details of what went wrong.  # noqa: E501

        :param error: The error of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501
        :type: object
        """

        self._error = error

    @property
    def conversation(self):
        """Gets the conversation of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501

        The conversation from which the switchboard event was fired.  # noqa: E501

        :return: The conversation of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501
        :rtype: ConversationTruncated
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this SwitchboardAcceptControlFailureAllOfPayload.

        The conversation from which the switchboard event was fired.  # noqa: E501

        :param conversation: The conversation of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501
        :type: ConversationTruncated
        """

        self._conversation = conversation

    @property
    def metadata(self):
        """Gets the metadata of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :return: The metadata of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SwitchboardAcceptControlFailureAllOfPayload.

        Flat object containing custom properties. Strings, numbers and booleans  are the only supported format that can be passed to metadata. The metadata is limited to 4KB in size.   # noqa: E501

        :param metadata: The metadata of this SwitchboardAcceptControlFailureAllOfPayload.  # noqa: E501
        :type: object
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

        self._metadata = metadata

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
        if not isinstance(other, SwitchboardAcceptControlFailureAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwitchboardAcceptControlFailureAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()