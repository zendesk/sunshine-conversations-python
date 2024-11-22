# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 14.0.0
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


class OAuthEndpointsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authorize(self, client_id, response_type, **kwargs):  # noqa: E501
        """Authorize  # noqa: E501

        This endpoint begins the OAuth flow. It relies on a browser session for authentication. If the user is not logged in to Sunshine Conversations they will be redirected to the login page. If the user has many apps, they will first be prompted to select the one they wish to integrate with. They will then be presented with an Allow/Deny dialog, describing details of the access your integration is requesting.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize(client_id, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str client_id: Your integration’s unique identifier (required)
        :param str response_type: For now the only acceptable value is code. (required)
        :param str state: You may pass in any arbitrary string value here which will be returned to you along with the code via browser redirect.
        :param str redirect_uri: You may pass in a redirect_uri to determine which URI the response is redirected to. This URI must be contained in the list configured by your integration. If this option is not passed, the first URI present in the list will be used.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.authorize_with_http_info(client_id, response_type, **kwargs)  # noqa: E501

    def authorize_with_http_info(self, client_id, response_type, **kwargs):  # noqa: E501
        """Authorize  # noqa: E501

        This endpoint begins the OAuth flow. It relies on a browser session for authentication. If the user is not logged in to Sunshine Conversations they will be redirected to the login page. If the user has many apps, they will first be prompted to select the one they wish to integrate with. They will then be presented with an Allow/Deny dialog, describing details of the access your integration is requesting.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_with_http_info(client_id, response_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str client_id: Your integration’s unique identifier (required)
        :param str response_type: For now the only acceptable value is code. (required)
        :param str state: You may pass in any arbitrary string value here which will be returned to you along with the code via browser redirect.
        :param str redirect_uri: You may pass in a redirect_uri to determine which URI the response is redirected to. This URI must be contained in the list configured by your integration. If this option is not passed, the first URI present in the list will be used.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'client_id',
            'response_type',
            'state',
            'redirect_uri'
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
                    " to method authorize" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'client_id' is set
        if self.api_client.client_side_validation and ('client_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['client_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `client_id` when calling `authorize`")  # noqa: E501
        # verify the required parameter 'response_type' is set
        if self.api_client.client_side_validation and ('response_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['response_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `response_type` when calling `authorize`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_id' in local_var_params and local_var_params['client_id'] is not None:  # noqa: E501
            query_params.append(('client_id', local_var_params['client_id']))  # noqa: E501
        if 'response_type' in local_var_params and local_var_params['response_type'] is not None:  # noqa: E501
            query_params.append(('response_type', local_var_params['response_type']))  # noqa: E501
        if 'state' in local_var_params and local_var_params['state'] is not None:  # noqa: E501
            query_params.append(('state', local_var_params['state']))  # noqa: E501
        if 'redirect_uri' in local_var_params and local_var_params['redirect_uri'] is not None:  # noqa: E501
            query_params.append(('redirect_uri', local_var_params['redirect_uri']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/oauth/authorize', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token(self, inline_object, **kwargs):  # noqa: E501
        """Get Token  # noqa: E501

        This endpoint is used to exchange an authorization code for an access token. It should only be used in server-to-server calls.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token(inline_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InlineObject inline_object: (required)
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
        return self.get_token_with_http_info(inline_object, **kwargs)  # noqa: E501

    def get_token_with_http_info(self, inline_object, **kwargs):  # noqa: E501
        """Get Token  # noqa: E501

        This endpoint is used to exchange an authorization code for an access token. It should only be used in server-to-server calls.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_with_http_info(inline_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InlineObject inline_object: (required)
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
            'inline_object'
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
                    " to method get_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'inline_object' is set
        if self.api_client.client_side_validation and ('inline_object' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object` when calling `get_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object' in local_var_params:
            body_params = local_var_params['inline_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/oauth/token', 'POST',
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

    def revoke_access(self, **kwargs):  # noqa: E501
        """Revoke Access  # noqa: E501

        This endpoint is used to revoke your integration’s access to the user’s Sunshine Conversations app. Revoking access means your integration will no longer be able to interact with the app, and any webhooks the integration had previously configured will be removed.  Calling this endpoint is equivalent to the user removing your integration manually in the Sunshine Conversations web app. Your integration’s `removeUrl` (if configured) will also be called when an integration is removed in this way.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_access(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
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
        return self.revoke_access_with_http_info(**kwargs)  # noqa: E501

    def revoke_access_with_http_info(self, **kwargs):  # noqa: E501
        """Revoke Access  # noqa: E501

        This endpoint is used to revoke your integration’s access to the user’s Sunshine Conversations app. Revoking access means your integration will no longer be able to interact with the app, and any webhooks the integration had previously configured will be removed.  Calling this endpoint is equivalent to the user removing your integration manually in the Sunshine Conversations web app. Your integration’s `removeUrl` (if configured) will also be called when an integration is removed in this way.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_access_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
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
                    " to method revoke_access" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/oauth/authorization', 'DELETE',
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
