# coding: utf-8

"""
    Company

    企业相关信息 - 工商  * 默认域名： service-1ffy5rfz-1259459016.ap-shanghai.apigateway.myqcloud.com/release * 自定义域名： data.service.company.smoothnlp.com/   # noqa: E501
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


SecretId = None
SecretKey = None

HOST = "http://data.service.company.smoothnlp.com"


class CompanyApi(object):
  

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @evaldata
    def get_company_exact(self, name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_exact_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_exact_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_exact_with_http_info(self, name, **kwargs):  # noqa: E501
        

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_exact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_company_exact`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
        return self.api_client.call_api( HOST,
            '/company_exact', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_company_fuzzy(self, name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_fuzzy_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_fuzzy_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_fuzzy_with_http_info(self, name, **kwargs):  # noqa: E501
        

        all_params = ['name', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_fuzzy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_company_fuzzy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
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
        #此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign




        header_params['Source'] = Source
        return self.api_client.call_api(HOST,
            '/company_fuzzy', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_company_member(self, name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_member_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_member_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_member_with_http_info(self, name, **kwargs):  # noqa: E501
        

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_company_member`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
        return self.api_client.call_api(HOST,
            '/company/member', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_company_outbound_share(self, name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_outbound_share_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_outbound_share_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_outbound_share_with_http_info(self, name, **kwargs):  # noqa: E501
        

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
                    " to method get_company_outbound_share" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_company_outbound_share`")  # noqa: E501

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
        #此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign




        header_params['Source'] = Source
        return self.api_client.call_api(HOST,
            '/company/outbound_share', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_company_shareholder(self, name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_shareholder_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_shareholder_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_shareholder_with_http_info(self, name, **kwargs):  # noqa: E501
        

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_shareholder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_company_shareholder`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
        return self.api_client.call_api(HOST,
            '/company/shareholder', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_company_trademark(self, name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_trademark_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_trademark_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_company_trademark_with_http_info(self, name, **kwargs):  # noqa: E501
        

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
                    " to method get_company_trademark" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_company_trademark`")  # noqa: E501

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
        #此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign




        header_params['Source'] = Source
        return self.api_client.call_api(HOST,
            '/company/trademark', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
    def get_competition_by_company_name(self, company_name, **kwargs):  # noqa: E501
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_competition_by_company_name_with_http_info(company_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_competition_by_company_name_with_http_info(company_name, **kwargs)  # noqa: E501
            return data

    def get_competition_by_company_name_with_http_info(self, company_name, **kwargs):  # noqa: E501
        

        all_params = ['company_name', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_competition_by_company_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_name' is set
        if ('company_name' not in params or
                params['company_name'] is None):
            raise ValueError("Missing the required parameter `company_name` when calling `get_competition_by_company_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_name' in params:
            query_params.append(('company_name', params['company_name']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        #此api为秘钥对验证
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign




        header_params['Source'] = Source
        return self.api_client.call_api(HOST,
            '/competition_by_company_name', 'GET',    #如果此API为ANY方法，则默认为GET方法，您可以通过修改第二个参数来变更您想使用的方法，如POST,PUT，HEAD等，注意:当存在body参数时，请不要使用HEAD或GET方法
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
