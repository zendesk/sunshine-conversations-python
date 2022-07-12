# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class Device(object):
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
        'type': 'str',
        'guid': 'str',
        'client_id': 'str',
        'status': 'str',
        'integration_id': 'str',
        'last_seen': 'str',
        'push_notification_token': 'str',
        'info': 'object',
        'app_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'guid': 'guid',
        'client_id': 'clientId',
        'status': 'status',
        'integration_id': 'integrationId',
        'last_seen': 'lastSeen',
        'push_notification_token': 'pushNotificationToken',
        'info': 'info',
        'app_version': 'appVersion'
    }

    nulls = set()

    def __init__(self, id=None, type=None, guid=None, client_id=None, status=None, integration_id=None, last_seen=None, push_notification_token=Undefined(), info=Undefined(), app_version=Undefined(), local_vars_configuration=None):  # noqa: E501
        """Device - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._guid = None
        self._client_id = None
        self._status = None
        self._integration_id = None
        self._last_seen = None
        self._push_notification_token = None
        self._info = None
        self._app_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if guid is not None:
            self.guid = guid
        if client_id is not None:
            self.client_id = client_id
        if status is not None:
            self.status = status
        if integration_id is not None:
            self.integration_id = integration_id
        if last_seen is not None:
            self.last_seen = last_seen
        self.push_notification_token = push_notification_token
        self.info = info
        self.app_version = app_version

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501

        The unique ID of the device.  # noqa: E501

        :return: The id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.

        The unique ID of the device.  # noqa: E501

        :param id: The id of this Device.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501

        The type of integration that the device represents.  # noqa: E501

        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.

        The type of integration that the device represents.  # noqa: E501

        :param type: The type of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["android", "ios", "web"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def guid(self):
        """Gets the guid of this Device.  # noqa: E501

        A unique identifier for the device, generated client-side by the SDK.  # noqa: E501

        :return: The guid of this Device.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Device.

        A unique identifier for the device, generated client-side by the SDK.  # noqa: E501

        :param guid: The guid of this Device.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def client_id(self):
        """Gets the client_id of this Device.  # noqa: E501

        The id of the client to which this device is associated.  # noqa: E501

        :return: The client_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Device.

        The id of the client to which this device is associated.  # noqa: E501

        :param client_id: The client_id of this Device.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def status(self):
        """Gets the status of this Device.  # noqa: E501

        The device status. Indicates if the device will receive push notifications or not.  # noqa: E501

        :return: The status of this Device.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Device.

        The device status. Indicates if the device will receive push notifications or not.  # noqa: E501

        :param status: The status of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def integration_id(self):
        """Gets the integration_id of this Device.  # noqa: E501

        The ID of the integration that the device was created for.  # noqa: E501

        :return: The integration_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this Device.

        The ID of the integration that the device was created for.  # noqa: E501

        :param integration_id: The integration_id of this Device.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def last_seen(self):
        """Gets the last_seen of this Device.  # noqa: E501

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the last time the user interacted with this device.  # noqa: E501

        :return: The last_seen of this Device.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Device.

        A datetime string with the format YYYY-MM-DDThh:mm:ss.SSSZ representing the last time the user interacted with this device.  # noqa: E501

        :param last_seen: The last_seen of this Device.  # noqa: E501
        :type: str
        """

        self._last_seen = last_seen

    @property
    def push_notification_token(self):
        """Gets the push_notification_token of this Device.  # noqa: E501

        The token used for push notifications on Android and iOS devices.  # noqa: E501

        :return: The push_notification_token of this Device.  # noqa: E501
        :rtype: str
        """
        return self._push_notification_token

    @push_notification_token.setter
    def push_notification_token(self, push_notification_token):
        """Sets the push_notification_token of this Device.

        The token used for push notifications on Android and iOS devices.  # noqa: E501

        :param push_notification_token: The push_notification_token of this Device.  # noqa: E501
        :type: str
        """
        if type(push_notification_token) is Undefined:
            push_notification_token = None
            self.nulls.discard("push_notification_token")
        elif push_notification_token is None:
            self.nulls.add("push_notification_token")
        else:
            self.nulls.discard("push_notification_token")

        self._push_notification_token = push_notification_token

    @property
    def info(self):
        """Gets the info of this Device.  # noqa: E501

        A flat curated object with properties that vary for each SDK platform. All keys are optional and not guaranteed to be available.  # noqa: E501

        :return: The info of this Device.  # noqa: E501
        :rtype: object
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Device.

        A flat curated object with properties that vary for each SDK platform. All keys are optional and not guaranteed to be available.  # noqa: E501

        :param info: The info of this Device.  # noqa: E501
        :type: object
        """
        if type(info) is Undefined:
            info = None
            self.nulls.discard("info")
        elif info is None:
            self.nulls.add("info")
        else:
            self.nulls.discard("info")

        self._info = info

    @property
    def app_version(self):
        """Gets the app_version of this Device.  # noqa: E501

        Version of the mobile app in which the SDK is embedded. Not applicable for devices of type web.  # noqa: E501

        :return: The app_version of this Device.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this Device.

        Version of the mobile app in which the SDK is embedded. Not applicable for devices of type web.  # noqa: E501

        :param app_version: The app_version of this Device.  # noqa: E501
        :type: str
        """
        if type(app_version) is Undefined:
            app_version = None
            self.nulls.discard("app_version")
        elif app_version is None:
            self.nulls.add("app_version")
        else:
            self.nulls.discard("app_version")

        self._app_version = app_version

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
        if not isinstance(other, Device):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Device):
            return True

        return self.to_dict() != other.to_dict()
