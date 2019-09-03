# smoothnlp_api
公共数据API服务

## Install 安装
```python
pip install smoothnlp_api
```

## Usage 使用
**Set Up**
```python
import smoothnlp_api
smoothnlp_api.SECRET_ID = " YOUR Secret ID "  ## 配置秘钥
smoothnlp_api.SECRET_KEY = " YOUR Secret KEY"
```
**Call API**
```python
api_instance = smoothnlp_api.InvestmentApi()

## 配置调用Query参数
param = {"year":"2019"} ## 注意, 不同参数可能不同, 具体详情请参见接口文档
api_response = api_instance.get_investment(param) ## 返回结果为parse好的json格式, 大部分为python原生dict
```
