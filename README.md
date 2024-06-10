# LeDQA

## Introduction
LeDQA is the first Chinese legal case document-based question answering dataset to our best knowledge. Specifically, we build a comprehensive question schema (including 48 element-based questions) for the Chinese civil law by legal professionals and annotate the relevant sentences to these questions in each case document. The constructed dataset originates from Chinese civil cases and contains 100 case documents, 4,800 case-question pairs and 132,048 sentence-level relevance annotations.

## Data Format

### Question Schema
The question schema can be found in `QuestionSchema.json`. Here are 48 questions from 10 categories. We take one category as an example.
```json
{
    "担保情况 - Guarantee situations": {
        "是否有担保？": "Is there a guarantee?",
        "是否由公司担保？": "Is it guaranteed by the company?",
        "是否由个人担保？": "Is it guaranteed by an individual?",
        "担保是否经过公司内部决议？": "Has the guarantee been approved by internal resolution of the company?",
        "是否对外担保？": "Is it guaranteed externally?",
        "是否公司对外分支结构？": "Is it a branch structure of the company?",
        "是否有多个责任人？": "Are there multiple responsible parties?",
        "担保人是否是夫妻、法定代表人及负责人、独资企业？": "Is the guarantor a spouse, legal representative or person in charge, or a sole proprietorship?",
        "是否存在法定代表人以自己名义签订合同的情况？": "Is there a situation where the legal representative signs the contract in his own name?"
    }
}
```

### Legal Case Documents
The legal case documents can be found in `CaseDocs.json`. Each piece of data consists of a case ID and its corresponding content. We take one case as an example.
```json
{
    "3565": "【一审法院查明】一审法院认定事实：魏欢欢、张磊系夫妻关系。周琦为融丰投资中心的执行事务合伙人。2013年12月24日，张磊通过银行汇款方式向融丰投资中心转账5万元，该款用途标注为理财产品。2014年1月15日，魏欢欢向融丰投资中心转账5万元，该款用途标注为理财。2016年11月18日，周琦向魏欢欢、张磊出具借条一张。内容为：今有周琦向魏欢欢、张磊各借款五万元共计十万元整。上述欠款约定于2017年12月12日前还清。借款：周琦。此后周琦未向魏欢欢、张磊还款，魏欢欢、张磊即提起诉讼。一审庭审中，周琦否认上述款项为周琦个人借款。同时，双方一致认可借条内容为魏欢欢、张磊书写，周琦签署了“借款：周琦”的内容。同时，魏欢欢、张磊否认该款是对融丰投资中心的理财款。【本院查明】二审中，当事人未提交新证据。本院对一审法院查明的事实予以确认。"
}
```

### Answers
We annotate the answers for all the case-question pairs and save them in the folder `answer`. And for each document, we save the answers for it in the file `caseID.json`. We show the `answer/3098.json` as the example.
```json
[
{"question": 1, "answer": "是"},
{"question": 2, "answer": "是"},
{"question": 3, "answer": "是"},
{"question": 4, "answer": "是"},
{"question": 5, "answer": "是"},
{"question": 6, "answer": "否"},
{"question": 7, "answer": "是"},
{"question": 8, "answer": "否"},
{"question": 9, "answer": "否"},
{"question": 10, "answer": "是"},
{"question": 11, "answer": "是"},
{"question": 12, "answer": "本金及利息"},
{"question": 13, "answer": "是"},
{"question": 14, "answer": "是"},
{"question": 15, "answer": "是"},
{"question": 16, "answer": "是"},
{"question": 17, "answer": "否"},
{"question": 18, "answer": "是"},
{"question": 19, "answer": "不知道"},
{"question": 20, "answer": "否"},
{"question": 21, "answer": "是"},
{"question": 22, "answer": "是"},
{"question": 23, "answer": "否"},
{"question": 24, "answer": "否"},
{"question": 25, "answer": "不知道"},
{"question": 26, "answer": "是"},
{"question": 27, "answer": "否"},
{"question": 28, "answer": "是"},
{"question": 29, "answer": "否"},
{"question": 30, "answer": "是"},
{"question": 31, "answer": "是"},
{"question": 32, "answer": "不知道"},
{"question": 33, "answer": "否"},
{"question": 34, "answer": "是"},
{"question": 35, "answer": "否"},
{"question": 36, "answer": "否"},
{"question": 37, "answer": "否"},
{"question": 38, "answer": "否"},
{"question": 39, "answer": "否"},
{"question": 40, "answer": "否"},
{"question": 41, "answer": "否"},
{"question": 42, "answer": "否"},
{"question": 43, "answer": "是"},
{"question": 44, "answer": "否"},
{"question": 45, "answer": "否"},
{"question": 46, "answer": "是"},
{"question": 47, "answer": "否"},
{"question": 48, "answer": "是"}
]
```

