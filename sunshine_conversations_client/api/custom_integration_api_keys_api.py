# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.3.5
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


class CustomIntegrationApiKeysApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_integration_key(self, app_id, integration_id, integration_api_key, **kwargs):  # noqa: E501
        """Create Integration Key  # noqa: E501

        Creates an API key for the specified custom integration. The response body will include a secret as well it’s corresponding id, which you can use to generate JSON Web Tokens to securely make API calls on behalf of the integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_integration_key(app_id, integration_id, integration_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param IntegrationApiKey integration_api_key: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: IntegrationApiKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_custom_integration_key_with_http_info(app_id, integration_id, integration_api_key, **kwargs)  # noqa: E501

    def create_custom_integration_key_with_http_info(self, app_id, integration_id, integration_api_key, **kwargs):  # noqa: E501
        """Create Integration Key  # noqa: E501

        Creates an API key for the specified custom integration. The response body will include a secret as well it’s corresponding id, which you can use to generate JSON Web Tokens to securely make API calls on behalf of the integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_integration_key_with_http_info(app_id, integration_id, integration_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param IntegrationApiKey integration_api_key: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(IntegrationApiKeyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id',
            'integration_api_key'
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
                    " to method create_custom_integration_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `create_custom_integration_key`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `create_custom_integration_key`")  # noqa: E501
        # verify the required parameter 'integration_api_key' is set
        if self.api_client.client_side_validation and ('integration_api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_api_key` when calling `create_custom_integration_key`")  # noqa: E501

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
        if 'integration_api_key' in local_var_params:
            body_params = local_var_params['integration_api_key']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/integrations/{integrationId}/keys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationApiKeyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_custom_integration_key(self, app_id, integration_id, key_id, **kwargs):  # noqa: E501
        """Delete Integration Key  # noqa: E501

        Removes an API key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_integration_key(app_id, integration_id, key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str key_id: The id of the key. (required)
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
        return self.delete_custom_integration_key_with_http_info(app_id, integration_id, key_id, **kwargs)  # noqa: E501

    def delete_custom_integration_key_with_http_info(self, app_id, integration_id, key_id, **kwargs):  # noqa: E501
        """Delete Integration Key  # noqa: E501

        Removes an API key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_integration_key_with_http_info(app_id, integration_id, key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str key_id: The id of the key. (required)
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
            'key_id'
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
                    " to method delete_custom_integration_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `delete_custom_integration_key`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `delete_custom_integration_key`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if self.api_client.client_side_validation and ('key_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_id` when calling `delete_custom_integration_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501
        if 'key_id' in local_var_params:
            path_params['keyId'] = local_var_params['key_id']  # noqa: E501

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
            '/v2/apps/{appId}/integrations/{integrationId}/keys/{keyId}', 'DELETE',
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

    def get_custom_integration_key(self, app_id, integration_id, key_id, **kwargs):  # noqa: E501
        """Get Integration Key  # noqa: E501

        Get the specified API key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_integration_key(app_id, integration_id, key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str key_id: The id of the key. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: IntegrationApiKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_custom_integration_key_with_http_info(app_id, integration_id, key_id, **kwargs)  # noqa: E501

    def get_custom_integration_key_with_http_info(self, app_id, integration_id, key_id, **kwargs):  # noqa: E501
        """Get Integration Key  # noqa: E501

        Get the specified API key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_integration_key_with_http_info(app_id, integration_id, key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str integration_id: The id of the integration. (required)
        :param str key_id: The id of the key. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(IntegrationApiKeyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'integration_id',
            'key_id'
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
                    " to method get_custom_integration_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_custom_integration_key`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `get_custom_integration_key`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if self.api_client.client_side_validation and ('key_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_id` when calling `get_custom_integration_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'integration_id' in local_var_params:
            path_params['integrationId'] = local_var_params['integration_id']  # noqa: E501
        if 'key_id' in local_var_params:
            path_params['keyId'] = local_var_params['key_id']  # noqa: E501

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
            '/v2/apps/{appId}/integrations/{integrationId}/keys/{keyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationApiKeyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_custom_integration_keys(self, app_id, integration_id, **kwargs):  # noqa: E501
        """List Integration Keys  # noqa: E501

        Lists all API keys for a given integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_custom_integration_keys(app_id, integration_id, async_req=True)
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
        :return: IntegrationApiKeyListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_custom_integration_keys_with_http_info(app_id, integration_id, **kwargs)  # noqa: E501

    def list_custom_integration_keys_with_http_info(self, app_id, integration_id, **kwargs):  # noqa: E501
        """List Integration Keys  # noqa: E501

        Lists all API keys for a given integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_custom_integration_keys_with_http_info(app_id, integration_id, async_req=True)
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
        :return: tuple(IntegrationApiKeyListResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method list_custom_integration_keys" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `list_custom_integration_keys`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if self.api_client.client_side_validation and ('integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `integration_id` when calling `list_custom_integration_keys`")  # noqa: E501

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
            '/v2/apps/{appId}/integrations/{integrationId}/keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationApiKeyListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
