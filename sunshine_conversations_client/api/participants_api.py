# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 15.1.0
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


class ParticipantsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def join_conversation(self, app_id, conversation_id, participant_join_body, **kwargs):  # noqa: E501
        """Join Conversation  # noqa: E501

        Adds a user to a conversation using either their userId or userExternalId. The endpoint only supports adding a participant to a sdkGroup conversation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_conversation(app_id, conversation_id, participant_join_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str conversation_id: Identifies the conversation. (required)
        :param ParticipantJoinBody participant_join_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ParticipantResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.join_conversation_with_http_info(app_id, conversation_id, participant_join_body, **kwargs)  # noqa: E501

    def join_conversation_with_http_info(self, app_id, conversation_id, participant_join_body, **kwargs):  # noqa: E501
        """Join Conversation  # noqa: E501

        Adds a user to a conversation using either their userId or userExternalId. The endpoint only supports adding a participant to a sdkGroup conversation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_conversation_with_http_info(app_id, conversation_id, participant_join_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str conversation_id: Identifies the conversation. (required)
        :param ParticipantJoinBody participant_join_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ParticipantResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'conversation_id',
            'participant_join_body'
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
                    " to method join_conversation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `join_conversation`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if self.api_client.client_side_validation and ('conversation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['conversation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `conversation_id` when calling `join_conversation`")  # noqa: E501
        # verify the required parameter 'participant_join_body' is set
        if self.api_client.client_side_validation and ('participant_join_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['participant_join_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `participant_join_body` when calling `join_conversation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'conversation_id' in local_var_params:
            path_params['conversationId'] = local_var_params['conversation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'participant_join_body' in local_var_params:
            body_params = local_var_params['participant_join_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/conversations/{conversationId}/join', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParticipantResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def leave_conversation(self, app_id, conversation_id, participant_leave_body, **kwargs):  # noqa: E501
        """Leave Conversation  # noqa: E501

        Removes a user from a conversation using either their userId, userExternalId, or participantId.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_conversation(app_id, conversation_id, participant_leave_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str conversation_id: Identifies the conversation. (required)
        :param ParticipantLeaveBody participant_leave_body: (required)
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
        return self.leave_conversation_with_http_info(app_id, conversation_id, participant_leave_body, **kwargs)  # noqa: E501

    def leave_conversation_with_http_info(self, app_id, conversation_id, participant_leave_body, **kwargs):  # noqa: E501
        """Leave Conversation  # noqa: E501

        Removes a user from a conversation using either their userId, userExternalId, or participantId.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.leave_conversation_with_http_info(app_id, conversation_id, participant_leave_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str conversation_id: Identifies the conversation. (required)
        :param ParticipantLeaveBody participant_leave_body: (required)
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
            'conversation_id',
            'participant_leave_body'
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
                    " to method leave_conversation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `leave_conversation`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if self.api_client.client_side_validation and ('conversation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['conversation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `conversation_id` when calling `leave_conversation`")  # noqa: E501
        # verify the required parameter 'participant_leave_body' is set
        if self.api_client.client_side_validation and ('participant_leave_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['participant_leave_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `participant_leave_body` when calling `leave_conversation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'conversation_id' in local_var_params:
            path_params['conversationId'] = local_var_params['conversation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'participant_leave_body' in local_var_params:
            body_params = local_var_params['participant_leave_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/apps/{appId}/conversations/{conversationId}/leave', 'POST',
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

    def list_participants(self, app_id, conversation_id, **kwargs):  # noqa: E501
        """List Participants  # noqa: E501

        Lists all the participants of a particular conversation. This API is paginated through [cursor pagination](#section/Introduction/API-pagination-and-records-limits).  ```shell /v2/apps/:appId/conversations/:conversationId/participants?page[before]=26508c10541a4b0ff472e5e2 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_participants(app_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str conversation_id: Identifies the conversation. (required)
        :param Page page: Contains parameters for applying cursor pagination.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ParticipantListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_participants_with_http_info(app_id, conversation_id, **kwargs)  # noqa: E501

    def list_participants_with_http_info(self, app_id, conversation_id, **kwargs):  # noqa: E501
        """List Participants  # noqa: E501

        Lists all the participants of a particular conversation. This API is paginated through [cursor pagination](#section/Introduction/API-pagination-and-records-limits).  ```shell /v2/apps/:appId/conversations/:conversationId/participants?page[before]=26508c10541a4b0ff472e5e2 ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_participants_with_http_info(app_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_id: Identifies the app. (required)
        :param str conversation_id: Identifies the conversation. (required)
        :param Page page: Contains parameters for applying cursor pagination.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ParticipantListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'app_id',
            'conversation_id',
            'page'
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
                    " to method list_participants" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `list_participants`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if self.api_client.client_side_validation and ('conversation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['conversation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `conversation_id` when calling `list_participants`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['appId'] = local_var_params['app_id']  # noqa: E501
        if 'conversation_id' in local_var_params:
            path_params['conversationId'] = local_var_params['conversation_id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            '/v2/apps/{appId}/conversations/{conversationId}/participants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParticipantListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
