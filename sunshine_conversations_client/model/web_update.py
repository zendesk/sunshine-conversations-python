# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class WebUpdate(object):
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
        'brand_color': 'str',
        'fixed_intro_pane': 'bool',
        'conversation_color': 'str',
        'action_color': 'str',
        'display_style': 'str',
        'button_icon_url': 'str',
        'button_width': 'str',
        'button_height': 'str',
        'integration_order': 'list[str]',
        'business_name': 'str',
        'business_icon_url': 'str',
        'background_image_url': 'str',
        'origin_whitelist': 'list[str]',
        'prechat_capture': 'PrechatCapture',
        'can_user_create_more_conversations': 'bool'
    }

    attribute_map = {
        'display_name': 'displayName',
        'default_responder_id': 'defaultResponderId',
        'brand_color': 'brandColor',
        'fixed_intro_pane': 'fixedIntroPane',
        'conversation_color': 'conversationColor',
        'action_color': 'actionColor',
        'display_style': 'displayStyle',
        'button_icon_url': 'buttonIconUrl',
        'button_width': 'buttonWidth',
        'button_height': 'buttonHeight',
        'integration_order': 'integrationOrder',
        'business_name': 'businessName',
        'business_icon_url': 'businessIconUrl',
        'background_image_url': 'backgroundImageUrl',
        'origin_whitelist': 'originWhitelist',
        'prechat_capture': 'prechatCapture',
        'can_user_create_more_conversations': 'canUserCreateMoreConversations'
    }

    nulls = set()

    def __init__(self, display_name=Undefined(), default_responder_id=Undefined(), brand_color='65758e', fixed_intro_pane=False, conversation_color='0099ff', action_color='0099ff', display_style='button', button_icon_url=Undefined(), button_width='58', button_height='58', integration_order=Undefined(), business_name=None, business_icon_url=None, background_image_url=None, origin_whitelist=Undefined(), prechat_capture=None, can_user_create_more_conversations=None, local_vars_configuration=None):  # noqa: E501
        """WebUpdate - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._default_responder_id = None
        self._brand_color = None
        self._fixed_intro_pane = None
        self._conversation_color = None
        self._action_color = None
        self._display_style = None
        self._button_icon_url = None
        self._button_width = None
        self._button_height = None
        self._integration_order = None
        self._business_name = None
        self._business_icon_url = None
        self._background_image_url = None
        self._origin_whitelist = None
        self._prechat_capture = None
        self._can_user_create_more_conversations = None
        self.discriminator = None

        self.display_name = display_name
        self.default_responder_id = default_responder_id
        if brand_color is not None:
            self.brand_color = brand_color
        if fixed_intro_pane is not None:
            self.fixed_intro_pane = fixed_intro_pane
        if conversation_color is not None:
            self.conversation_color = conversation_color
        if action_color is not None:
            self.action_color = action_color
        if display_style is not None:
            self.display_style = display_style
        self.button_icon_url = button_icon_url
        if button_width is not None:
            self.button_width = button_width
        if button_height is not None:
            self.button_height = button_height
        self.integration_order = integration_order
        if business_name is not None:
            self.business_name = business_name
        if business_icon_url is not None:
            self.business_icon_url = business_icon_url
        if background_image_url is not None:
            self.background_image_url = background_image_url
        self.origin_whitelist = origin_whitelist
        if prechat_capture is not None:
            self.prechat_capture = prechat_capture
        if can_user_create_more_conversations is not None:
            self.can_user_create_more_conversations = can_user_create_more_conversations

    @property
    def display_name(self):
        """Gets the display_name of this WebUpdate.  # noqa: E501

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :return: The display_name of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this WebUpdate.

        A human-friendly name used to identify the integration. `displayName` can be unset by changing it to `null`.  # noqa: E501

        :param display_name: The display_name of this WebUpdate.  # noqa: E501
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
        """Gets the default_responder_id of this WebUpdate.  # noqa: E501

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :return: The default_responder_id of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._default_responder_id

    @default_responder_id.setter
    def default_responder_id(self, default_responder_id):
        """Sets the default_responder_id of this WebUpdate.

        The default responder ID for the integration. This is the ID of the responder that will be used to send messages to the user. For more information, refer to <a href=\"https://docs.smooch.io/guide/switchboard/#per-channel-default-responder\">Per-channel default responder</a> guide.   # noqa: E501

        :param default_responder_id: The default_responder_id of this WebUpdate.  # noqa: E501
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
    def brand_color(self):
        """Gets the brand_color of this WebUpdate.  # noqa: E501

        This color will be used in the messenger header and the button or tab in idle state. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :return: The brand_color of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._brand_color

    @brand_color.setter
    def brand_color(self, brand_color):
        """Sets the brand_color of this WebUpdate.

        This color will be used in the messenger header and the button or tab in idle state. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :param brand_color: The brand_color of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._brand_color = brand_color

    @property
    def fixed_intro_pane(self):
        """Gets the fixed_intro_pane of this WebUpdate.  # noqa: E501

        When true, the introduction pane will be pinned at the top of the conversation instead of scrolling with it.  # noqa: E501

        :return: The fixed_intro_pane of this WebUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_intro_pane

    @fixed_intro_pane.setter
    def fixed_intro_pane(self, fixed_intro_pane):
        """Sets the fixed_intro_pane of this WebUpdate.

        When true, the introduction pane will be pinned at the top of the conversation instead of scrolling with it.  # noqa: E501

        :param fixed_intro_pane: The fixed_intro_pane of this WebUpdate.  # noqa: E501
        :type: bool
        """

        self._fixed_intro_pane = fixed_intro_pane

    @property
    def conversation_color(self):
        """Gets the conversation_color of this WebUpdate.  # noqa: E501

        This color will be used for customer messages, quick replies and actions in the footer. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :return: The conversation_color of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._conversation_color

    @conversation_color.setter
    def conversation_color(self, conversation_color):
        """Sets the conversation_color of this WebUpdate.

        This color will be used for customer messages, quick replies and actions in the footer. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :param conversation_color: The conversation_color of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._conversation_color = conversation_color

    @property
    def action_color(self):
        """Gets the action_color of this WebUpdate.  # noqa: E501

        This color will be used for call-to-actions inside your messages. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :return: The action_color of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._action_color

    @action_color.setter
    def action_color(self, action_color):
        """Sets the action_color of this WebUpdate.

        This color will be used for call-to-actions inside your messages. Must be a 3 or 6-character hexadecimal color.  # noqa: E501

        :param action_color: The action_color of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._action_color = action_color

    @property
    def display_style(self):
        """Gets the display_style of this WebUpdate.  # noqa: E501

        Choose how the messenger will appear on your website. Must be either button or tab.  # noqa: E501

        :return: The display_style of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_style

    @display_style.setter
    def display_style(self, display_style):
        """Sets the display_style of this WebUpdate.

        Choose how the messenger will appear on your website. Must be either button or tab.  # noqa: E501

        :param display_style: The display_style of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._display_style = display_style

    @property
    def button_icon_url(self):
        """Gets the button_icon_url of this WebUpdate.  # noqa: E501

        With the button style Web Messenger, you have the option of selecting your own button icon. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :return: The button_icon_url of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._button_icon_url

    @button_icon_url.setter
    def button_icon_url(self, button_icon_url):
        """Sets the button_icon_url of this WebUpdate.

        With the button style Web Messenger, you have the option of selecting your own button icon. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :param button_icon_url: The button_icon_url of this WebUpdate.  # noqa: E501
        :type: str
        """
        if type(button_icon_url) is Undefined:
            button_icon_url = None
            self.nulls.discard("button_icon_url")
        elif button_icon_url is None:
            self.nulls.add("button_icon_url")
        else:
            self.nulls.discard("button_icon_url")

        self._button_icon_url = button_icon_url

    @property
    def button_width(self):
        """Gets the button_width of this WebUpdate.  # noqa: E501

        With the button style Web Messenger, you have the option of specifying the button width.  # noqa: E501

        :return: The button_width of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._button_width

    @button_width.setter
    def button_width(self, button_width):
        """Sets the button_width of this WebUpdate.

        With the button style Web Messenger, you have the option of specifying the button width.  # noqa: E501

        :param button_width: The button_width of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._button_width = button_width

    @property
    def button_height(self):
        """Gets the button_height of this WebUpdate.  # noqa: E501

        With the button style Web Messenger, you have the option of specifying the button height.  # noqa: E501

        :return: The button_height of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._button_height

    @button_height.setter
    def button_height(self, button_height):
        """Sets the button_height of this WebUpdate.

        With the button style Web Messenger, you have the option of specifying the button height.  # noqa: E501

        :param button_height: The button_height of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._button_height = button_height

    @property
    def integration_order(self):
        """Gets the integration_order of this WebUpdate.  # noqa: E501

        Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed.  # noqa: E501

        :return: The integration_order of this WebUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._integration_order

    @integration_order.setter
    def integration_order(self, integration_order):
        """Sets the integration_order of this WebUpdate.

        Array of integration IDs, order will be reflected in the Web Messenger. When set, only integrations from this list will be displayed in the Web Messenger. If unset, all integrations will be displayed.  # noqa: E501

        :param integration_order: The integration_order of this WebUpdate.  # noqa: E501
        :type: list[str]
        """
        if type(integration_order) is Undefined:
            integration_order = None
            self.nulls.discard("integration_order")
        elif integration_order is None:
            self.nulls.add("integration_order")
        else:
            self.nulls.discard("integration_order")

        self._integration_order = integration_order

    @property
    def business_name(self):
        """Gets the business_name of this WebUpdate.  # noqa: E501

        A custom business name for the Web Messenger.  # noqa: E501

        :return: The business_name of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this WebUpdate.

        A custom business name for the Web Messenger.  # noqa: E501

        :param business_name: The business_name of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def business_icon_url(self):
        """Gets the business_icon_url of this WebUpdate.  # noqa: E501

        A custom business icon url for the Web Messenger. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :return: The business_icon_url of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._business_icon_url

    @business_icon_url.setter
    def business_icon_url(self, business_icon_url):
        """Sets the business_icon_url of this WebUpdate.

        A custom business icon url for the Web Messenger. The image must be at least 200 x 200 pixels and must be in either JPG, PNG, or GIF format.  # noqa: E501

        :param business_icon_url: The business_icon_url of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._business_icon_url = business_icon_url

    @property
    def background_image_url(self):
        """Gets the background_image_url of this WebUpdate.  # noqa: E501

        A background image url for the conversation. Image will be tiled to fit the window.  # noqa: E501

        :return: The background_image_url of this WebUpdate.  # noqa: E501
        :rtype: str
        """
        return self._background_image_url

    @background_image_url.setter
    def background_image_url(self, background_image_url):
        """Sets the background_image_url of this WebUpdate.

        A background image url for the conversation. Image will be tiled to fit the window.  # noqa: E501

        :param background_image_url: The background_image_url of this WebUpdate.  # noqa: E501
        :type: str
        """

        self._background_image_url = background_image_url

    @property
    def origin_whitelist(self):
        """Gets the origin_whitelist of this WebUpdate.  # noqa: E501

        A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454: scheme \"://\" host [ \":\" port ], where scheme is http or https.   # noqa: E501

        :return: The origin_whitelist of this WebUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._origin_whitelist

    @origin_whitelist.setter
    def origin_whitelist(self, origin_whitelist):
        """Sets the origin_whitelist of this WebUpdate.

        A list of origins to whitelist. When set, only the origins from this list will be able to initialize the Web Messenger. If unset, all origins are whitelisted. The elements in the list should follow the serialized-origin format from RFC 6454: scheme \"://\" host [ \":\" port ], where scheme is http or https.   # noqa: E501

        :param origin_whitelist: The origin_whitelist of this WebUpdate.  # noqa: E501
        :type: list[str]
        """
        if type(origin_whitelist) is Undefined:
            origin_whitelist = None
            self.nulls.discard("origin_whitelist")
        elif origin_whitelist is None:
            self.nulls.add("origin_whitelist")
        else:
            self.nulls.discard("origin_whitelist")

        self._origin_whitelist = origin_whitelist

    @property
    def prechat_capture(self):
        """Gets the prechat_capture of this WebUpdate.  # noqa: E501

        Object whose properties can be set to specify the add-on’s options. See the [guide](https://docs.smooch.io/guide/web-messenger/#prechat-capture) to learn more about Prechat Capture.  # noqa: E501

        :return: The prechat_capture of this WebUpdate.  # noqa: E501
        :rtype: PrechatCapture
        """
        return self._prechat_capture

    @prechat_capture.setter
    def prechat_capture(self, prechat_capture):
        """Sets the prechat_capture of this WebUpdate.

        Object whose properties can be set to specify the add-on’s options. See the [guide](https://docs.smooch.io/guide/web-messenger/#prechat-capture) to learn more about Prechat Capture.  # noqa: E501

        :param prechat_capture: The prechat_capture of this WebUpdate.  # noqa: E501
        :type: PrechatCapture
        """

        self._prechat_capture = prechat_capture

    @property
    def can_user_create_more_conversations(self):
        """Gets the can_user_create_more_conversations of this WebUpdate.  # noqa: E501

        Allows users to create more than one conversation on the web messenger integration.  # noqa: E501

        :return: The can_user_create_more_conversations of this WebUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_create_more_conversations

    @can_user_create_more_conversations.setter
    def can_user_create_more_conversations(self, can_user_create_more_conversations):
        """Sets the can_user_create_more_conversations of this WebUpdate.

        Allows users to create more than one conversation on the web messenger integration.  # noqa: E501

        :param can_user_create_more_conversations: The can_user_create_more_conversations of this WebUpdate.  # noqa: E501
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
        if not isinstance(other, WebUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebUpdate):
            return True

        return self.to_dict() != other.to_dict()
