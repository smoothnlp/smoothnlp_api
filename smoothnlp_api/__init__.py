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


def getSimpleSign(source, SecretId, SecretKey):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    if SecretId ==  "" or SecretKey == "" or SecretKey is None or SecretId is None:
        logger.fatal("请先设置 SecretId/SecretKey 对，再计算签名")
        raise ConnectionError(" Invalid Secret ID or Key ")
    dateTime = datetime.datetime.utcnow().strftime(GMT_FORMAT)  # 这里，用当前时间来生成 datetime 对象
    auth = "hmac id=\"" + SecretId + "\", algorithm=\"hmac-sha1\", headers=\"date source\", signature=\""
    signStr = "date: " + dateTime + "\n" + "source: " + source

    sign = hmac.new(SecretKey.encode('utf-8'), signStr.encode("utf-8"), hashlib.sha1).digest()
    sign = base64.b64encode(sign)
    sign = sign.decode('utf-8')
    sign = auth + sign + "\""

    return sign, dateTime

# import apis into sdk package
from smoothnlp_api.api.investment_api import InvestmentApi
from smoothnlp_api.api.news_api import NewsApi
from smoothnlp_api.api.company_api import CompanyApi

# import ApiClient
from smoothnlp_api.api_client import ApiClient
from smoothnlp_api.configuration import Configuration
# import models into sdk package

config = Configuration()

