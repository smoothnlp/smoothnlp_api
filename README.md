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
smoothnlp_api.SECRET_KEY = " YOUR Secret KEY "
```
**Call API**
```python
api_instance = smoothnlp_api.InvestmentApi()

## 配置调用Query参数
param = {"year":"2019"} ## 注意, 不同参数可能不同, 具体详情请参见接口文档
api_response = api_instance.get_investment(param) ## 返回结果为parse好的json格式, 大部分为python原生dict
```


## APIs 接口详情
#### 投资事件
`smoothnlp_api.InvestmentApi()`

**参数:** 

名称 | 类型 | 描述  | 必填  | 默认值
------------- | ------------- | ------------- | ------------- | -------------
 **cate1** | **str**| 行业一级类目 | 否 | 
 **cate2** | **str**| 行业二级类目 | 否 | 
 **company_name** | **str**| 企业工商名称 | 否 | 
 **product_name** | **str**| 项目名称 | 否 | 
 **year** | **str**| 融资年份, 如: 2019 | 否 | 
 
 **注:**
* 目前支持的行业以及类目有: '金融', '旅游', '广告营销', '教育', '新工业', '本地生活', '医疗健康', '房产服务', '电子商务', '工具软件', '文娱传媒', '硬件', '社交网络', '农业', '体育运动', '游戏', '物流', '汽车交通', '企业服务'
* 默认单次返回最多5条数据. 