# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.8.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class AppSettings(object):
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
        'conversation_retention_seconds': 'int',
        'mask_credit_card_numbers': 'bool',
        'use_animal_names': 'bool',
        'echo_postback': 'bool',
        'ignore_auto_conversation_start': 'bool',
        'multi_convo_enabled': 'bool',
        'attachments_access': 'str',
        'attachments_token_expiration_seconds': 'int',
        'app_localization_enabled': 'bool'
    }

    attribute_map = {
        'conversation_retention_seconds': 'conversationRetentionSeconds',
        'mask_credit_card_numbers': 'maskCreditCardNumbers',
        'use_animal_names': 'useAnimalNames',
        'echo_postback': 'echoPostback',
        'ignore_auto_conversation_start': 'ignoreAutoConversationStart',
        'multi_convo_enabled': 'multiConvoEnabled',
        'attachments_access': 'attachmentsAccess',
        'attachments_token_expiration_seconds': 'attachmentsTokenExpirationSeconds',
        'app_localization_enabled': 'appLocalizationEnabled'
    }

    nulls = set()

    def __init__(self, conversation_retention_seconds=None, mask_credit_card_numbers=None, use_animal_names=None, echo_postback=None, ignore_auto_conversation_start=None, multi_convo_enabled=None, attachments_access=None, attachments_token_expiration_seconds=None, app_localization_enabled=None, local_vars_configuration=None):  # noqa: E501
        """AppSettings - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversation_retention_seconds = None
        self._mask_credit_card_numbers = None
        self._use_animal_names = None
        self._echo_postback = None
        self._ignore_auto_conversation_start = None
        self._multi_convo_enabled = None
        self._attachments_access = None
        self._attachments_token_expiration_seconds = None
        self._app_localization_enabled = None
        self.discriminator = None

        if conversation_retention_seconds is not None:
            self.conversation_retention_seconds = conversation_retention_seconds
        if mask_credit_card_numbers is not None:
            self.mask_credit_card_numbers = mask_credit_card_numbers
        if use_animal_names is not None:
            self.use_animal_names = use_animal_names
        if echo_postback is not None:
            self.echo_postback = echo_postback
        if ignore_auto_conversation_start is not None:
            self.ignore_auto_conversation_start = ignore_auto_conversation_start
        if multi_convo_enabled is not None:
            self.multi_convo_enabled = multi_convo_enabled
        if attachments_access is not None:
            self.attachments_access = attachments_access
        if attachments_token_expiration_seconds is not None:
            self.attachments_token_expiration_seconds = attachments_token_expiration_seconds
        if app_localization_enabled is not None:
            self.app_localization_enabled = app_localization_enabled

    @property
    def conversation_retention_seconds(self):
        """Gets the conversation_retention_seconds of this AppSettings.  # noqa: E501

        Number of seconds of inactivity before a conversation’s messages  will be automatically deleted. See  [Conversation Retention Seconds](https://docs.smooch.io/guide/creating-and-managing-apps/#conversation-retention-seconds) for more information.   # noqa: E501

        :return: The conversation_retention_seconds of this AppSettings.  # noqa: E501
        :rtype: int
        """
        return self._conversation_retention_seconds

    @conversation_retention_seconds.setter
    def conversation_retention_seconds(self, conversation_retention_seconds):
        """Sets the conversation_retention_seconds of this AppSettings.

        Number of seconds of inactivity before a conversation’s messages  will be automatically deleted. See  [Conversation Retention Seconds](https://docs.smooch.io/guide/creating-and-managing-apps/#conversation-retention-seconds) for more information.   # noqa: E501

        :param conversation_retention_seconds: The conversation_retention_seconds of this AppSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                conversation_retention_seconds is not None and conversation_retention_seconds < 0):  # noqa: E501
            raise ValueError("Invalid value for `conversation_retention_seconds`, must be a value greater than or equal to `0`")  # noqa: E501

        self._conversation_retention_seconds = conversation_retention_seconds

    @property
    def mask_credit_card_numbers(self):
        """Gets the mask_credit_card_numbers of this AppSettings.  # noqa: E501

        A boolean specifying whether credit card numbers should be masked  when sent through Sunshine Conversations.   # noqa: E501

        :return: The mask_credit_card_numbers of this AppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._mask_credit_card_numbers

    @mask_credit_card_numbers.setter
    def mask_credit_card_numbers(self, mask_credit_card_numbers):
        """Sets the mask_credit_card_numbers of this AppSettings.

        A boolean specifying whether credit card numbers should be masked  when sent through Sunshine Conversations.   # noqa: E501

        :param mask_credit_card_numbers: The mask_credit_card_numbers of this AppSettings.  # noqa: E501
        :type: bool
        """

        self._mask_credit_card_numbers = mask_credit_card_numbers

    @property
    def use_animal_names(self):
        """Gets the use_animal_names of this AppSettings.  # noqa: E501

        A boolean specifying whether animal names should be used for  unnamed users. See the  [user naming guide](https://docs.smooch.io/guide/receiving-messages/#message-author-name) for details.   # noqa: E501

        :return: The use_animal_names of this AppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_animal_names

    @use_animal_names.setter
    def use_animal_names(self, use_animal_names):
        """Sets the use_animal_names of this AppSettings.

        A boolean specifying whether animal names should be used for  unnamed users. See the  [user naming guide](https://docs.smooch.io/guide/receiving-messages/#message-author-name) for details.   # noqa: E501

        :param use_animal_names: The use_animal_names of this AppSettings.  # noqa: E501
        :type: bool
        """

        self._use_animal_names = use_animal_names

    @property
    def echo_postback(self):
        """Gets the echo_postback of this AppSettings.  # noqa: E501

        A boolean specifying whether a message should be added to the conversation  history when a postback button is clicked. See  [Echo Postbacks](https://docs.smooch.io/guide/creating-and-managing-apps/#echo-postbacks) for more information.   # noqa: E501

        :return: The echo_postback of this AppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._echo_postback

    @echo_postback.setter
    def echo_postback(self, echo_postback):
        """Sets the echo_postback of this AppSettings.

        A boolean specifying whether a message should be added to the conversation  history when a postback button is clicked. See  [Echo Postbacks](https://docs.smooch.io/guide/creating-and-managing-apps/#echo-postbacks) for more information.   # noqa: E501

        :param echo_postback: The echo_postback of this AppSettings.  # noqa: E501
        :type: bool
        """

        self._echo_postback = echo_postback

    @property
    def ignore_auto_conversation_start(self):
        """Gets the ignore_auto_conversation_start of this AppSettings.  # noqa: E501

        A boolean specifying whether a non message event coming from a channel will  trigger a  [start conversation](https://docs.smooch.io/rest/#section/Webhook-Triggers) event and count as a monthly active user (MAU). <aside class=\"notice\">Calling <code>startConversation()</code> (or equivalent) from the Android,  iOS or Web SDK will count as a MAU, regardless of the value of this setting.</aside>   # noqa: E501

        :return: The ignore_auto_conversation_start of this AppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_auto_conversation_start

    @ignore_auto_conversation_start.setter
    def ignore_auto_conversation_start(self, ignore_auto_conversation_start):
        """Sets the ignore_auto_conversation_start of this AppSettings.

        A boolean specifying whether a non message event coming from a channel will  trigger a  [start conversation](https://docs.smooch.io/rest/#section/Webhook-Triggers) event and count as a monthly active user (MAU). <aside class=\"notice\">Calling <code>startConversation()</code> (or equivalent) from the Android,  iOS or Web SDK will count as a MAU, regardless of the value of this setting.</aside>   # noqa: E501

        :param ignore_auto_conversation_start: The ignore_auto_conversation_start of this AppSettings.  # noqa: E501
        :type: bool
        """

        self._ignore_auto_conversation_start = ignore_auto_conversation_start

    @property
    def multi_convo_enabled(self):
        """Gets the multi_convo_enabled of this AppSettings.  # noqa: E501

        A boolean specifying whether users are allowed to be part of several conversations. Enabling `multiConvo` is **irreversible**.   # noqa: E501

        :return: The multi_convo_enabled of this AppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._multi_convo_enabled

    @multi_convo_enabled.setter
    def multi_convo_enabled(self, multi_convo_enabled):
        """Sets the multi_convo_enabled of this AppSettings.

        A boolean specifying whether users are allowed to be part of several conversations. Enabling `multiConvo` is **irreversible**.   # noqa: E501

        :param multi_convo_enabled: The multi_convo_enabled of this AppSettings.  # noqa: E501
        :type: bool
        """

        self._multi_convo_enabled = multi_convo_enabled

    @property
    def attachments_access(self):
        """Gets the attachments_access of this AppSettings.  # noqa: E501

        A string specifying whether attachments should be stored in a publicly or privately accessible cloud storage. attachmentsAccess is set to public by default but can be modified to private.   # noqa: E501

        :return: The attachments_access of this AppSettings.  # noqa: E501
        :rtype: str
        """
        return self._attachments_access

    @attachments_access.setter
    def attachments_access(self, attachments_access):
        """Sets the attachments_access of this AppSettings.

        A string specifying whether attachments should be stored in a publicly or privately accessible cloud storage. attachmentsAccess is set to public by default but can be modified to private.   # noqa: E501

        :param attachments_access: The attachments_access of this AppSettings.  # noqa: E501
        :type: str
        """

        self._attachments_access = attachments_access

    @property
    def attachments_token_expiration_seconds(self):
        """Gets the attachments_token_expiration_seconds of this AppSettings.  # noqa: E501

        Number of seconds representing the expiration time of the generated media tokens for private attachments. The JWT will be valid for 2 hours by default.   # noqa: E501

        :return: The attachments_token_expiration_seconds of this AppSettings.  # noqa: E501
        :rtype: int
        """
        return self._attachments_token_expiration_seconds

    @attachments_token_expiration_seconds.setter
    def attachments_token_expiration_seconds(self, attachments_token_expiration_seconds):
        """Sets the attachments_token_expiration_seconds of this AppSettings.

        Number of seconds representing the expiration time of the generated media tokens for private attachments. The JWT will be valid for 2 hours by default.   # noqa: E501

        :param attachments_token_expiration_seconds: The attachments_token_expiration_seconds of this AppSettings.  # noqa: E501
        :type: int
        """

        self._attachments_token_expiration_seconds = attachments_token_expiration_seconds

    @property
    def app_localization_enabled(self):
        """Gets the app_localization_enabled of this AppSettings.  # noqa: E501

        A boolean specifying whether the messages authored by the Sunshine Conversations platform should be localized.   # noqa: E501

        :return: The app_localization_enabled of this AppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._app_localization_enabled

    @app_localization_enabled.setter
    def app_localization_enabled(self, app_localization_enabled):
        """Sets the app_localization_enabled of this AppSettings.

        A boolean specifying whether the messages authored by the Sunshine Conversations platform should be localized.   # noqa: E501

        :param app_localization_enabled: The app_localization_enabled of this AppSettings.  # noqa: E501
        :type: bool
        """

        self._app_localization_enabled = app_localization_enabled

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
        if not isinstance(other, AppSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppSettings):
            return True

        return self.to_dict() != other.to_dict()
