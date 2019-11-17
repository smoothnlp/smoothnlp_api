# coding: utf-8

# flake8: noqa

"""
    Investment

    投资事件(主要来源ITjuzi)  * 默认域名： service-m5j3awiv-1259459016.ap-shanghai.apigateway.myqcloud.com/release * 自定义域名： data.service.invest.smoothnlp.com/   # noqa: E501
"""


from __future__ import absolute_import

global SECRET_ID
global SECRET_KEY

import logging
import hmac
import base64
import datetime
import hashlib

logger = logging.getLogger("data_service_logger")

from smoothnlp_api.configuration import Configuration
config = Configuration()

def getSimpleSign(source, SecretId = None, SecretKey=None):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    if SecretId ==  "" or SecretKey == "" or config.SECRET_KEY is None or config.SECRET_ID is None:
        logger.fatal("请先设置 SecretId/SecretKey 对，再计算签名")
        raise ConnectionError(" Invalid Secret ID or Key ")
    dateTime = datetime.datetime.utcnow().strftime(GMT_FORMAT)  # 这里，用当前时间来生成 datetime 对象
    auth = "hmac id=\"" + config.SECRET_ID + "\", algorithm=\"hmac-sha1\", headers=\"date source\", signature=\""
    signStr = "date: " + dateTime + "\n" + "source: " + source

    sign = hmac.new(config.SECRET_KEY.encode('utf-8'), signStr.encode("utf-8"), hashlib.sha1).digest()
    sign = base64.b64encode(sign)
    sign = sign.decode('utf-8')
    sign = auth + sign + "\""

    return sign, dateTime



# import apis into sdk package
from .api.investment_api import InvestmentApi
from .api.news_api import NewsApi
from .api.company_api import CompanyApi
from .api.xiuwen_api import XiuwenApi

# import ApiClient
from smoothnlp_api.api_client import ApiClient

# import models into sdk package


