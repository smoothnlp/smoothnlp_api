# coding: utf-8

"""
    NLP

    NLP Pipeline 处理  * 默认域名： service-hvlkvptv-1259459016.ap-shanghai.apigateway.myqcloud.com/release * 自定义域名： data.service.nlp.smoothnlp.com/   # noqa: E501
"""

from __future__ import absolute_import

import requests
import datetime
import hashlib
import hmac
import base64

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from smoothnlp_api import getSimpleSign
import smoothnlp_api
from ..api_client import ApiClient
from ..api import evaldata

SecretId = smoothnlp_api.config.SECRET_ID
SecretKey = smoothnlp_api.config.SECRET_KEY

HOST = "http://data.service.nlp.smoothnlp.com"


class NLPApi(object):
  

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @evaldata
    def get(self, text, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_with_http_info(text, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(text, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, text, **kwargs):  # noqa: E501
        

        all_params = ['text']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['HTML'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        
        # Source等从这里加入 header_params
        Source = 'AndriodApp'  # 可自定义
        
#####flag#####
        #此api无任何认证方式


        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @evaldata
    def get_parsedate(self, givendate, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_parsedate_with_http_info(givendate, **kwargs)  # noqa: E501
        else:
            (data) = self.get_parsedate_with_http_info(givendate, **kwargs)  # noqa: E501
            return data

    def get_parsedate_with_http_info(self, givendate, **kwargs):  # noqa: E501
        

        all_params = ['givendate', 'pubdate']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_parsedate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'givendate' is set
        if ('givendate' not in params or
                params['givendate'] is None):
            raise ValueError("Missing the required parameter `givendate` when calling `get_parsedate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'givendate' in params:
            query_params.append(('givendate', params['givendate']))  # noqa: E501
        if 'pubdate' in params:
            query_params.append(('pubdate', params['pubdate']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['HTML'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        
        # Source等从这里加入 header_params
        Source = 'AndriodApp'  # 可自定义
        
#####flag#####
        #此api无任何认证方式




        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/parsedate', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @evaldata
    def get_split2sentences(self, text, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_split2sentences_with_http_info(text, **kwargs)  # noqa: E501
        else:
            (data) = self.get_split2sentences_with_http_info(text, **kwargs)  # noqa: E501
            return data

    def get_split2sentences_with_http_info(self, text, **kwargs):  # noqa: E501
        

        all_params = ['text']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_split2sentences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `get_split2sentences`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['JSON'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        
        # Source等从这里加入 header_params
        Source = 'AndriodApp'  # 可自定义
        
#####flag#####
        #此api无任何认证方式




        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/split2sentences', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
