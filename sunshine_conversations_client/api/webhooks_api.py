# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sunshine_conversations_client.api_client import ApiClient
from sunshine_conversations_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WebhooksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_webhook(self, app_id, integration_id, webhook_create_body, **kwargs):  # noqa: E501
        """Create Webhook  # noqa: E501

        Creates a new webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook(app_id, integration_id, webhook_create_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param WebhookCreateBody webhook_create_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_webhook_with_http_info(app_id, integration_id, webhook_create_body, **kwargs)  # noqa: E501

    def create_webhook_with_http_info(self, app_id, integration_id, webhook_create_body, **kwargs):  # noqa: E501
        """Create Webhook  # noqa: E501

        Creates a new webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_webhook_with_http_info(app_id, integration_id, webhook_create_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param WebhookCreateBody webhook_create_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WebhookResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id',
            'webhook_create_body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_webhook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `create_webhook`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `create_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_create_body' is set
        if self.api_client.client_side_validation and ('webhook_create_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['webhook_create_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `webhook_create_body` when calling `create_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook_create_body' in local_var_params:
            body_params = local_var_params['webhook_create_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/integrations/{integrationId}/webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_webhook(self, app_id, integration_id, webhook_id, **kwargs):  # noqa: E501
        """Delete Webhook  # noqa: E501

        Deletes the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_webhook(app_id, integration_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str webhook_id: The id of the webhook. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_webhook_with_http_info(app_id, integration_id, webhook_id, **kwargs)  # noqa: E501

    def delete_webhook_with_http_info(self, app_id, integration_id, webhook_id, **kwargs):  # noqa: E501
        """Delete Webhook  # noqa: E501

        Deletes the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_webhook_with_http_info(app_id, integration_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str webhook_id: The id of the webhook. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id',
            'webhook_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `delete_webhook`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `delete_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_id' is set
        if self.api_client.client_side_validation and ('webhook_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['webhook_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `webhook_id` when calling `delete_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501
        if 'webhook_id' in local_var_params:
            path_params['webhookId'] = local_var_params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_webhook(self, app_id, integration_id, webhook_id, **kwargs):  # noqa: E501
        """Get Webhook  # noqa: E501

        Gets the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webhook(app_id, integration_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str webhook_id: The id of the webhook. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_webhook_with_http_info(app_id, integration_id, webhook_id, **kwargs)  # noqa: E501

    def get_webhook_with_http_info(self, app_id, integration_id, webhook_id, **kwargs):  # noqa: E501
        """Get Webhook  # noqa: E501

        Gets the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_webhook_with_http_info(app_id, integration_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str webhook_id: The id of the webhook. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WebhookResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id',
            'webhook_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_webhook`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `get_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_id' is set
        if self.api_client.client_side_validation and ('webhook_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['webhook_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `webhook_id` when calling `get_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501
        if 'webhook_id' in local_var_params:
            path_params['webhookId'] = local_var_params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_webhooks(self, app_id, integration_id, **kwargs):  # noqa: E501
        """List Webhooks  # noqa: E501

        Lists all webhooks for a given Sunshine Conversations Connect integration or custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_webhooks(app_id, integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WebhookListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_webhooks_with_http_info(app_id, integration_id, **kwargs)  # noqa: E501

    def list_webhooks_with_http_info(self, app_id, integration_id, **kwargs):  # noqa: E501
        """List Webhooks  # noqa: E501

        Lists all webhooks for a given Sunshine Conversations Connect integration or custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_webhooks_with_http_info(app_id, integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WebhookListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_webhooks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `list_webhooks`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `list_webhooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/integrations/{integrationId}/webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_webhook(self, app_id, integration_id, webhook_id, webhook_body, **kwargs):  # noqa: E501
        """Update Webhook  # noqa: E501

        Updates the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_webhook(app_id, integration_id, webhook_id, webhook_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str webhook_id: The id of the webhook. (required)
        :param WebhookBody webhook_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WebhookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_webhook_with_http_info(app_id, integration_id, webhook_id, webhook_body, **kwargs)  # noqa: E501

    def update_webhook_with_http_info(self, app_id, integration_id, webhook_id, webhook_body, **kwargs):  # noqa: E501
        """Update Webhook  # noqa: E501

        Updates the specified webhook associated with a Sunshine Conversations Connect integration or a custom integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_webhook_with_http_info(app_id, integration_id, webhook_id, webhook_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str webhook_id: The id of the webhook. (required)
        :param WebhookBody webhook_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WebhookResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id',
            'webhook_id',
            'webhook_body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_webhook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `update_webhook`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `update_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_id' is set
        if self.api_client.client_side_validation and ('webhook_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['webhook_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `webhook_id` when calling `update_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_body' is set
        if self.api_client.client_side_validation and ('webhook_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['webhook_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `webhook_body` when calling `update_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501
        if 'webhook_id' in local_var_params:
            path_params['webhookId'] = local_var_params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook_body' in local_var_params:
            body_params = local_var_params['webhook_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/integrations/{integrationId}/webhooks/{webhookId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