### Relevant Sentences
We annotate the relevant sentences for all the case-question pairs and save them in the folder `Relevant sentences`. And for each document, we save the relevant sentences with the number for it in the file `caseID.json`. We show the `sentences/104.json` as the example.
```json
[
{"question": 1, "sentence_number": 1, "sentence": "若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担。"},
{"question": 2, "sentence_number": 1, "sentence": "若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担。"},
{"question": 3, "sentence_number": 2, "sentence": "本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 4, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元  \n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金  \n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 5, "sentence_number": 1, "sentence": "若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担。"},
{"question": 6, "sentence_number": 14, "sentence": "波卉公司成立于2015年10月16日，股东为案外人刘某、张某2及戴波，戴波持股40%，公司经营范围为“从事电源、电力设备、半导体设备（除特种设备）科技领域内的技术开发、技术咨询、技术服务（除承装、承修、承试电力设施），自动化控制设备安装、调试、维修（除特种设备），半导体设备安装、维修（除特种设备），电力设备及配件，自动化控制设备及配件，半导体设备及配件销售……”，揭蓉亦参与波卉公司经营管理\n亿隅公司成立于2015年11月11日，2019年10月23日其股东变更为A中心持股34.5%、上海B管理中心（有限合伙）持股65.5%，公司经营范围变更为“从事半导体设备、电力科技、电源科技领域内的技术开发、技术咨询、技术转让、技术服务，电力设备及配件、自动化控制设备及配件、半导体设备及配件生产销售，自动化控制设备安装、调试、维修，货物或技术进出口”\n2017年4月12日，波卉公司与上海XX有限公司签订《通用厂房租赁合同》一份，约定波卉公司于2017年5月1日至2020年4月30日租赁上海市张江高科技园区XX路XX号XX幢一楼F1-2室作为办公场所\n后波卉公司、亿隅公司与上海XX有限公司签订《通用厂房出租合同主体变更协议》，约定自2019年8月1日起将上述协议承租方由波卉公司变更为亿隅公司\n上述协议签订后，该办公场所由亿隅公司使用，2019年8月起的租金由亿隅公司向上海XX有限公司支付\n2019年12月20日，亿隅公司到“应届生求职网”发布校园招聘信息，联系人邮箱后缀为“＠bowietek.com”\n2019年10月8日亿隅公司提供给客户的维修合同、2019年10月15日亿隅公司提供给客户的预检报告书首部均有“XX”标识\n波卉公司于国家企业信用信息公示系统公布的2015年至2018年年度报告显示地址均为亿隅公司现地址、电话与上述预检报告书所示电话一致\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司\n2019年7月，波卉公司欲引进投资人，与亿隅公司进行磋商\n2019年10月30日，亿隅公司员工吉某参与孙灵敏与戴波间就债务问题的沟通\n2019年11月1日，戴波与亿隅公司签订劳动合同，担任亿隅公司研发总监\n同日，波卉公司员工张某1与亿隅公司签订劳动合同，担任亿隅公司财务"},
{"question": 7, "sentence_number": 3, "sentence": "戴波与揭蓉系夫妻关系，揭蓉系A中心出资占比98%的无限责任合伙人\n戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 8, "sentence_number": 5, "sentence": "戴波与揭蓉系夫妻关系，揭蓉系A中心出资占比98%的无限责任合伙人\n戴波持股40%\n2019年10月23日其股东变更为A中心持股34.5%\n戴波、波卉公司向孙灵敏出具欠条一份\n戴波与亿隅公司签订劳动合同，担任亿隅公司研发总监"},
{"question": 9, "sentence_number": 8, "sentence": "2017年4月12日，波卉公司与上海XX有限公司签订《通用厂房租赁合同》一份，约定波卉公司于2017年5月1日至2020年4月30日租赁上海市张江高科技园区XX路XX号XX幢一楼F1-2室作为办公场所\n后波卉公司、亿隅公司与上海XX有限公司签订《通用厂房出租合同主体变更协议》，约定自2019年8月1日起将上述协议承租方由波卉公司变更为亿隅公司\n2019年10月8日亿隅公司提供给客户的维修合同、2019年10月15日亿隅公司提供给客户的预检报告书首部均有“XX”标识\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n2019年10月30日，亿隅公司员工吉某参与孙灵敏与戴波间就债务问题的沟通\n2019年11月1日，戴波与亿隅公司签订劳动合同，担任亿隅公司研发总监\n同日，波卉公司员工张某1与亿隅公司签订劳动合同，担任亿隅公司财务"},
{"question": 10, "sentence_number": 7, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司"},
{"question": 11, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 12, "sentence_number": 4, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”"},
{"question": 13, "sentence_number": 2, "sentence": "2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元"},
{"question": 14, "sentence_number": 2, "sentence": "经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元。\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金。"},
{"question": 15, "sentence_number": 1, "sentence": "若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金"},
{"question": 16, "sentence_number": 1, "sentence": "若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 17, "sentence_number": 0, "sentence": ""},
{"question": 18, "sentence_number": 3, "sentence": "波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”。\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元。\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担。"},
{"question": 19, "sentence_number": 9, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 20, "sentence_number": 2, "sentence": "若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元"},
{"question": 21, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元  \n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金  \n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担  "},
{"question": 22, "sentence_number": 5, "sentence": "2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通"},
{"question": 23, "sentence_number": 1, "sentence": "亿隅公司对孙灵敏提交的证据的真实性予以认可，关联性不予认可"},
{"question": 24, "sentence_number": 9, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 25, "sentence_number": 10, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担\n2019年10月30日，亿隅公司员工吉某参与孙灵敏与戴波间就债务问题的沟通"},
{"question": 26, "sentence_number": 4, "sentence": "孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”"},
{"question": 27, "sentence_number": 4, "sentence": "戴波与揭蓉系夫妻关系，揭蓉系A中心出资占比98%的无限责任合伙人  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n戴波、波卉公司、揭蓉未发表质证意见  \n戴波、波卉公司、揭蓉、亿隅公司二审中均未提交新证据"},
{"question": 28, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元  \n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金  \n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 29, "sentence_number": 0, "sentence": ""},
{"question": 30, "sentence_number": 8, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司\n2019年10月30日，亿隅公司员工吉某参与孙灵敏与戴波间就债务问题的沟通"},
{"question": 31, "sentence_number": 6, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司"},
{"question": 32, "sentence_number": 4, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”  \n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”  \n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”  \n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”"},
{"question": 33, "sentence_number": 3, "sentence": "本院组织当事人进行了证据交换和质证\n亿隅公司对孙灵敏提交的证据的真实性予以认可，关联性不予认可\n本院认证认为，因亿隅公司对孙灵敏提交证据的真实性予以认可，故本院对上述证据的真实性予以确认，但其证明内容，则根据全案证据予以综合分析"},
{"question": 34, "sentence_number": 6, "sentence": "2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 35, "sentence_number": 5, "sentence": "孙灵敏向本院提交波卉公司员工之间的聊天记录，欲证明揭蓉通知员工使用亿隅公司的信息开票。\n戴波、波卉公司、揭蓉未发表质证意见。\n亿隅公司对孙灵敏提交的证据的真实性予以认可，关联性不予认可。\n戴波、波卉公司、揭蓉、亿隅公司二审中均未提交新证据。\n本院认证认为，因亿隅公司对孙灵敏提交证据的真实性予以认可，故本院对上述证据的真实性予以确认，但其证明内容，则根据全案证据予以综合分析。"},
{"question": 36, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 37, "sentence_number": 9, "sentence": "孙灵敏向本院提交波卉公司员工之间的聊天记录，欲证明揭蓉通知员工使用亿隅公司的信息开票\n2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2017年5月3日，波卉公司申请备案网站域名“XX.com”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元"},
{"question": 38, "sentence_number": 4, "sentence": "戴波、波卉公司、揭蓉未发表质证意见  \n亿隅公司对孙灵敏提交的证据的真实性予以认可，关联性不予认可  \n戴波、波卉公司、揭蓉、亿隅公司二审中均未提交新证据  \n本院认证认为，因亿隅公司对孙灵敏提交证据的真实性予以认可，故本院对上述证据的真实性予以确认，但其证明内容，则根据全案证据予以综合分析"},
{"question": 39, "sentence_number": 5, "sentence": "戴波与揭蓉系夫妻关系，揭蓉系A中心出资占比98%的无限责任合伙人\n2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”"},
{"question": 40, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元  \n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金  \n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 41, "sentence_number": 8, "sentence": "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”\n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”\n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”\n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”\n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通\n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n2019年11月1日，戴波与亿隅公司签订劳动合同，担任亿隅公司研发总监\n同日，波卉公司员工张某1与亿隅公司签订劳动合同，担任亿隅公司财务"},
{"question": 42, "sentence_number": 5, "sentence": "2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”  \n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”  \n2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”  \n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  "},
{"question": 43, "sentence_number": 1, "sentence": "若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担。"},
{"question": 44, "sentence_number": 5, "sentence": "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元  \n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金  \n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 45, "sentence_number": 7, "sentence": "【本院查明】本院二审期间，当事人围绕上诉请求依法提交了证据  \n本院组织当事人进行了证据交换和质证  \n孙灵敏向本院提交波卉公司员工之间的聊天记录，欲证明揭蓉通知员工使用亿隅公司的信息开票  \n戴波、波卉公司、揭蓉未发表质证意见  \n亿隅公司对孙灵敏提交的证据的真实性予以认可，关联性不予认可  \n戴波、波卉公司、揭蓉、亿隅公司二审中均未提交新证据  \n本院认证认为，因亿隅公司对孙灵敏提交证据的真实性予以认可，故本院对上述证据的真实性予以确认，但其证明内容，则根据全案证据予以综合分析  "},
{"question": 46, "sentence_number": 4, "sentence": "戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元\n经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元\n若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金\n若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担"},
{"question": 47, "sentence_number": 8, "sentence": "后波卉公司、亿隅公司与上海XX有限公司签订《通用厂房出租合同主体变更协议》，约定自2019年8月1日起将上述协议承租方由波卉公司变更为亿隅公司\n上述协议签订后，该办公场所由亿隅公司使用，2019年8月起的租金由亿隅公司向上海XX有限公司支付\n2019年12月20日，亿隅公司到“应届生求职网”发布校园招聘信息，联系人邮箱后缀为“＠bowietek.com”\n上述办公场所由亿隅公司租赁后，该商标曾仍显示于办公场所玻璃门上，本案诉讼期间亿隅公司拆除\n2019年10月8日亿隅公司提供给客户的维修合同、2019年10月15日亿隅公司提供给客户的预检报告书首部均有“XX”标识\n波卉公司于国家企业信用信息公示系统公布的2015年至2018年年度报告显示地址均为亿隅公司现地址、电话与上述预检报告书所示电话一致\n2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司\n孙灵敏向本院提交波卉公司员工之间的聊天记录，欲证明揭蓉通知员工使用亿隅公司的信息开票"},
{"question": 48, "sentence_number": 15, "sentence": "戴波与揭蓉系夫妻关系，揭蓉系A中心出资占比98%的无限责任合伙人  \n波卉公司成立于2015年10月16日，股东为案外人刘某、张某2及戴波，戴波持股40%  \n后波卉公司、亿隅公司与上海XX有限公司签订《通用厂房出租合同主体变更协议》，约定自2019年8月1日起将上述协议承租方由波卉公司变更为亿隅公司  \n2017年5月3日，波卉公司申请备案网站域名“XX.com”  \n2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”  \n2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”  \n2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”  \n波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”  \n2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通  \n同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元  \n2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司  \n2019年7月，波卉公司欲引进投资人，与亿隅公司进行磋商  \n2019年11月1日，戴波与亿隅公司签订劳动合同，担任亿隅公司研发总监  \n同日，波卉公司员工张某1与亿隅公司签订劳动合同，担任亿隅公司财务  \n孙灵敏向本院提交波卉公司员工之间的聊天记录，欲证明揭蓉通知员工使用亿隅公司的信息开票"}
]
```

