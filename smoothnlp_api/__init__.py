# coding: utf-8

# flake8: noqa

"""
    Investment

    投资事件(主要来源ITjuzi)  * 默认域名： service-m5j3awiv-1259459016.ap-shanghai.apigateway.myqcloud.com/release * 自定义域名： data.service.invest.smoothnlp.com/   # noqa: E501
"""


from __future__ import absolute_import

global SECRET_ID
global SECRET_KEY

SECRET_ID = None
SECRET_KEY = None

# import apis into sdk package
from smoothnlp_api.api.investment_api import InvestmentApi

# import ApiClient
from smoothnlp_api.api_client import ApiClient
from smoothnlp_api.configuration import Configuration
# import models into sdk package

import logging

logger = logging.getLogger("data_service_logger")

def setKey(secrete_id,secret_key):
    SECRET_ID = secrete_id
    SECRET_KEY = secret_key


