# smoothnlp_api
公共数据API服务

## Install 安装
```bash
pip install smoothnlp_api
```

## Usage 使用
**Set Up**
```python
import smoothnlp_api
smoothnlp_api.config.setAuth(" YOUR Secret ID ",  ## 配置秘钥
                             " YOUR Secret KEY ")
```

**Call API**
```python
## 创建对应的 API Instance
api_instance = smoothnlp_api.InvestmentApi()

## 配置调用Query参数
param = {"year":"2019"} ## 注意, 不同参数可能不同, 具体详情请参见接口文档
api_response = api_instance.get_investment(param) ## 返回结果为parse好的json格式, 大部分为python原生dict
```


## APIs 接口详情

#### 投资事件
`smoothnlp_api.InvestmentApi()`[具体文档](http://doc.smoothnlp.com/web/#/p/4072db16dc854ef182561a8c75b6f6b6)

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

---------

#### 新闻资讯
`smoothnlp_api.NewsApi()` [具体文档](http://doc.smoothnlp.com/web/#/p/e42fdc345ca760e9a9b207ea77a8ac3c)

**参数:**

名称 | 类型 | 描述  | 必填  | 默认值
------------- | ------------- | ------------- | ------------- | -------------
 **company_kw** | **str**| 公司简称或全称 | 是 | 腾讯 
 **start_date** | **str**| 开始日期 | 否 | 2019-06-01
 **end_date** | **str**| 接入日期 | 否 | 2020-12-30
 **offset** | **int**| 开始条数 | 否 | 
 **limit** | **int**| 返回条数 | 否 | 
 
 **示例**
```python
>> import smoothnlp_api
>> api_instance = smoothnlp_api.NewsApi()
>> api_instance.get_company_news(company_kw="阿里巴巴")
```

-------------

#### 企业工商
`smoothnlp_api.CompanyApi()` [具体文档](http://doc.smoothnlp.com/web/#/p/c18fa97554fd4220bee162e1f4d948f8)

**参数**

名称 | 类型 | 描述  | 必填  | 默认值
------------- | ------------- | ------------- | ------------- | -------------
 **name** | **str**| 公司(工商)名称 | 是 | 
 
**示例**
```python
>> import smoothnlp_api
>> api_instance = smoothnlp_api.CompanyApi()
>> api_instance.get_company_fuzzy(name='今日头条')
>> api_instance.get_company_exact(name="深圳市腾讯计算机系统有限公司")

```
 
 


# 声明
> 如果你对以上数据API感兴趣, 我们对**学术研究**开放我们的数据, 欢迎联系:contact@smoothnlp.com; 我们将免费分配你对应接口的*秘钥*

> 商务合作请联系 business@smoothnlp.com

