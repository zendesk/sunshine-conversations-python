# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 12.2.1
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


class SwitchboardIntegrationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_switchboard_integration(self, app_id, switchboard_id, switchboard_integration_create_body, **kwargs):  # noqa: E501
        """Create Switchboard Integration  # noqa: E501

        Create a switchboard integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_switchboard_integration(app_id, switchboard_id, switchboard_integration_create_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param SwitchboardIntegrationCreateBody switchboard_integration_create_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SwitchboardIntegrationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_switchboard_integration_with_http_info(app_id, switchboard_id, switchboard_integration_create_body, **kwargs)  # noqa: E501

    def create_switchboard_integration_with_http_info(self, app_id, switchboard_id, switchboard_integration_create_body, **kwargs):  # noqa: E501
        """Create Switchboard Integration  # noqa: E501

        Create a switchboard integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_switchboard_integration_with_http_info(app_id, switchboard_id, switchboard_integration_create_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param SwitchboardIntegrationCreateBody switchboard_integration_create_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SwitchboardIntegrationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'switchboard_id',
            'switchboard_integration_create_body'
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
                    " to method create_switchboard_integration" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `create_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_id' is set
        if self.api_client.client_side_validation and ('switchboard_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_id` when calling `create_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_integration_create_body' is set
        if self.api_client.client_side_validation and ('switchboard_integration_create_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_integration_create_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_integration_create_body` when calling `create_switchboard_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'switchboard_id' in local_var_params:
            path_params['switchboardId'] = local_var_params['switchboard_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'switchboard_integration_create_body' in local_var_params:
            body_params = local_var_params['switchboard_integration_create_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SwitchboardIntegrationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_switchboard_integration(self, app_id, switchboard_id, switchboard_integration_id, **kwargs):  # noqa: E501
        """Delete Switchboard Integration  # noqa: E501

        Deletes the switchboard integration. If the deleted switchboard integration had an active status for some conversations, the default switchboard integration will replace it. Note that it is forbidden to delete a switchboard integration if it's the default one (a new one must be chosen first) or if another switchboard integration's `nextSwitchboardIntegrationId` refers to it. The integration that was linked to the deleted switchboard integration will start receiving all conversation events, regardless of the switchboard status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_switchboard_integration(app_id, switchboard_id, switchboard_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param str switchboard_integration_id: Identifies the switchboard integration. (required)
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
        return self.delete_switchboard_integration_with_http_info(app_id, switchboard_id, switchboard_integration_id, **kwargs)  # noqa: E501

    def delete_switchboard_integration_with_http_info(self, app_id, switchboard_id, switchboard_integration_id, **kwargs):  # noqa: E501
        """Delete Switchboard Integration  # noqa: E501

        Deletes the switchboard integration. If the deleted switchboard integration had an active status for some conversations, the default switchboard integration will replace it. Note that it is forbidden to delete a switchboard integration if it's the default one (a new one must be chosen first) or if another switchboard integration's `nextSwitchboardIntegrationId` refers to it. The integration that was linked to the deleted switchboard integration will start receiving all conversation events, regardless of the switchboard status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_switchboard_integration_with_http_info(app_id, switchboard_id, switchboard_integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param str switchboard_integration_id: Identifies the switchboard integration. (required)
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
            'switchboard_id',
            'switchboard_integration_id'
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
                    " to method delete_switchboard_integration" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `delete_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_id' is set
        if self.api_client.client_side_validation and ('switchboard_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_id` when calling `delete_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_integration_id' is set
        if self.api_client.client_side_validation and ('switchboard_integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_integration_id` when calling `delete_switchboard_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'switchboard_id' in local_var_params:
            path_params['switchboardId'] = local_var_params['switchboard_id']  # noqa: E501
        if 'switchboard_integration_id' in local_var_params:
            path_params['switchboardIntegrationId'] = local_var_params['switchboard_integration_id']  # noqa: E501

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
            '/v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations/{switchboardIntegrationId}', 'DELETE',
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

    def list_switchboard_integrations(self, app_id, switchboard_id, **kwargs):  # noqa: E501
        """List Switchboard Integrations  # noqa: E501

        Lists all switchboard integrations linked to the switchboard.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_switchboard_integrations(app_id, switchboard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SwitchboardIntegrationListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_switchboard_integrations_with_http_info(app_id, switchboard_id, **kwargs)  # noqa: E501

    def list_switchboard_integrations_with_http_info(self, app_id, switchboard_id, **kwargs):  # noqa: E501
        """List Switchboard Integrations  # noqa: E501

        Lists all switchboard integrations linked to the switchboard.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_switchboard_integrations_with_http_info(app_id, switchboard_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SwitchboardIntegrationListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'switchboard_id'
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
                    " to method list_switchboard_integrations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `list_switchboard_integrations`")  # noqa: E501
        # verify the required parameter 'switchboard_id' is set
        if self.api_client.client_side_validation and ('switchboard_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_id` when calling `list_switchboard_integrations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'switchboard_id' in local_var_params:
            path_params['switchboardId'] = local_var_params['switchboard_id']  # noqa: E501

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
            '/v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SwitchboardIntegrationListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_switchboard_integration(self, app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body, **kwargs):  # noqa: E501
        """Update Switchboard Integration  # noqa: E501

        Updates a switchboard integration record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_switchboard_integration(app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param str switchboard_integration_id: Identifies the switchboard integration. (required)
        :param SwitchboardIntegrationUpdateBody switchboard_integration_update_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SwitchboardIntegrationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_switchboard_integration_with_http_info(app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body, **kwargs)  # noqa: E501

    def update_switchboard_integration_with_http_info(self, app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body, **kwargs):  # noqa: E501
        """Update Switchboard Integration  # noqa: E501

        Updates a switchboard integration record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_switchboard_integration_with_http_info(app_id, switchboard_id, switchboard_integration_id, switchboard_integration_update_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str switchboard_id: Identifies the switchboard. (required)
        :param str switchboard_integration_id: Identifies the switchboard integration. (required)
        :param SwitchboardIntegrationUpdateBody switchboard_integration_update_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SwitchboardIntegrationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'switchboard_id',
            'switchboard_integration_id',
            'switchboard_integration_update_body'
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
                    " to method update_switchboard_integration" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `update_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_id' is set
        if self.api_client.client_side_validation and ('switchboard_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_id` when calling `update_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_integration_id' is set
        if self.api_client.client_side_validation and ('switchboard_integration_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_integration_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_integration_id` when calling `update_switchboard_integration`")  # noqa: E501
        # verify the required parameter 'switchboard_integration_update_body' is set
        if self.api_client.client_side_validation and ('switchboard_integration_update_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['switchboard_integration_update_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `switchboard_integration_update_body` when calling `update_switchboard_integration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'switchboard_id' in local_var_params:
            path_params['switchboardId'] = local_var_params['switchboard_id']  # noqa: E501
        if 'switchboard_integration_id' in local_var_params:
            path_params['switchboardIntegrationId'] = local_var_params['switchboard_integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'switchboard_integration_update_body' in local_var_params:
            body_params = local_var_params['switchboard_integration_update_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations/{switchboardIntegrationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SwitchboardIntegrationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
