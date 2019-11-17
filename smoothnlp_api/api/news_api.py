# coding: utf-8

"""
    News

    资讯信息查询接口  * 默认域名： service-nl4at3t9-1259459016.ap-shanghai.apigateway.myqcloud.com/release * 自定义域名： data.service.news.smoothnlp.com/release   # noqa: E501
"""


from __future__ import absolute_import


# python 2 and python 3 compatibility library
import six

from smoothnlp_api.api_client import ApiClient
import smoothnlp_api
from smoothnlp_api import getSimpleSign

# SecretId = smoothnlp_api.SECRET # !!!!!!!在此填入SecretKey!!!!!!

HOST = "http://data.service.news.smoothnlp.com/"

class NewsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_company_news(self, company_kw, **kwargs):  # noqa: E501

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_company_news_with_http_info(company_kw, **kwargs)  # noqa: E501
        else:
            (data) = self.get_company_news_with_http_info(company_kw, **kwargs)  # noqa: E501
            data = eval(data)
            return data

    def get_company_news_with_http_info(self, company_kw, **kwargs):  # noqa: E501

        all_params = ['company_kw', 'end_date', 'limit', 'offset', 'start_date']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_news" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_kw' is set
        if ('company_kw' not in params or
                params['company_kw'] is None):
            raise ValueError(
                "Missing the required parameter `company_kw` when calling `get_company_news`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_kw' in params:
            query_params.append(('company_kw', params['company_kw']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501

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
        sign, dateTime = getSimpleSign(Source, smoothnlp_api.config.SECRET_ID, smoothnlp_api.config.SECRET_KEY)
        header_params['Date'] = dateTime
        header_params['Authorization'] = sign

        header_params['Source'] = Source
        return self.api_client.call_api(
            HOST,
            '/news/company',
            'GET',
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
