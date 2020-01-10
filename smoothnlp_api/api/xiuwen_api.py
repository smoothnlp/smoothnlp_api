# coding: utf-8

"""
    xiuwen

    不对外公开, 仅仅支持嗅问前段  * 默认域名： service-cisism3l-1259459016.ap-shanghai.apigateway.myqcloud.com/release * 自定义域名： data.service.xiuwen.smoothnlp.com/   # noqa: E501
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

HOST = "http://data.service.xiuwen.smoothnlp.com"

class XiuwenApi(object):
  

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @evaldata
    def get_company_search(self, name, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_search_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_search_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_search_with_http_info(self, name, **kwargs):  # noqa: E501

        all_params = ['name', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError(
                "Missing the required parameter `name` when calling `get_company_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
        # 此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign

        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/company/search', 'GET',
            # 如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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



    def get_news_event_kw(self, offset, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_news_event_kw_with_http_info(offset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_news_event_kw_with_http_info(offset, **kwargs)  # noqa: E501
            return data

    def get_news_event_kw_with_http_info(self, offset, **kwargs):  # noqa: E501
        

        all_params = ['offset', 'event', 'text']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_news_event_kw" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `get_news_event_kw`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'event' in params:
            query_params.append(('event', params['event']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
        #此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign




        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/news/event/kw', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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

    def get_news_kw(self, kw, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_news_kw_with_http_info(kw, **kwargs)  # noqa: E501
        else:
            (data) = self.get_news_kw_with_http_info(kw, **kwargs)  # noqa: E501
            return data

    def get_news_kw_with_http_info(self, kw, **kwargs):  # noqa: E501
        

        all_params = ['kw', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_news_kw" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kw' is set
        if ('kw' not in params or
                params['kw'] is None):
            raise ValueError("Missing the required parameter `kw` when calling `get_news_kw`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'kw' in params:
            query_params.append(('kw', params['kw']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
        #此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign




        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/news/kw', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_processcorpus(self, text, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_processcorpus_with_http_info(text, **kwargs)  # noqa: E501
        else:
            (data) = self.get_processcorpus_with_http_info(text, **kwargs)  # noqa: E501
            return data

    def get_processcorpus_with_http_info(self, text, **kwargs):  # noqa: E501
        

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
                    " to method get_processcorpus" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `get_processcorpus`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'text' in params:
            header_params['text'] = params['text'].encode('utf-8')  # noqa: E501

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
            '/processcorpus', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