### Relevance Annotations
We save the sentence-level relevance annotations in the folder `Relevance Annotations`. Specifically, we save the relevance annotaions for each question-document pair in the file `Relevance Annotations/caseID/questionID.json`. For example, the annotations for the "104" case with the "13" question is shown as follows:
```json
{
    "【一审法院查明】一审法院认定事实：戴波与揭蓉系夫妻关系，揭蓉系A中心出资占比98%的无限责任合伙人；": 0,
    "波卉公司成立于2015年10月16日，股东为案外人刘某、张某2及戴波，戴波持股40%，公司经营范围为“从事电源、电力设备、半导体设备（除特种设备）科技领域内的技术开发、技术咨询、技术服务（除承装、承修、承试电力设施），自动化控制设备安装、调试、维修（除特种设备），半导体设备安装、维修（除特种设备），电力设备及配件，自动化控制设备及配件，半导体设备及配件销售……”，揭蓉亦参与波卉公司经营管理；": 0,
    "亿隅公司成立于2015年11月11日，2019年10月23日其股东变更为A中心持股34.5%、上海B管理中心（有限合伙）持股65.5%，公司经营范围变更为“从事半导体设备、电力科技、电源科技领域内的技术开发、技术咨询、技术转让、技术服务，电力设备及配件、自动化控制设备及配件、半导体设备及配件生产销售，自动化控制设备安装、调试、维修，货物或技术进出口”；": 0,
    "2017年4月12日，波卉公司与上海XX有限公司签订《通用厂房租赁合同》一份，约定波卉公司于2017年5月1日至2020年4月30日租赁上海市张江高科技园区XX路XX号XX幢一楼F1-2室作为办公场所；": 0,
    "后波卉公司、亿隅公司与上海XX有限公司签订《通用厂房出租合同主体变更协议》，约定自2019年8月1日起将上述协议承租方由波卉公司变更为亿隅公司；": 0,
    "上述协议签订后，该办公场所由亿隅公司使用，2019年8月起的租金由亿隅公司向上海XX有限公司支付；": 0,
    "2017年5月3日，波卉公司申请备案网站域名“XX.com”；": 0,
    "2019年12月20日，亿隅公司到“应届生求职网”发布校园招聘信息，联系人邮箱后缀为“＠bowietek.com”；": 0,
    "2017年8月28日，波卉公司申请注册商标“XX”；": 0,
    "上述办公场所由亿隅公司租赁后，该商标曾仍显示于办公场所玻璃门上，本案诉讼期间亿隅公司拆除；": 0,
    "2019年10月8日亿隅公司提供给客户的维修合同、2019年10月15日亿隅公司提供给客户的预检报告书首部均有“XX”标识；": 0,
    "波卉公司于国家企业信用信息公示系统公布的2015年至2018年年度报告显示地址均为亿隅公司现地址、电话与上述预检报告书所示电话一致；": 0,
    "2018年8月1日，孙灵敏向波卉公司转账200,000元，备注“入股注资波卉”；": 0,
    "2018年5月14日，孙灵敏向波卉公司转账150,000元，备注为“波卉借款”；": 1,
    "2018年5月17日，孙灵敏向波卉公司转账250,000元，备注“入股波卉”；": 0,
    "波卉公司于收款当日分别向孙灵敏出具相应金额的收据，载明“借款为孙思敏参与公司的增资款”；": 0,
    "2019年7月15日，孙灵敏与揭蓉通过微信对上述款项出具欠条事项进行沟通；": 0,
    "同日，戴波、波卉公司向孙灵敏出具欠条一份，载明：本人因公司资金周转共向孙灵敏借款600,000元；": 0,
    "经协商，借款利息为年息一分，还款日为2019年11月10日，自2018年10月1日开始计息，利息为66,666.67元，应还总额为666,666.67元；": 1,
    "若到期未能归还，本人愿承担以未还本金加利息为基数、按照每日0.4‰计算的违约金；": 0,
    "若欠款人未按期归还导致诉讼的，因诉讼产生的诉讼费、保全费（包括但不限于法院收取的保全费、债权人为采取诉讼保全而由担保公司或担保人提供担保物而产生的担保费等）、执行费、律师费等费用由欠款人承担；": 0,
    "2020年3月6日，孙灵敏以亿隅公司业务审计人员身份与波卉公司原客户通电话，客户确认于2019年9月左右波卉公司曾发函表示后续业务由亿隅公司接替波卉公司；": 0,
    "一审法院另查明，2019年7月，波卉公司欲引进投资人，与亿隅公司进行磋商；": 0,
    "2019年10月30日，亿隅公司员工吉某参与孙灵敏与戴波间就债务问题的沟通；": 0,
    "2019年11月1日，戴波与亿隅公司签订劳动合同，担任亿隅公司研发总监；": 0,
    "同日，波卉公司员工张某1与亿隅公司签订劳动合同，担任亿隅公司财务；": 0,
    "【本院查明】本院二审期间，当事人围绕上诉请求依法提交了证据；": 0,
    "本院组织当事人进行了证据交换和质证；": 0,
    "孙灵敏向本院提交波卉公司员工之间的聊天记录，欲证明揭蓉通知员工使用亿隅公司的信息开票；": 0,
    "戴波、波卉公司、揭蓉未发表质证意见；": 0,
    "亿隅公司对孙灵敏提交的证据的真实性予以认可，关联性不予认可；": 0,
    "戴波、波卉公司、揭蓉、亿隅公司二审中均未提交新证据；": 0,
    "本院认证认为，因亿隅公司对孙灵敏提交证据的真实性予以认可，故本院对上述证据的真实性予以确认，但其证明内容，则根据全案证据予以综合分析；": 0
}
```
