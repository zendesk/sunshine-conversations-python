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


class Message(object):
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
        'id': 'str',
        'received': 'str',
        'author': 'Author',
        'activity': 'ActivityMessage',
        'content': 'Content',
        'source': 'Source',
        'quoted_message': 'QuotedMessage',
        'metadata': 'dict',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'received': 'received',
        'author': 'author',
        'activity': 'activity',
        'content': 'content',
        'source': 'source',
        'quoted_message': 'quotedMessage',
        'metadata': 'metadata',
        'deleted': 'deleted'
    }

    nulls = set()

    def __init__(self, id=None, received=None, author=None, activity=None, content=None, source=None, quoted_message=Undefined(), metadata=Undefined(), deleted=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Message - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._received = None
        self._author = None
        self._activity = None
        self._content = None
        self._source = None
        self._quoted_message = None
        self._metadata = None
        self._deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if received is not None:
            self.received = received
        if author is not None:
            self.author = author
        if activity is not None:
            self.activity = activity
        if content is not None:
            self.content = content
        if source is not None:
            self.source = source
        self.quoted_message = quoted_message
        self.metadata = metadata
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501

        The unique ID of the message.  # noqa: E501

        :return: The id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.

        The unique ID of the message.  # noqa: E501

        :param id: The id of this Message.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def received(self):
        """Gets the received of this Message.  # noqa: E501

        A datetime string with the format `YYYY-MM-DDThh:mm:ss.SSSZ` representing when Sunshine Conversations received the message.  # noqa: E501

        :return: The received of this Message.  # noqa: E501
        :rtype: str
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this Message.

        A datetime string with the format `YYYY-MM-DDThh:mm:ss.SSSZ` representing when Sunshine Conversations received the message.  # noqa: E501

        :param received: The received of this Message.  # noqa: E501
        :type: str
        """

        self._received = received

    @property
    def author(self):
        """Gets the author of this Message.  # noqa: E501


        :return: The author of this Message.  # noqa: E501
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Message.


        :param author: The author of this Message.  # noqa: E501
        :type: Author
        """

        self._author = author

    @property
    def activity(self):
        """Gets the activity of this Message.  # noqa: E501

        Details of the system activity that generated this message. This field is used when actions taken by the system generate a persisted message to notify the user or agent of an event that occurred. For example, when a user's Ticket gets closed. This property applies only to informational text messages generated via system events.  # noqa: E501

        :return: The activity of this Message.  # noqa: E501
        :rtype: ActivityMessage
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this Message.

        Details of the system activity that generated this message. This field is used when actions taken by the system generate a persisted message to notify the user or agent of an event that occurred. For example, when a user's Ticket gets closed. This property applies only to informational text messages generated via system events.  # noqa: E501

        :param activity: The activity of this Message.  # noqa: E501
        :type: ActivityMessage
        """

        self._activity = activity

    @property
    def content(self):
        """Gets the content of this Message.  # noqa: E501

        The content of the message.  # noqa: E501

        :return: The content of this Message.  # noqa: E501
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Message.

        The content of the message.  # noqa: E501

        :param content: The content of this Message.  # noqa: E501
        :type: Content
        """

        self._content = content

    @property
    def source(self):
        """Gets the source of this Message.  # noqa: E501


        :return: The source of this Message.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Message.


        :param source: The source of this Message.  # noqa: E501
        :type: Source
        """

        self._source = source

    @property
    def quoted_message(self):
        """Gets the quoted_message of this Message.  # noqa: E501

        The quoted message is currently only available for WhatsApp and Web Messenger `formResponse` messages.  # noqa: E501

        :return: The quoted_message of this Message.  # noqa: E501
        :rtype: QuotedMessage
        """
        return self._quoted_message

    @quoted_message.setter
    def quoted_message(self, quoted_message):
        """Sets the quoted_message of this Message.

        The quoted message is currently only available for WhatsApp and Web Messenger `formResponse` messages.  # noqa: E501

        :param quoted_message: The quoted_message of this Message.  # noqa: E501
        :type: QuotedMessage
        """
        if type(quoted_message) is Undefined:
            quoted_message = None
            self.nulls.discard("quoted_message")
        elif quoted_message is None:
            self.nulls.add("quoted_message")
        else:
            self.nulls.discard("quoted_message")

        self._quoted_message = quoted_message

    @property
    def metadata(self):
        """Gets the metadata of this Message.  # noqa: E501


        :return: The metadata of this Message.  # noqa: E501
        :rtype: dict
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Message.


        :param metadata: The metadata of this Message.  # noqa: E501
        :type: dict
        """
        if type(metadata) is Undefined:
            metadata = None
            self.nulls.discard("metadata")
        elif metadata is None:
            self.nulls.add("metadata")
        else:
            self.nulls.discard("metadata")

        self._metadata = metadata

    @property
    def deleted(self):
        """Gets the deleted of this Message.  # noqa: E501

        true if the message serves as a placeholder for one that has been deleted.  # noqa: E501

        :return: The deleted of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Message.

        true if the message serves as a placeholder for one that has been deleted.  # noqa: E501

        :param deleted: The deleted of this Message.  # noqa: E501
        :type: bool
        """
        if type(deleted) is Undefined:
            deleted = None
            self.nulls.discard("deleted")
        elif deleted is None:
            self.nulls.add("deleted")
        else:
            self.nulls.discard("deleted")

        self._deleted = deleted

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
        if not isinstance(other, Message):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Message):
            return True

        return self.to_dict() != other.to_dict()
